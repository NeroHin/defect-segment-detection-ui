# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defect-detection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1136, 721)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        Form.setFont(font)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1111, 71))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.btnLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.btnLayout.setContentsMargins(0, 0, 0, 0)
        self.btnLayout.setObjectName("btnLayout")
        self.selectFolderBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(20)
        self.selectFolderBtn.setFont(font)
        self.selectFolderBtn.setObjectName("selectFolderBtn")
        self.btnLayout.addWidget(self.selectFolderBtn)
        self.detectDefectsBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(20)
        self.detectDefectsBtn.setFont(font)
        self.detectDefectsBtn.setObjectName("detectDefectsBtn")
        self.btnLayout.addWidget(self.detectDefectsBtn)
        self.segmentBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(20)
        self.segmentBtn.setFont(font)
        self.segmentBtn.setObjectName("segmentBtn")
        self.btnLayout.addWidget(self.segmentBtn)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 150, 1111, 331))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.imgLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.imgLayout.setContentsMargins(0, 0, 0, 0)
        self.imgLayout.setObjectName("imgLayout")
        self.originalImage = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        self.originalImage.setFont(font)
        self.originalImage.setFrameShape(QtWidgets.QFrame.Box)
        self.originalImage.setText("")
        self.originalImage.setAlignment(QtCore.Qt.AlignCenter)
        self.originalImage.setObjectName("originalImage")
        self.imgLayout.addWidget(self.originalImage)
        self.detectImage = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        self.detectImage.setFont(font)
        self.detectImage.setFrameShape(QtWidgets.QFrame.Box)
        self.detectImage.setText("")
        self.detectImage.setAlignment(QtCore.Qt.AlignCenter)
        self.detectImage.setObjectName("detectImage")
        self.imgLayout.addWidget(self.detectImage)
        self.segmentImage = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        self.segmentImage.setFont(font)
        self.segmentImage.setFrameShape(QtWidgets.QFrame.Box)
        self.segmentImage.setText("")
        self.segmentImage.setAlignment(QtCore.Qt.AlignCenter)
        self.segmentImage.setObjectName("segmentImage")
        self.imgLayout.addWidget(self.segmentImage)
        self.originalImageText = QtWidgets.QLabel(Form)
        self.originalImageText.setGeometry(QtCore.QRect(20, 110, 331, 41))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        self.originalImageText.setFont(font)
        self.originalImageText.setAlignment(QtCore.Qt.AlignCenter)
        self.originalImageText.setObjectName("originalImageText")
        self.detectImageText_ = QtWidgets.QLabel(Form)
        self.detectImageText_.setGeometry(QtCore.QRect(400, 110, 331, 41))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        self.detectImageText_.setFont(font)
        self.detectImageText_.setAlignment(QtCore.Qt.AlignCenter)
        self.detectImageText_.setObjectName("detectImageText_")
        self.segmentImageText = QtWidgets.QLabel(Form)
        self.segmentImageText.setGeometry(QtCore.QRect(780, 110, 331, 41))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        self.segmentImageText.setFont(font)
        self.segmentImageText.setAlignment(QtCore.Qt.AlignCenter)
        self.segmentImageText.setObjectName("segmentImageText")
        self.diceCoefficientText = QtWidgets.QLabel(Form)
        self.diceCoefficientText.setGeometry(QtCore.QRect(760, 490, 161, 41))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.diceCoefficientText.setFont(font)
        self.diceCoefficientText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.diceCoefficientText.setObjectName("diceCoefficientText")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(390, 490, 60, 141))
        self.widget.setObjectName("widget")
        self.detectMetricLayout = QtWidgets.QVBoxLayout(self.widget)
        self.detectMetricLayout.setContentsMargins(0, 0, 0, 0)
        self.detectMetricLayout.setObjectName("detectMetricLayout")
        self.fpsText = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.fpsText.setFont(font)
        self.fpsText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.fpsText.setObjectName("fpsText")
        self.detectMetricLayout.addWidget(self.fpsText)
        self.predictText = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.predictText.setFont(font)
        self.predictText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.predictText.setObjectName("predictText")
        self.detectMetricLayout.addWidget(self.predictText)
        self.iouText = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.iouText.setFont(font)
        self.iouText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.iouText.setObjectName("iouText")
        self.detectMetricLayout.addWidget(self.iouText)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 490, 160, 211))
        self.widget1.setObjectName("widget1")
        self.imgInfoLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.imgInfoLayout.setContentsMargins(0, 0, 0, 0)
        self.imgInfoLayout.setObjectName("imgInfoLayout")
        self.currentImageNumber = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.currentImageNumber.setFont(font)
        self.currentImageNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.currentImageNumber.setObjectName("currentImageNumber")
        self.imgInfoLayout.addWidget(self.currentImageNumber)
        self.typeText = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.typeText.setFont(font)
        self.typeText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.typeText.setObjectName("typeText")
        self.imgInfoLayout.addWidget(self.typeText)
        self.uncoverAP = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.uncoverAP.setFont(font)
        self.uncoverAP.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.uncoverAP.setObjectName("uncoverAP")
        self.imgInfoLayout.addWidget(self.uncoverAP)
        self.unevenAP = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.unevenAP.setFont(font)
        self.unevenAP.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.unevenAP.setObjectName("unevenAP")
        self.imgInfoLayout.addWidget(self.unevenAP)
        self.scratchAP = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(18)
        font.setUnderline(True)
        self.scratchAP.setFont(font)
        self.scratchAP.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scratchAP.setObjectName("scratchAP")
        self.imgInfoLayout.addWidget(self.scratchAP)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.selectFolderBtn.setText(_translate("Form", "Select Image Folder"))
        self.detectDefectsBtn.setText(_translate("Form", "Detect Defects"))
        self.segmentBtn.setText(_translate("Form", "Segment"))
        self.originalImageText.setText(_translate("Form", "Original Image"))
        self.detectImageText_.setText(_translate("Form", "Detect Image"))
        self.segmentImageText.setText(_translate("Form", "Segment Image"))
        self.diceCoefficientText.setText(_translate("Form", "Dice Coefficient"))
        self.fpsText.setText(_translate("Form", "FPS"))
        self.predictText.setText(_translate("Form", "Predict"))
        self.iouText.setText(_translate("Form", "IoU"))
        self.currentImageNumber.setText(_translate("Form", "CurrentImage:"))
        self.typeText.setText(_translate("Form", "Type(Ground Truth)"))
        self.uncoverAP.setText(_translate("Form", "AP50(uncover):"))
        self.unevenAP.setText(_translate("Form", "AP50(uneven):"))
        self.scratchAP.setText(_translate("Form", "AP50(Scratch):"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
