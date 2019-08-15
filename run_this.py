import time
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTreeWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication, QIcon
from PyQt5.QtCore import QRect, Qt, QTimer, pyqtSignal
import cv2
from Annotate_Console import *
from collections import defaultdict
import json

class MyMainWinow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWinow,self).__init__(parent)
        self.setupUi(self)

        self.OpendefaultPath = './'
        self.SavedefaultPath = './'
        self.FeaturePointList = []
        self.m4_ShowAnnoWinWidth = self.m4_ShowImage.width()  # 打开标注图片窗口的宽度
        self.m4_ShowAnnoWinHeight = self.m4_ShowImage.height()  # 打开标注图片窗口的高度
        self.m4_OpenAnnImage.clicked.connect(self.m4_OpenAnn)  # 创建 打开标注图片信号槽
        self.m4_Complete.clicked.connect(self.m4_CloseAnn)  # 创建 关闭标注图片信号槽
        self.m4_Back.clicked.connect(self.m4_RemoveFeaturePoint)
        self.m4_SetOpenPath.clicked.connect(self.m4_SetOpenDir)
        self.m4_SetSavePath.clicked.connect(self.m4_SetSaveDir)
        self.m4_ShowImage.sendmsg.connect(self.m4_GetFeaturePoint)  # 自定义信号槽连接

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
        # 保存特征点和图像
        if len(self.FeaturePointList) != 0 and len(self.OpenImagePath) != 0:
            # 获取被标注图像的名称
            m4_ImageName = self.OpenImagePath.split('/')
            # 存入字典
            dict_feature_point = defaultdict(list)
            dict_feature_point[m4_ImageName[-1]] = self.FeaturePointList


            with open(self.SavedefaultPath + "/" + m4_ImageName[-1] + '.json', "w") as f:
                json.dump(dict_feature_point, f)

            # dumps 将数据转换成字符串
            # json_str = json.dumps(dict_feature_point)
            # loads: 将字符串转换为字典
            # new_dict = json.loads(json_str)
            reply = QMessageBox.information(self, '提示', 'Label已保存到：' + self.SavedefaultPath + '/'+ m4_ImageName[-1] + '.json'
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

    # 松开鼠标，获取特征点
    def m4_GetFeaturePoint(self, x0, y0):
        x_center, y_center = self.m4_CoordinateConvert(x0, y0, self.m4_ShowAnnoWinWidth,
                                                                   self.m4_ShowAnnoWinHeight,
                                                                   self.image_width,
                                                                   self.image_heigh)
        self.FeaturePointList.append((x_center, y_center))
        frame_show = self.img.copy()
        # 画出特征点
        self.m4_DrawFeaturePoint(self.FeaturePointList ,frame_show)
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
            self.m4_DrawFeaturePoint(self.FeaturePointList ,frame_show)
            self.m4_AnnImageShow(frame_show)
        else:
            self.m4_Back.setEnabled(False)

    # 画出特征点
    def m4_DrawFeaturePoint(self, FeaturePointList, frame_show, lineLength=20):
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
            cv2.line(frame_show, (line1_x1, line1_y1), (line1_x2, line1_y2), (0, 255, 255), 8)
            cv2.line(frame_show, (line2_x1, line2_y1), (line2_x2, line2_y2), (0, 255, 255), 8)
            cv2.putText(frame_show, str(count), fPoint, cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 0), 8)

    def m4_SetOpenDir(self):
        self.OpendefaultPath = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "./")
        self.m4_AnnoDir.setText(self.OpendefaultPath)
    def m4_SetSaveDir(self):
        self.SavedefaultPath = QFileDialog.getExistingDirectory(self, '设置Label保存目录！', './')
        self.m4_LabelDir.setText(self.SavedefaultPath)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWinow()
    myWin.show()
    sys.exit(app.exec())
