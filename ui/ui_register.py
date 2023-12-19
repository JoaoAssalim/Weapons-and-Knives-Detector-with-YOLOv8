# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_Register(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(412, 259)
        self.Main_QW = QWidget(MainWindow)
        self.Main_QW.setObjectName(u"Main_QW")
        self.gridLayout = QGridLayout(self.Main_QW)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Main_QF = QFrame(self.Main_QW)
        self.Main_QF.setObjectName(u"Main_QF")
        self.Main_QF.setStyleSheet(u"QFrame#Main_QF{\n"
"	background-color: rgb(159, 246, 252);\n"
"border:0px solid red;\n"
"border-radius:30px\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Main_QF)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.CameraIP = QFrame(self.Main_QF)
        self.CameraIP.setObjectName(u"CameraIP")
        self.CameraIP.setStyleSheet(u"QLineEdit{margin-left: 20px; margin-right: 20px;}")
        self.CameraIP.setFrameShape(QFrame.StyledPanel)
        self.CameraIP.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.CameraIP)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.camera_ip = QLineEdit(self.CameraIP)
        self.camera_ip.setObjectName(u"camera_ip")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_ip.sizePolicy().hasHeightForWidth())
        self.camera_ip.setSizePolicy(sizePolicy)
        self.camera_ip.setMinimumSize(QSize(400, 18))
        self.camera_ip.setMaximumSize(QSize(400, 18))
        self.camera_ip.setStyleSheet(u"QLineEdit{margin-left: 20px; margin-right: 20px; border: 1px solid rgb(0, 0, 0);}")

        self.gridLayout_3.addWidget(self.camera_ip, 4, 1, 1, 1, Qt.AlignHCenter)

        self.label = QLabel(self.CameraIP)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))
        self.label.setStyleSheet(u"QLabel{\n"
"font: 700 italic 11pt \"Segoe UI\";\n"
"margin-left: 10px;}")

        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)

        self.local_name = QLineEdit(self.CameraIP)
        self.local_name.setObjectName(u"local_name")
        self.local_name.setMinimumSize(QSize(400, 18))
        self.local_name.setMaximumSize(QSize(400, 18))
        self.local_name.setStyleSheet(u"QLineEdit{margin-left: 20px; margin-right: 20px; border: 1px solid rgb(0, 0, 0);}")

        self.gridLayout_3.addWidget(self.local_name, 2, 1, 1, 1, Qt.AlignHCenter)

        self.top = QFrame(self.CameraIP)
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


        self.gridLayout_3.addWidget(self.top, 0, 1, 1, 1)

        self.register_2 = QPushButton(self.CameraIP)
        self.register_2.setObjectName(u"register_2")
        self.register_2.setMinimumSize(QSize(400, 40))
        self.register_2.setMaximumSize(QSize(16777215, 16777215))
        self.register_2.setLayoutDirection(Qt.LeftToRight)
        self.register_2.setStyleSheet(u"QPushButton{\n"
"	margin-top: 10px;\n"
"	margin-left: 20px;\n"
"	margin-right: 20px;\n"
"	margin-bottom: 5px;\n"
"	background-color: rgb(13, 63, 112);\n"
"	border-radius:6px;\n"
"	color: rgb(255,255,255);\n"
"	font-size: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(45, 180, 204)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(21, 140, 1617);\n"
"}")

        self.gridLayout_3.addWidget(self.register_2, 6, 1, 1, 1)

        self.label_2 = QLabel(self.CameraIP)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))
        self.label_2.setStyleSheet(u"QLabel{\n"
"font: 700 italic 11pt \"Segoe UI\";\n"
"margin-left: 10px;}")

        self.gridLayout_3.addWidget(self.label_2, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.CameraIP, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.Main_QF, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.Main_QW)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Local Name", None))
        self.explain_title.setText(QCoreApplication.translate("MainWindow", u"Register New Camera", None))
        self.min_sf.setText("")
        self.max_sf.setText("")
        self.close_button.setText("")
        self.register_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Camera IP", None))
    # retranslateUi

