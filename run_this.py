import time
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTreeWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication, QIcon
from PyQt5.QtCore import QRect, Qt, QTimer, pyqtSignal
import cv2
from Annotate_Console import *
from collections import defaultdict
import json, os

class MyMainWinow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWinow,self).__init__(parent)
        self.setupUi(self)

        self.OpendefaultPath = './'
        self.SavedefaultPath = './'
        self.fpLength = int(self.m4_LengthP.text())
        self.fpSize = int(self.m4_SizeP.text())
        self.NumSize = float(self.m4_Num_Size.text())
        self.FeaturePointList = []
        self.m4_ShowAnnoWinWidth = self.m4_ShowImage.width()  # 打开标注图片窗口的宽度
        self.m4_ShowAnnoWinHeight = self.m4_ShowImage.height()  # 打开标注图片窗口的高度
        self.m4_OpenAnnImage.clicked.connect(self.m4_OpenAnn)  # 创建 打开标注图片信号槽
        self.m4_Complete.clicked.connect(self.m4_CloseAnn)  # 创建 关闭标注图片信号槽
        self.m4_Back.clicked.connect(self.m4_RemoveFeaturePoint)
        self.m4_SetOpenPath.clicked.connect(self.m4_SetOpenDir)
        self.m4_SetSavePath.clicked.connect(self.m4_SetSaveDir)
        self.m4_OpenCheckImage.clicked.connect(self.m4_ShowAnnoResult)
        self.m4_ShowImage.sendmsg.connect(self.m4_GetFeaturePoint)  # 自定义信号槽连接
        self.m4_LengthP.textChanged.connect(self.LengthP_changed)
        self.m4_SizeP.textChanged.connect(self.fpSize_changed)
        self.m4_Num_Size.textChanged.connect(self.NumSize_changed)
        self.m4_CloseCheckImage.clicked.connect(self.m4_CloseShowAnnoResult)
    # 打开标注图片
    def m4_OpenAnn(self):
        # Feature Point点集列表
        self.FeaturePointList = []
        # 打开标注图片对话框
        self.OpenImagePath, _ = QFileDialog.getOpenFileName(self, "打开图片", self.OpendefaultPath)

        if len(self.OpenImagePath) == 0:
            # 打开失败提醒对话框
            reply = QMessageBox.information(self, '提示', '图像打开失败!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            # 显示打开的标注图片的路径
            self.m4_ShowAnnote.setText(self.OpenImagePath)
            self.img = cv2.imread(self.OpenImagePath)
            self.image_width, self.image_heigh = self.img.shape[1], self.img.shape[0]
            self.m4_AnnImageShow(self.img) # 标注窗口显示图片
            self.m4_ShowImage.setEnabled(True) # 使能标注窗口

    # 完成标注， 同时选择是否打开下一张
    def m4_CloseAnn(self):
        if len(self.FeaturePointList) != 12:
            reply = QMessageBox.information(self, '提示', '标注未达到13个点！', QMessageBox.Ok, QMessageBox.Ok)
        else:
            # 保存特征点和图像
            if len(self.FeaturePointList) != 0 and len(self.OpenImagePath) != 0:
                # 获取被标注图像的名称
                m4_ImageName = self.OpenImagePath.split('/')
                # 存入字典
                dict_feature_point = defaultdict(list)
                dict_feature_point[m4_ImageName[-1]] = self.FeaturePointList
                with open(self.SavedefaultPath + '/' + m4_ImageName[-1] + '.json', "w") as f:
                    json.dump(dict_feature_point, f)

                # dumps 将数据转换成字符串
                # json_str = json.dumps(dict_feature_point)
                # loads: 将字符串转换为字典
                # new_dict = json.loads(json_str)
                reply = QMessageBox.information(self, '提示', 'Label已保存到：' + self.SavedefaultPath + '/' + m4_ImageName[-1] + '.json'
                                                , QMessageBox.Ok, QMessageBox.Ok)

            self.m4_Back.setEnabled(False)
            self.FeaturePointList = [] # 清空Feature Point点集列表
            self.m4_ShowImage.setPixmap(QtGui.QPixmap(":/pic/YY.jpg"))

            # 打开下一张？
            reply = QMessageBox.information(self, '提示', '标注完成，是否打开下一张图片？', QMessageBox.Ok | QMessageBox.Close,
                                            QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                reply = QMessageBox.information(self, '提示', '标注完成，同时打开下一张图像！', QMessageBox.Ok, QMessageBox.Ok)
                # 打开下一张图片
                self.m4_OpenAnn()
            else:
                reply = QMessageBox.information(self, '提示', '标注完成!', QMessageBox.Ok, QMessageBox.Ok)

    # 标注图像显示
    def m4_AnnImageShow(self, frame):
        frame = frame.copy()
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        QImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.m4_ShowImage.setPixmap(pixmap)

    # 检查标注图像显示
    def m4_AnnImageResultShow(self, frame):
        frame = frame.copy()
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        QImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.m4_CheckImage.setPixmap(pixmap)


    # 松开鼠标，获取特征点
    def m4_GetFeaturePoint(self, x0, y0):
        if len(self.FeaturePointList) < 12:
            x_center, y_center = self.m4_CoordinateConvert(x0, y0, self.m4_ShowAnnoWinWidth,
                                                                       self.m4_ShowAnnoWinHeight,
                                                                       self.image_width,
                                                                       self.image_heigh)
            self.FeaturePointList.append((x_center, y_center))
        else:
            reply = QMessageBox.information(self, '提示', '标注已达到12个点！', QMessageBox.Ok, QMessageBox.Ok)
        frame_show = self.img.copy()
        # 画出特征点
        self.m4_DrawFeaturePoint(self.FeaturePointList ,frame_show, lineLength=self.fpLength, size=self.fpSize, Num_Size=self.NumSize)
        # 刷新标注特征点图像
        self.m4_AnnImageShow(frame_show)
        if len(self.FeaturePointList) != 0:
            self.m4_Back.setEnabled(True)

    # 窗口坐标转图像坐标
    def m4_CoordinateConvert(self, x0, y0, win_width, win_heigh, image_width, image_heigh):
        '''
        :param x0: 矩形框的左上点x坐标(窗口上的）
        :param y0: 矩形框的左上点y坐标(窗口上的）
        :param win_width: 显示窗口的长度
        :param win_heigh: 显示窗口的宽度
        :param image_width: 图像的宽度
        :param image_heigh: 图像的宽度
        :return: 图像上对应的坐标
        '''
        m4_ratioX = image_width / win_width
        m4_ratioY = image_heigh / win_heigh

        x_tl = x0 * m4_ratioX
        y_tl = y0 * m4_ratioY

        m4_Coordinate = (int(x_tl), int(y_tl))
        return m4_Coordinate

    # 去掉上一个特征点
    def m4_RemoveFeaturePoint(self):
        if len(self.FeaturePointList) != 0:
            self.FeaturePointList.pop()
            frame_show = self.img.copy()
            self.m4_DrawFeaturePoint(self.FeaturePointList ,frame_show, lineLength=self.fpLength, size=self.fpSize, Num_Size=self.NumSize)
            self.m4_AnnImageShow(frame_show)
        else:
            self.m4_Back.setEnabled(False)

    # 画出特征点
    def m4_DrawFeaturePoint(self, FeaturePointList, frame_show, lineLength=20, size=8, Num_Size=2):
        count = 0
        for fPoint in FeaturePointList:
            count += 1
            line1_x1 = fPoint[0] - lineLength
            line1_y1 = fPoint[1] - lineLength
            line1_x2 = fPoint[0] + lineLength
            line1_y2 = fPoint[1] + lineLength

            line2_x1 = fPoint[0] + lineLength
            line2_y1 = fPoint[1] - lineLength
            line2_x2 = fPoint[0] - lineLength
            line2_y2 = fPoint[1] + lineLength
            cv2.line(frame_show, (line1_x1, line1_y1), (line1_x2, line1_y2), (0, 255, 255), size)
            cv2.line(frame_show, (line2_x1, line2_y1), (line2_x2, line2_y2), (0, 255, 255), size)
            cv2.putText(frame_show, str(count), tuple(fPoint), cv2.FONT_HERSHEY_SIMPLEX, Num_Size, (255, 255, 0), size)

    def m4_SetOpenDir(self):
        self.OpendefaultPath = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "./")
        self.m4_AnnoDir.setText(self.OpendefaultPath)
    def m4_SetSaveDir(self):
        self.SavedefaultPath = QFileDialog.getExistingDirectory(self, '设置Label保存目录！', './')
        self.m4_LabelDir.setText(self.SavedefaultPath)

    def m4_ShowAnnoResult(self):
        AnnImagePath, _ = QFileDialog.getOpenFileName(self, "请打开已标注的图片", self.OpendefaultPath)
        imagename = AnnImagePath.split('/')[-1]
        labename = self.SavedefaultPath + '/'+ imagename + '.json'
        if not os.path.exists(labename):
            reply = QMessageBox.information(self, '提示', '请选择已标注的图片, 同时请正确设置Label保存的目录!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.m4_CloseCheckImage.setEnabled(True)
            with open(labename, 'r') as load_f:
                load_dict = json.load(load_f)
            fps = load_dict[imagename]
            img = cv2.imread(AnnImagePath)
            self.m4_DrawFeaturePoint(fps, img, lineLength=self.fpLength, size=self.fpSize, Num_Size=self.NumSize)
            self.m4_AnnImageResultShow(img)

    def m4_CloseShowAnnoResult(self):
        self.m4_CheckImage.setPixmap(QtGui.QPixmap(":/pic/YY.jpg"))
        self.m4_CloseCheckImage.setEnabled(False)

    def LengthP_changed(self):
        self.fpLength = int(self.m4_LengthP.text())

    def fpSize_changed(self):
        self.fpSize = int(self.m4_SizeP.text())

    def NumSize_changed(self):
        self.NumSize = float(self.m4_Num_Size.text())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWinow()
    myWin.show()
    sys.exit(app.exec())
