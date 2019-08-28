# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Annotate_Console.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from m4_QLabel import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 1050)
        MainWindow.setMinimumSize(QtCore.QSize(1680, 1050))
        MainWindow.setMaximumSize(QtCore.QSize(1680, 1050))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/YY.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.m4_ShowImage = m4_QLabel(self.centralwidget)
        self.m4_ShowImage.setEnabled(False)
        self.m4_ShowImage.setGeometry(QtCore.QRect(10, 60, 1231, 921))
        self.m4_ShowImage.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.m4_ShowImage.setMouseTracking(True)
        self.m4_ShowImage.setAutoFillBackground(False)
        self.m4_ShowImage.setFrameShape(QtWidgets.QFrame.Box)
        self.m4_ShowImage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.m4_ShowImage.setText("")
        self.m4_ShowImage.setPixmap(QtGui.QPixmap(":/pic/YY.jpg"))
        self.m4_ShowImage.setScaledContents(True)
        self.m4_ShowImage.setObjectName("m4_ShowImage")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.m4_ShowAnnote = QtWidgets.QLabel(self.centralwidget)
        self.m4_ShowAnnote.setGeometry(QtCore.QRect(160, 10, 571, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.m4_ShowAnnote.setFont(font)
        self.m4_ShowAnnote.setFrameShape(QtWidgets.QFrame.Box)
        self.m4_ShowAnnote.setText("")
        self.m4_ShowAnnote.setObjectName("m4_ShowAnnote")
        self.m4_CheckImage = QtWidgets.QLabel(self.centralwidget)
        self.m4_CheckImage.setEnabled(True)
        self.m4_CheckImage.setGeometry(QtCore.QRect(1240, 60, 431, 381))
        self.m4_CheckImage.setFrameShape(QtWidgets.QFrame.Box)
        self.m4_CheckImage.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.m4_CheckImage.setText("")
        self.m4_CheckImage.setPixmap(QtGui.QPixmap(":/pic/YY.jpg"))
        self.m4_CheckImage.setScaledContents(True)
        self.m4_CheckImage.setObjectName("m4_CheckImage")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(750, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.m4_CheckAnnotate = QtWidgets.QLabel(self.centralwidget)
        self.m4_CheckAnnotate.setGeometry(QtCore.QRect(910, 10, 541, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.m4_CheckAnnotate.setFont(font)
        self.m4_CheckAnnotate.setFrameShape(QtWidgets.QFrame.Box)
        self.m4_CheckAnnotate.setText("")
        self.m4_CheckAnnotate.setObjectName("m4_CheckAnnotate")
        self.m4_OpenAnnImage = QtWidgets.QPushButton(self.centralwidget)
        self.m4_OpenAnnImage.setGeometry(QtCore.QRect(1270, 450, 151, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_OpenAnnImage.setFont(font)
        self.m4_OpenAnnImage.setObjectName("m4_OpenAnnImage")
        self.m4_Complete = QtWidgets.QPushButton(self.centralwidget)
        self.m4_Complete.setGeometry(QtCore.QRect(1270, 570, 151, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_Complete.setFont(font)
        self.m4_Complete.setObjectName("m4_Complete")
        self.m4_OpenCheckImage = QtWidgets.QPushButton(self.centralwidget)
        self.m4_OpenCheckImage.setGeometry(QtCore.QRect(1490, 450, 161, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_OpenCheckImage.setFont(font)
        self.m4_OpenCheckImage.setObjectName("m4_OpenCheckImage")
        self.m4_CloseCheckImage = QtWidgets.QPushButton(self.centralwidget)
        self.m4_CloseCheckImage.setEnabled(False)
        self.m4_CloseCheckImage.setGeometry(QtCore.QRect(1490, 510, 161, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_CloseCheckImage.setFont(font)
        self.m4_CloseCheckImage.setObjectName("m4_CloseCheckImage")
        self.m4_Back = QtWidgets.QPushButton(self.centralwidget)
        self.m4_Back.setEnabled(False)
        self.m4_Back.setGeometry(QtCore.QRect(1270, 510, 151, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_Back.setFont(font)
        self.m4_Back.setObjectName("m4_Back")
        self.m4_SetOpenPath = QtWidgets.QPushButton(self.centralwidget)
        self.m4_SetOpenPath.setGeometry(QtCore.QRect(1260, 630, 181, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_SetOpenPath.setFont(font)
        self.m4_SetOpenPath.setObjectName("m4_SetOpenPath")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1250, 620, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.m4_SetSavePath = QtWidgets.QPushButton(self.centralwidget)
        self.m4_SetSavePath.setGeometry(QtCore.QRect(1260, 740, 221, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_SetSavePath.setFont(font)
        self.m4_SetSavePath.setObjectName("m4_SetSavePath")
        self.m4_AnnoDir = QtWidgets.QLabel(self.centralwidget)
        self.m4_AnnoDir.setEnabled(False)
        self.m4_AnnoDir.setGeometry(QtCore.QRect(1260, 690, 411, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.m4_AnnoDir.setFont(font)
        self.m4_AnnoDir.setFrameShape(QtWidgets.QFrame.Box)
        self.m4_AnnoDir.setText("")
        self.m4_AnnoDir.setObjectName("m4_AnnoDir")
        self.m4_LabelDir = QtWidgets.QLabel(self.centralwidget)
        self.m4_LabelDir.setEnabled(False)
        self.m4_LabelDir.setGeometry(QtCore.QRect(1260, 800, 411, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.m4_LabelDir.setFont(font)
        self.m4_LabelDir.setFrameShape(QtWidgets.QFrame.Box)
        self.m4_LabelDir.setText("")
        self.m4_LabelDir.setObjectName("m4_LabelDir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1260, 850, 181, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.m4_LengthP = QtWidgets.QLineEdit(self.centralwidget)
        self.m4_LengthP.setGeometry(QtCore.QRect(1440, 850, 51, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_LengthP.setFont(font)
        self.m4_LengthP.setClearButtonEnabled(False)
        self.m4_LengthP.setObjectName("m4_LengthP")
        self.m4_SizeP = QtWidgets.QLineEdit(self.centralwidget)
        self.m4_SizeP.setGeometry(QtCore.QRect(1440, 890, 51, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_SizeP.setFont(font)
        self.m4_SizeP.setObjectName("m4_SizeP")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1260, 890, 181, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1260, 930, 181, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.m4_Num_Size = QtWidgets.QLineEdit(self.centralwidget)
        self.m4_Num_Size.setGeometry(QtCore.QRect(1440, 930, 51, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.m4_Num_Size.setFont(font)
        self.m4_Num_Size.setObjectName("m4_Num_Size")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1250, 840, 421, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1500, 850, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1500, 890, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1500, 930, 101, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.m4_Classes = QtWidgets.QComboBox(self.centralwidget)
        self.m4_Classes.setGeometry(QtCore.QRect(1490, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.m4_Classes.setFont(font)
        self.m4_Classes.setObjectName("m4_Classes")
        self.m4_Classes.addItem("")
        self.m4_Classes.addItem("")
        self.m4_Classes.addItem("")
        self.m4_Classes.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1450, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1680, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tool_Annotate"))
        self.label_2.setText(_translate("MainWindow", "被标注图片:"))
        self.label_5.setText(_translate("MainWindow", "查看标注结果："))
        self.m4_OpenAnnImage.setText(_translate("MainWindow", "打开需要标注图片"))
        self.m4_Complete.setText(_translate("MainWindow", "完成"))
        self.m4_OpenCheckImage.setText(_translate("MainWindow", "显示标注结果"))
        self.m4_CloseCheckImage.setText(_translate("MainWindow", "关闭标注结果"))
        self.m4_Back.setText(_translate("MainWindow", "撤回标注点"))
        self.m4_SetOpenPath.setText(_translate("MainWindow", "设置默认打开目录："))
        self.m4_SetSavePath.setText(_translate("MainWindow", "设置默认label保存目录："))
        self.label.setText(_translate("MainWindow", "设置标记点线段长度："))
        self.m4_LengthP.setText(_translate("MainWindow", "20"))
        self.m4_SizeP.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "设置标记点线段粗细："))
        self.label_4.setText(_translate("MainWindow", "设置标记点标号大小："))
        self.m4_Num_Size.setText(_translate("MainWindow", "0.4"))
        self.label_6.setText(_translate("MainWindow", "只能是整数"))
        self.label_7.setText(_translate("MainWindow", "只能是整数"))
        self.label_8.setText(_translate("MainWindow", "可以带小数"))
        self.m4_Classes.setItemText(0, _translate("MainWindow", "人脸"))
        self.m4_Classes.setItemText(1, _translate("MainWindow", "四旋翼-无人机"))
        self.m4_Classes.setItemText(2, _translate("MainWindow", "固定翼"))
        self.m4_Classes.setItemText(3, _translate("MainWindow", "降落伞"))
        self.label_9.setText(_translate("MainWindow", "类："))

import apprcc_rc
