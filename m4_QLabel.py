# imports
# import PyQt5.QtCore as __PyQt5_QtCore
# import PyQt5.QtGui as __PyQt5_QtGui
# from PyQt5 import QtWidgets


from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QRect, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen
class m4_QLabel(QLabel):
    """
    QLabel(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QLabel(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """

    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    sendmsg = pyqtSignal(float, float, float, float)
    # 鼠标点击事件
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

    # 鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.flag = False
        if self.x0 > self.x1:
            a_t = self.x0
            self.x0 = self.x1
            self.x1 = a_t
        if self.y0 > self.y1:
            b_t = self.y0
            self.y0 = self.y1
            self.y1 = b_t

        self.sendmsg.emit(self.x0, self.y0, self.x1, self.y1)
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0



    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        # if self.flag:
        self.x1 = event.x()
        self.y1 = event.y()
        if self.x1> self.width():
            self.x1 = self.width()
        elif self.x1 < 0:
            self.x1 = 0
        if self.y1> self.height():
            self.y1 = self.height()
        elif self.y1 < 0:
            self.y1 = 0
        self.update()

    # 绘制事件
    def paintEvent(self, event):
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, self.x1 - self.x0, self.y1 - self.y0)
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        painter.drawRect(rect)
        painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
        painter.drawLine(0, self.y1, self.width(), self.y1)
        painter.drawLine(self.x1, 0, self.x1, self.height())
