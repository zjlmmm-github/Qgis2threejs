# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qgis2threejs
                                 A QGIS plugin
 export terrain data, map canvas image and vector data to web browser
                              -------------------
        begin                : 2014-01-16
        copyright            : (C) 2014 Minoru Akagi
        email                : akaginch@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os

from PyQt4.QtCore import QDir, Qt
from PyQt4.QtGui import QColor, QImage, QImageReader, QPainter
from qgis.core import QGis, QgsMapRenderer, QgsPalLabeling, QgsMessageLog

import gdal2threejs
import qgis2threejstools as tools


class DataManager:
  """ manages a list of unique items """

  def __init__(self):
    self._list = []

  def _index(self, image):
    if image in self._list:
      return self._list.index(image)

    index = len(self._list)
    self._list.append(image)
    return index

class ImageManager(DataManager):

  IMAGE_FILE = 1
  CANVAS_IMAGE = 2
  MAP_IMAGE = 3
  LAYER_IMAGE = 4

  def __init__(self, context):
    DataManager.__init__(self)
    self.context = context
    self._renderer = None

  def imageIndex(self, path):
    img = (self.IMAGE_FILE, path)
    return self._index(img)

  def canvasImageIndex(self, transp_background):
    img = (self.CANVAS_IMAGE, transp_background)
    return self._index(img)

  def mapImageIndex(self, width, height, extent, transp_background):
    img = (self.MAP_IMAGE, (width, height, extent, transp_background))
    return self._index(img)

  def layerImageIndex(self, layerid, width, height, extent, transp_background):
    img = (self.LAYER_IMAGE, (layerid, width, height, extent, transp_background))
    return self._index(img)

  def mapCanvasImage(self, transp_background=False):
    """ returns base64 encoded map canvas image """
    canvas = self.context.canvas
    if transp_background:
      size = self.context.mapSettings.outputSize()
      return self.renderedImage(size.width(), size.height(), canvas.extent(), transp_background)

    if QGis.QGIS_VERSION_INT >= 20400:
     return tools.base64image(canvas.map().contentImage())
    temp_dir = QDir.tempPath()
    texfilename = os.path.join(temp_dir, "tex%s.png" % (self.context.timestamp))
    canvas.saveAsImage(texfilename)
    texData = gdal2threejs.base64image(texfilename)
    tools.removeTemporaryFiles([texfilename, texfilename + "w"])
    return texData

  def saveMapCanvasImage(self):
    texfilename = self.context.path_root + ".png"
    self.context.canvas.saveAsImage(texfilename)
    texSrc = os.path.split(texfilename)[1]
    tools.removeTemporaryFiles([texfilename + "w"])

  def _initRenderer(self):
    canvas = self.context.canvas

    # set up a renderer
    labeling = QgsPalLabeling()
    renderer = QgsMapRenderer()
    renderer.setDestinationCrs(self.context.crs)
    renderer.setProjectionsEnabled(True)
    renderer.setLabelingEngine(labeling)

    # save renderer
    self._labeling = labeling
    self._renderer = renderer

    # layer list
    self._layerids = [mapLayer.id() for mapLayer in canvas.layers()]

    # canvas color
    self.canvasColor = canvas.canvasColor()

  def renderedImage(self, width, height, extent, transp_background=False, layerids=None):
    antialias = True

    if self._renderer is None:
      self._initRenderer()

    renderer = self._renderer
    if layerids is None:
      renderer.setLayerSet(self._layerids)
    else:
      renderer.setLayerSet(layerids)

    image = QImage(width, height, QImage.Format_ARGB32_Premultiplied)
    if transp_background:
      image.fill(QColor(Qt.transparent).rgba())   #
    else:
      image.fill(self.canvasColor.rgba())   #

    renderer.setOutputSize(image.size(), image.logicalDpiX())
    renderer.setExtent(extent)

    painter = QPainter()
    painter.begin(image)
    if antialias:
      painter.setRenderHint(QPainter.Antialiasing)
    renderer.render(painter)
    painter.end()

    return tools.base64image(image)

    #if context.localBrowsingMode:
    #else:
    #  texfilename = os.path.splitext(htmlfilename)[0] + "_%d.png" % plane_index
    #  image.save(texfilename)
    #  texSrc = os.path.split(texfilename)[1]
    #  tex["src"] = texSrc

  def write(self, f):   #TODO: separated image files (not in localBrowsingMode)
    if len(self._list) == 0:
      return

    f.write(u'\n// Base64 encoded images\n')
    for index, image in enumerate(self._list):
      imageType = image[0]
      if imageType == self.IMAGE_FILE:
        image_path = image[1]
        if os.path.exists(image_path):
          size = QImageReader(image_path).size()
          args = (index, size.width(), size.height(), gdal2threejs.base64image(image_path))
        else:
          f.write(u"project.images[%d] = {data:null};\n" % index)
          QgsMessageLog.logMessage(u'Image file not found: {0}'.format(image_path), "Qgis2threejs")
          continue

      elif imageType == self.MAP_IMAGE:
        width, height, extent, transp_background = image[1]
        args = (index, width, height, self.renderedImage(width, height, extent, transp_background))

      elif imageType == self.LAYER_IMAGE:
        layerid, width, height, extent, transp_background = image[1]
        args = (index, width, height, self.renderedImage(width, height, extent, transp_background, [layerid]))

      else:   #imageType == self.CANVAS_IMAGE:
        transp_background = image[1]
        size = self.context.mapSettings.outputSize()
        args = (index, size.width(), size.height(), self.mapCanvasImage(transp_background))

      f.write(u'project.images[%d] = {width:%d,height:%d,data:"%s"};\n' % args)


class MaterialManager(DataManager):

  MESH_LAMBERT = 0
  MESH_PHONG = 1
  LINE_BASIC = 2
  SPRITE = 3

  WIREFRAME = 10
  MESH_LAMBERT_SMOOTH = 0
  MESH_LAMBERT_FLAT = 11

  CANVAS_IMAGE = 20
  MAP_IMAGE = 21
  LAYER_IMAGE = 22
  IMAGE_FILE = 23

  ERROR_COLOR = "0"

  def __init__(self):
    DataManager.__init__(self)

  def _indexCol(self, type, color, transparency=0, doubleSide=False):
    if color[0:2] != "0x":
      color = self.ERROR_COLOR
    mat = (type, color, transparency, doubleSide)
    return self._index(mat)

  def getMeshLambertIndex(self, color, transparency=0, doubleSide=False):
    return self._indexCol(self.MESH_LAMBERT, color, transparency, doubleSide)

  def getSmoothMeshLambertIndex(self, color, transparency=0, doubleSide=False):
    return self._indexCol(self.MESH_LAMBERT_SMOOTH, color, transparency, doubleSide)

  def getFlatMeshLambertIndex(self, color, transparency=0, doubleSide=False):
    return self._indexCol(self.MESH_LAMBERT_FLAT, color, transparency, doubleSide)

  def getLineBasicIndex(self, color, transparency=0):
    return self._indexCol(self.LINE_BASIC, color, transparency)

  def getWireframeIndex(self, color, transparency=0):
    return self._indexCol(self.WIREFRAME, color, transparency)

  def getCanvasImageIndex(self, transparency=0, transp_background=False):
    mat = (self.CANVAS_IMAGE, transp_background, transparency, True)
    return self._index(mat)

  def getMapImageIndex(self, width, height, extent, transparency=0, transp_background=False):
    mat = (self.MAP_IMAGE, (width, height, extent, transp_background), transparency, True)
    return self._index(mat)

  def getLayerImageIndex(self, layerid, width, height, extent, transparency=0, transp_background=False):
    mat = (self.LAYER_IMAGE, (layerid, width, height, extent, transp_background), transparency, True)
    return self._index(mat)

  def getImageFileIndex(self, path, transparency=0, transp_background=False, doubleSide=False):
    mat = (self.IMAGE_FILE, (path, transp_background), transparency, doubleSide)
    return self._index(mat)

  def getSpriteIndex(self, path, transparency=0):
    transp_background = True
    mat = (self.SPRITE, (path, transp_background), transparency, False)
    return self._index(mat)

  def write(self, f, imageManager):
    if not len(self._list):
      return

    toMaterialType = {self.WIREFRAME: self.MESH_LAMBERT,
                      self.MESH_LAMBERT_FLAT: self.MESH_LAMBERT,
                      self.CANVAS_IMAGE: self.MESH_PHONG,
                      self.MAP_IMAGE: self.MESH_PHONG,
                      self.LAYER_IMAGE: self.MESH_PHONG,
                      self.IMAGE_FILE: self.MESH_PHONG}

    for index, mat in enumerate(self._list):
      m = {"type": toMaterialType.get(mat[0], mat[0])}

      transp_background = False

      if mat[0] == self.CANVAS_IMAGE:
        transp_background = mat[1]
        m["i"] = imageManager.canvasImageIndex(transp_background)
      elif mat[0] == self.MAP_IMAGE:
        width, height, extent, transp_background = mat[1]
        m["i"] = imageManager.mapImageIndex(width, height, extent, transp_background)
      elif mat[0] == self.LAYER_IMAGE:
        layerid, width, height, extent, transp_background = mat[1]
        m["i"] = imageManager.layerImageIndex(layerid, width, height, extent, transp_background)
      elif mat[0] in [self.IMAGE_FILE, self.SPRITE]:
        filepath, transp_background = mat[1]
        m["i"] = imageManager.imageIndex(filepath)
      else:
        m["c"] = mat[1]

      if transp_background:
        m["t"] = 1

      if mat[0] == self.WIREFRAME:
        m["w"] = 1

      if mat[0] == self.MESH_LAMBERT_FLAT:
        m["flat"] = 1

      transparency = mat[2]
      if transparency > 0:
        opacity = 1.0 - float(transparency) / 100
        m["o"] = opacity

      # double sides
      if mat[3]:
        m["ds"] = 1

      f.write(u"lyr.m[{0}] = {1};\n".format(index, tools.pyobj2js(m, quoteHex=False)))

class JSONManager(DataManager):

  def __init__(self):
    DataManager.__init__(self)

  def jsonIndex(self, path):
    return self._index(path)

  def write(self, f):
    if len(self._list) == 0:
      return

    f.write(u'\n// JSON data\n')
    for index, path in enumerate(self._list):
      if os.path.exists(path):
        with open(path) as json:
          data = json.read().replace("\\", "\\\\").replace("'", "\\'").replace("\t", "\\t").replace("\r", "\\r").replace("\n", "\\n")
        f.write(u"project.jsons[%d] = {data:'%s'};\n" % (index, data))
        continue
      f.write(u"project.jsons[%d] = {data:null};\n" % index)
      QgsMessageLog.logMessage(u'JSON file not found: {0}'.format(path), "Qgis2threejs")