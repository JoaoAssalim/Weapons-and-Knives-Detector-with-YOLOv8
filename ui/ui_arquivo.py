# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1130, 785)
        self.Main_QW = QWidget(MainWindow)
        self.Main_QW.setObjectName(u"Main_QW")
        self.gridLayout = QGridLayout(self.Main_QW)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_QF = QFrame(self.Main_QW)
        self.Main_QF.setObjectName(u"Main_QF")
        self.Main_QF.setStyleSheet(u"QFrame#Main_QF{\n"
"	background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(107, 128, 210), stop:1 rgb(180, 140, 255));\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Main_QF)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ContentBox = QFrame(self.Main_QF)
        self.ContentBox.setObjectName(u"ContentBox")
        self.ContentBox.setStyleSheet(u"QFrame#ContentBox{\n"
"	background-color: rgb(245, 249, 254);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.ContentBox.setFrameShape(QFrame.StyledPanel)
        self.ContentBox.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ContentBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
        self.prev_btn = QPushButton(self.ContentBox)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setEnabled(True)
        self.prev_btn.setMinimumSize(QSize(130, 130))
        self.prev_btn.setMaximumSize(QSize(80, 80))
        self.prev_btn.setAutoFillBackground(False)
        self.prev_btn.setStyleSheet(u"QPushButton{\n"
"background-image: url(assets/before.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}")

        self.horizontalLayout.addWidget(self.prev_btn)

        self.video = QLabel(self.ContentBox)
        self.video.setObjectName(u"video")
        self.video.setMinimumSize(QSize(640, 550))
        self.video.setMaximumSize(QSize(640, 550))
        self.video.setStyleSheet(u"QLabel{border-radius: 20px;}")

        self.horizontalLayout.addWidget(self.video)

        self.next_btn = QPushButton(self.ContentBox)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(130, 130))
        self.next_btn.setMaximumSize(QSize(80, 80))
        self.next_btn.setStyleSheet(u"QPushButton{\n"
"background-image: url(assets/next.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}")

        self.horizontalLayout.addWidget(self.next_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.log = QTextEdit(self.ContentBox)
        self.log.setObjectName(u"log")
        self.log.setStyleSheet(u"QTextEdit {\n"
"    border-bottom-left-radius: 30px;\n"
"    border-bottom-right-radius: 30px;\n"
"}")

        self.gridLayout_5.addWidget(self.log, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 2, 0, 1, 1)

        self.top = QFrame(self.ContentBox)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 30))
        self.top.setMaximumSize(QSize(16777215, 30))
        self.top.setStyleSheet(u"QFrame#top{\n"
"background-color: rgba(255, 255, 255,0);\n"
"}")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.top)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, 0, -1, 0)
        self.explain_title = QLabel(self.top)
        self.explain_title.setObjectName(u"explain_title")
        self.explain_title.setMinimumSize(QSize(0, 30))
        self.explain_title.setMaximumSize(QSize(16777215, 30))
        self.explain_title.setStyleSheet(u"font: 700 italic 11pt \"Segoe UI\";")
        self.explain_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.explain_title, 0, 0, 1, 1)

        self.buttons_sf = QFrame(self.top)
        self.buttons_sf.setObjectName(u"buttons_sf")
        self.buttons_sf.setMinimumSize(QSize(120, 30))
        self.buttons_sf.setMaximumSize(QSize(120, 30))
        self.buttons_sf.setFrameShape(QFrame.StyledPanel)
        self.buttons_sf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_sf)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.add_camera = QPushButton(self.buttons_sf)
        self.add_camera.setObjectName(u"add_camera")
        self.add_camera.setMinimumSize(QSize(0, 20))
        self.add_camera.setMaximumSize(QSize(16777215, 20))
        self.add_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_camera.setStyleSheet(u"QPushButton{\n"
"background-image: url(assets/new.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border: none;\n"
"}")

        self.horizontalLayout_2.addWidget(self.add_camera)

        self.min_sf = QPushButton(self.buttons_sf)
        self.min_sf.setObjectName(u"min_sf")
        self.min_sf.setMinimumSize(QSize(14, 14))
        self.min_sf.setMaximumSize(QSize(14, 14))
        self.min_sf.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(4, 180, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(62, 158, 47)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(84, 171, 67);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.min_sf)

        self.max_sf = QPushButton(self.buttons_sf)
        self.max_sf.setObjectName(u"max_sf")
        self.max_sf.setMinimumSize(QSize(14, 14))
        self.max_sf.setMaximumSize(QSize(14, 14))
        self.max_sf.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(227, 199, 0);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(219, 209, 68)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(209, 202, 96);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.max_sf)

        self.close_button = QPushButton(self.buttons_sf)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setMinimumSize(QSize(14, 14))
        self.close_button.setMaximumSize(QSize(14, 14))
        self.close_button.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(240, 108, 96);\n"
"border:1px solid rgba(113, 17, 15,50);\n"
"border-radius:6px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 29, 31)\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(232, 59, 35);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.close_button)


        self.gridLayout_4.addWidget(self.buttons_sf, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.top, 0, 0, 1, 1)

        self.local_info = QLabel(self.ContentBox)
        self.local_info.setObjectName(u"local_info")
        self.local_info.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.local_info, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.ContentBox, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.Main_QF, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.Main_QW)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.prev_btn.setText("")
        self.video.setText("")
        self.next_btn.setText("")
        self.explain_title.setText(QCoreApplication.translate("MainWindow", u"Weapon Detector", None))
        self.add_camera.setText("")
        self.min_sf.setText("")
        self.max_sf.setText("")
        self.close_button.setText("")
        self.local_info.setText("")
    # retranslateUi

