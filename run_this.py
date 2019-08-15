import time
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTreeWidgetItem, QFileDialog
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, QGuiApplication, QIcon
from PyQt5.QtCore import QRect, Qt, QTimer, pyqtSignal
import cv2
from Annotate_Console import *
class MyMainWinow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWinow,self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWinow()
    myWin.show()
    sys.exit(app.exec())
