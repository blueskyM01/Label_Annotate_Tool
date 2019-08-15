import time
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTreeWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication, QIcon
from PyQt5.QtCore import QRect, Qt, QTimer, pyqtSignal
import cv2
from Annotate_Console import *
class MyMainWinow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWinow,self).__init__(parent)
        self.setupUi(self)

        self.FeaturePointList = []
        self.m4_ShowAnnoWinWidth = self.m4_ShowImage.width()  # 打开标注图片窗口的宽度
        self.m4_ShowAnnoWinHeight = self.m4_ShowImage.height()  # 打开标注图片窗口的高度
        self.m4_OpenAnnImage.clicked.connect(self.m4_OpenAnn)  # 创建 打开标注图片信号槽
        self.m4_Complete.clicked.connect(self.m4_CloseAnn)  # 创建 关闭标注图片信号槽

        self.m4_ShowImage.sendmsg.connect(self.m4_GetFeaturePoint)  # 自定义信号槽连接

    def m4_OpenAnn(self):
        self.FeaturePointList = []
        OpenImagePath, _ = QFileDialog.getOpenFileName(self, "打开图片", "./")
        if len(OpenImagePath) == 0:
            reply = QMessageBox.information(self, '提示', '图像打开失败!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.m4_ShowAnnote.setText(OpenImagePath)
            self.img = cv2.imread(OpenImagePath)
            self.image_width, self.image_heigh = self.img.shape[1], self.img.shape[0]
            self.m4_AnnImageShow(self.img)
            self.m4_ShowImage.setEnabled(True)

    def m4_CloseAnn(self):
        self.FeaturePointList = []
        self.m4_ShowImage.setPixmap(QtGui.QPixmap(":/pic/YY.jpg"))
        reply = QMessageBox.information(self, '提示', '标注完成，是否打开下一张图片？', QMessageBox.Ok | QMessageBox.Close,
                                        QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            # 打开下一张图片
            self.m4_OpenAnn()
        else:
            reply = QMessageBox.information(self, '提示', '标注完成!', QMessageBox.Ok, QMessageBox.Ok)
            self.m4_ShowImage.setEnabled(False)


    # 标注图像显示
    def m4_AnnImageShow(self, frame):
        frame = frame.copy()
        height, width, bytesPerComponent = frame.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        QImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        self.m4_ShowImage.setPixmap(pixmap)

    def m4_GetFeaturePoint(self, x0, y0):
        x_center, y_center = self.m4_CoordinateConvert(x0, y0, self.m4_ShowAnnoWinWidth,
                                                                   self.m4_ShowAnnoWinHeight,
                                                                   self.image_width,
                                                                   self.image_heigh)
        self.FeaturePointList.append((x_center, y_center))
        for fPoint in self.FeaturePointList:
            frame_show = self.img
            line1_x1 = fPoint[0] - 30
            line1_y1 = fPoint[1] - 30
            line1_x2 = fPoint[0] + 30
            line1_y2 = fPoint[1] + 30

            line2_x1 = fPoint[0] + 30
            line2_y1 = fPoint[1] - 30
            line2_x2 = fPoint[0] - 30
            line2_y2 = fPoint[1] + 30

            cv2.line(frame_show, (line1_x1, line1_y1), (line1_x2, line1_y2), (0, 0, 255), 8)
            cv2.line(frame_show, (line2_x1, line2_y1), (line2_x2, line2_y2), (0, 0, 255), 8)

            # cv2.circle(frame_show, fPoint, 50, (0, 255, 0), -1)
        self.m4_AnnImageShow(self.img)
        print(x_center, y_center)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWinow()
    myWin.show()
    sys.exit(app.exec())
