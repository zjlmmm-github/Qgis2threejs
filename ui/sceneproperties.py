# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\minorua\QGIS\plugins\Qgis2threejs\ui\sceneproperties.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScenePropertiesWidget(object):
    def setupUi(self, ScenePropertiesWidget):
        ScenePropertiesWidget.setObjectName("ScenePropertiesWidget")
        ScenePropertiesWidget.resize(385, 657)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ScenePropertiesWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_1 = QtWidgets.QGroupBox(ScenePropertiesWidget)
        self.groupBox_1.setObjectName("groupBox_1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_BaseSize = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_BaseSize.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_BaseSize.setObjectName("lineEdit_BaseSize")
        self.gridLayout_4.addWidget(self.lineEdit_BaseSize, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.checkBox_autoZShift = QtWidgets.QCheckBox(self.groupBox_1)
        self.checkBox_autoZShift.setObjectName("checkBox_autoZShift")
        self.gridLayout_4.addWidget(self.checkBox_autoZShift, 2, 2, 1, 1)
        self.lineEdit_zFactor = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_zFactor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_zFactor.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_zFactor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_zFactor.setObjectName("lineEdit_zFactor")
        self.gridLayout_4.addWidget(self.lineEdit_zFactor, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_1)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_zShift = QtWidgets.QLineEdit(self.groupBox_1)
        self.lineEdit_zShift.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_zShift.setObjectName("lineEdit_zShift")
        self.gridLayout_4.addWidget(self.lineEdit_zShift, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_1)
        self.groupBox_4 = QtWidgets.QGroupBox(ScenePropertiesWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_FixAspectRatio = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_FixAspectRatio.setObjectName("checkBox_FixAspectRatio")
        self.gridLayout_3.addWidget(self.checkBox_FixAspectRatio, 4, 0, 1, 1)
        self.radioButton_FixedExtent = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_FixedExtent.setObjectName("radioButton_FixedExtent")
        self.gridLayout_3.addWidget(self.radioButton_FixedExtent, 1, 0, 1, 1)
        self.radioButton_UseCanvasExtent = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_UseCanvasExtent.setChecked(True)
        self.radioButton_UseCanvasExtent.setObjectName("radioButton_UseCanvasExtent")
        self.gridLayout_3.addWidget(self.radioButton_UseCanvasExtent, 0, 0, 1, 1)
        self.gridLayout_Extent = QtWidgets.QGridLayout()
        self.gridLayout_Extent.setObjectName("gridLayout_Extent")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_Extent.addWidget(self.label_10, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_Extent.addWidget(self.label_7, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_Extent.addWidget(self.label_6, 4, 0, 1, 1)
        self.lineEdit_CenterY = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_CenterY.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_CenterY.setObjectName("lineEdit_CenterY")
        self.gridLayout_Extent.addWidget(self.lineEdit_CenterY, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_Extent.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_Extent.addWidget(self.label_5, 1, 0, 1, 1)
        self.pushButton_SelectExtent = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_SelectExtent.setObjectName("pushButton_SelectExtent")
        self.gridLayout_Extent.addWidget(self.pushButton_SelectExtent, 7, 3, 1, 1)
        self.lineEdit_Height = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_Height.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Height.setObjectName("lineEdit_Height")
        self.gridLayout_Extent.addWidget(self.lineEdit_Height, 4, 3, 1, 1)
        self.lineEdit_Width = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_Width.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Width.setObjectName("lineEdit_Width")
        self.gridLayout_Extent.addWidget(self.lineEdit_Width, 4, 1, 1, 1)
        self.lineEdit_Rotation = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_Rotation.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lineEdit_Rotation.setObjectName("lineEdit_Rotation")
        self.gridLayout_Extent.addWidget(self.lineEdit_Rotation, 7, 1, 1, 1)
        self.lineEdit_CenterX = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_CenterX.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhLowercaseOnly)
        self.lineEdit_CenterX.setObjectName("lineEdit_CenterX")
        self.gridLayout_Extent.addWidget(self.lineEdit_CenterX, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_Extent, 3, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(ScenePropertiesWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)
        self.checkBox_Outline = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Outline.setObjectName("checkBox_Outline")
        self.gridLayout_5.addWidget(self.checkBox_Outline, 1, 0, 1, 2)
        self.comboBox_MaterialType = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_MaterialType.sizePolicy().hasHeightForWidth())
        self.comboBox_MaterialType.setSizePolicy(sizePolicy)
        self.comboBox_MaterialType.setObjectName("comboBox_MaterialType")
        self.gridLayout_5.addWidget(self.comboBox_MaterialType, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(ScenePropertiesWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_Sky = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Sky.setChecked(True)
        self.radioButton_Sky.setObjectName("radioButton_Sky")
        self.gridLayout_2.addWidget(self.radioButton_Sky, 0, 0, 1, 2)
        self.radioButton_Color = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_Color.setMinimumSize(QtCore.QSize(110, 0))
        self.radioButton_Color.setObjectName("radioButton_Color")
        self.gridLayout_2.addWidget(self.radioButton_Color, 2, 0, 1, 1)
        self.colorButton_Color = QgsColorButton(self.groupBox_2)
        self.colorButton_Color.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorButton_Color.sizePolicy().hasHeightForWidth())
        self.colorButton_Color.setSizePolicy(sizePolicy)
        self.colorButton_Color.setObjectName("colorButton_Color")
        self.gridLayout_2.addWidget(self.colorButton_Color, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(ScenePropertiesWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_ProjectCRS = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_ProjectCRS.setChecked(True)
        self.radioButton_ProjectCRS.setObjectName("radioButton_ProjectCRS")
        self.verticalLayout.addWidget(self.radioButton_ProjectCRS)
        self.radioButton_WGS84 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_WGS84.setObjectName("radioButton_WGS84")
        self.verticalLayout.addWidget(self.radioButton_WGS84)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(ScenePropertiesWidget)
        self.radioButton_Color.toggled['bool'].connect(self.colorButton_Color.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(ScenePropertiesWidget)
        ScenePropertiesWidget.setTabOrder(self.lineEdit_BaseSize, self.lineEdit_zFactor)
        ScenePropertiesWidget.setTabOrder(self.lineEdit_zFactor, self.lineEdit_zShift)
        ScenePropertiesWidget.setTabOrder(self.lineEdit_zShift, self.checkBox_autoZShift)
        ScenePropertiesWidget.setTabOrder(self.checkBox_autoZShift, self.radioButton_UseCanvasExtent)
        ScenePropertiesWidget.setTabOrder(self.radioButton_UseCanvasExtent, self.radioButton_FixedExtent)
        ScenePropertiesWidget.setTabOrder(self.radioButton_FixedExtent, self.lineEdit_CenterX)
        ScenePropertiesWidget.setTabOrder(self.lineEdit_CenterX, self.lineEdit_CenterY)
        ScenePropertiesWidget.setTabOrder(self.lineEdit_CenterY, self.lineEdit_Width)
        ScenePropertiesWidget.setTabOrder(self.lineEdit_Width, self.lineEdit_Height)
        ScenePropertiesWidget.setTabOrder(self.lineEdit_Height, self.lineEdit_Rotation)
        ScenePropertiesWidget.setTabOrder(self.lineEdit_Rotation, self.pushButton_SelectExtent)
        ScenePropertiesWidget.setTabOrder(self.pushButton_SelectExtent, self.checkBox_FixAspectRatio)
        ScenePropertiesWidget.setTabOrder(self.checkBox_FixAspectRatio, self.comboBox_MaterialType)
        ScenePropertiesWidget.setTabOrder(self.comboBox_MaterialType, self.checkBox_Outline)
        ScenePropertiesWidget.setTabOrder(self.checkBox_Outline, self.radioButton_Sky)
        ScenePropertiesWidget.setTabOrder(self.radioButton_Sky, self.radioButton_Color)
        ScenePropertiesWidget.setTabOrder(self.radioButton_Color, self.colorButton_Color)
        ScenePropertiesWidget.setTabOrder(self.colorButton_Color, self.radioButton_ProjectCRS)
        ScenePropertiesWidget.setTabOrder(self.radioButton_ProjectCRS, self.radioButton_WGS84)

    def retranslateUi(self, ScenePropertiesWidget):
        _translate = QtCore.QCoreApplication.translate
        ScenePropertiesWidget.setWindowTitle(_translate("ScenePropertiesWidget", "Form"))
        self.groupBox_1.setTitle(_translate("ScenePropertiesWidget", "&World Coordinates"))
        self.label_2.setText(_translate("ScenePropertiesWidget", "Vertical shift"))
        self.label_3.setText(_translate("ScenePropertiesWidget", "Base width"))
        self.checkBox_autoZShift.setToolTip(_translate("ScenePropertiesWidget", "Automatic vertical shift adjustment"))
        self.checkBox_autoZShift.setText(_translate("ScenePropertiesWidget", "Auto"))
        self.label.setText(_translate("ScenePropertiesWidget", "Vertical exaggeration"))
        self.groupBox_4.setTitle(_translate("ScenePropertiesWidget", "Map &Extent"))
        self.checkBox_FixAspectRatio.setText(_translate("ScenePropertiesWidget", "Fix aspect ratio to 1:1"))
        self.radioButton_FixedExtent.setText(_translate("ScenePropertiesWidget", "Fixed extent"))
        self.radioButton_UseCanvasExtent.setText(_translate("ScenePropertiesWidget", "Use map canvas extent"))
        self.label_10.setText(_translate("ScenePropertiesWidget", "Rotation"))
        self.label_7.setText(_translate("ScenePropertiesWidget", "Height"))
        self.label_6.setText(_translate("ScenePropertiesWidget", "Width"))
        self.label_8.setText(_translate("ScenePropertiesWidget", "Center Y"))
        self.label_5.setText(_translate("ScenePropertiesWidget", "Center X"))
        self.pushButton_SelectExtent.setText(_translate("ScenePropertiesWidget", "Select..."))
        self.groupBox.setTitle(_translate("ScenePropertiesWidget", "&Material and Effect"))
        self.label_4.setText(_translate("ScenePropertiesWidget", "Material type"))
        self.checkBox_Outline.setToolTip(_translate("ScenePropertiesWidget", "Check this to enable outline effect"))
        self.checkBox_Outline.setText(_translate("ScenePropertiesWidget", "Enable outline effect"))
        self.groupBox_2.setTitle(_translate("ScenePropertiesWidget", "&Background"))
        self.radioButton_Sky.setText(_translate("ScenePropertiesWidget", "Sky"))
        self.radioButton_Color.setText(_translate("ScenePropertiesWidget", "Solid color"))
        self.groupBox_3.setTitle(_translate("ScenePropertiesWidget", "&Display of Coordinates"))
        self.radioButton_ProjectCRS.setText(_translate("ScenePropertiesWidget", "Coordinates in the project CRS"))
        self.radioButton_WGS84.setText(_translate("ScenePropertiesWidget", "Latitude and longitude (WGS84)"))
from qgis.gui import QgsColorButton
