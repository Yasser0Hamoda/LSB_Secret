# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(864, 804)
        MainWindow.setStyleSheet(u"\n"
"\n"
"background-color: rgb(37, 36, 34);\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/dark_orange/img/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicat"
                        "or:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, -1, -1, -1)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setMaximumSize(QSize(100, 16777215))
        self.frame_2.setBaseSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"background-color: rgb(64, 61, 57);\n"
"width: 185;\n"
"left: -25px;\n"
"border-radius: 50px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 35, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/img/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(60, 60))
        self.pushButton_5.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Kdam Thmor Pro"])
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"top: 135px;\n"
"left: 43px;\n"
"font-family: Kdam Thmor Pro;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"top: 135px;\n"
"left: 43px;\n"
"font-family: Kdam Thmor Pro;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 151, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(70, 70))
        self.pushButton_2.setMaximumSize(QSize(70, 70))
        self.pushButton_2.setFocusPolicy(Qt.StrongFocus)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color: rgb(91, 87, 81);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{  \n"
"	border-radius:10px;\n"
"	background-color: rgba(235, 94, 40, 1);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/img/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(40, 40))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(70, 70))
        self.pushButton.setMaximumSize(QSize(70, 70))
        self.pushButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color: rgb(91, 87, 81);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{  \n"
"	border-radius:10px;\n"
"	background-color: rgba(235, 94, 40, 1);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/img/encoder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(40, 40))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(70, 70))
        self.pushButton_3.setMaximumSize(QSize(70, 70))
        self.pushButton_3.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color: rgb(91, 87, 81);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{  \n"
"	border-radius:10px;\n"
"	background-color: rgba(235, 94, 40, 1);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/img/decoder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(40, 40))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(70, 70))
        self.pushButton_4.setMaximumSize(QSize(70, 70))
        self.pushButton_4.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	background-color: rgb(91, 87, 81);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked\n"
"{  \n"
"	border-radius:10px;\n"
"	background-color: rgba(235, 94, 40, 1);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/img/saves.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(40, 40))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-image:url(:/img/BG.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-origin: content;\n"
"background-attachment: fixed;\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_6 = QFrame(self.page_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.frame_14.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_14.setLayoutDirection(Qt.LeftToRight)
        self.frame_14.setAutoFillBackground(False)
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_14)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(300, 100))
        self.label_12.setMaximumSize(QSize(500, 500))
        self.label_12.setStyleSheet(u"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 50px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #EB5E28;\n"
"background:transparent;\n"
"")

        self.verticalLayout_7.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_14)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 36px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"background:transparent;\n"
"")

        self.verticalLayout_7.addWidget(self.label_13)

        self.textEdit_2 = QTextEdit(self.frame_14)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"QTextEdit{\n"
"background: rgba(64, 61, 57, 0.7);\n"
"border-radius: 20px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-size: 20px;\n"
"line-height: 100%;\n"
"color: #FFFFFF;\n"
"padding:30px 30px;\n"
"}\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.textEdit_2)

        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(250)
        sizePolicy2.setVerticalStretch(100)
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(100, 100))
        self.label_14.setMaximumSize(QSize(250, 100))
        self.label_14.setStyleSheet(u"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 36px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"background:transparent;")

        self.verticalLayout_7.addWidget(self.label_14)

        self.frame_5 = QFrame(self.frame_14)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(300, 50))
        self.frame_5.setMaximumSize(QSize(1000, 150))
        self.frame_5.setStyleSheet(u"background: rgba(64, 61, 57, 0.7);\n"
"border-radius: 20px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-size: 20px;\n"
"line-height: 100%;\n"
"color: #FFFFFF;\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 3, 0)
        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background:transparent;\n"
"padding:0px 30px;")
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_5)

        self.pushButton_9 = QPushButton(self.frame_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(56, 54, 50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"icon:url(:/img/880eef29f787c838e5be91b50d4f475dd29b0bfc (1).ico);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/img/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QSize(60, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_9)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.label_15 = QLabel(self.frame_14)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 100))
        self.label_15.setMaximumSize(QSize(250, 100))
        self.label_15.setStyleSheet(u"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 36px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"background:transparent;\n"
"")

        self.verticalLayout_7.addWidget(self.label_15)

        self.frame_3 = QFrame(self.frame_14)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(300, 50))
        self.frame_3.setMaximumSize(QSize(1000, 150))
        self.frame_3.setStyleSheet(u"background: rgba(64, 61, 57, 0.7);\n"
"border-radius: 20px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-size: 20px;\n"
"line-height: 100%;\n"
"color: #FFFFFF;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_6 = QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 0))
        self.lineEdit_6.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_6.setStyleSheet(u"background:transparent;\n"
"padding:0px 20px;")
        self.lineEdit_6.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_6)

        self.showPassword_2 = QPushButton(self.frame_3)
        self.showPassword_2.setObjectName(u"showPassword_2")
        self.showPassword_2.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(56, 54, 50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"icon:url(:/img/output-onlinepngtools (1).png);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/img/output-onlinepngtools.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showPassword_2.setIcon(icon6)
        self.showPassword_2.setIconSize(QSize(25, 25))
        self.showPassword_2.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.showPassword_2)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 150))
        self.frame_15.setStyleSheet(u"background:transparent;\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_15)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_10 = QPushButton(self.frame_15)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(150, 50))
        self.pushButton_10.setMaximumSize(QSize(300, 150))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"background: #EB5E28;\n"
"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 30px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 100, 43)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(218, 85, 37);\n"
"}\n"
"")

        self.gridLayout_7.addWidget(self.pushButton_10, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_15)


        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_7 = QFrame(self.page_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(300, 100))
        self.label_5.setMaximumSize(QSize(500, 500))
        self.label_5.setStyleSheet(u"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 50px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #EB5E28;\n"
"background:transparent;\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(100, 100))
        self.label_6.setMaximumSize(QSize(250, 100))
        self.label_6.setStyleSheet(u"font-family: Kdam Thmor Pro;\n"
"background:transparent;\n"
"font-weight: 400;\n"
"font-size: 36px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"")

        self.verticalLayout_3.addWidget(self.label_6)

        self.frame_8 = QFrame(self.frame_10)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(300, 50))
        self.frame_8.setMaximumSize(QSize(1000, 150))
        self.frame_8.setStyleSheet(u"background: rgba(64, 61, 57, 0.7);\n"
"border-radius: 20px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-size: 20px;\n"
"line-height: 100%;\n"
"color: #FFFFFF;\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 3, 0)
        self.lineEdit_7 = QLineEdit(self.frame_8)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background:transparent;\n"
"padding:0px 30px;")
        self.lineEdit_7.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_7)

        self.pushButton_11 = QPushButton(self.frame_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(60, 50))
        self.pushButton_11.setSizeIncrement(QSize(60, 50))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(56, 54, 50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"icon:url(:/img/880eef29f787c838e5be91b50d4f475dd29b0bfc (1).ico);\n"
"}")
        self.pushButton_11.setIcon(icon5)
        self.pushButton_11.setIconSize(QSize(60, 25))

        self.horizontalLayout_5.addWidget(self.pushButton_11)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 100))
        self.label_7.setMaximumSize(QSize(250, 100))
        self.label_7.setStyleSheet(u"font-family: Kdam Thmor Pro;\n"
"background:transparent;\n"
"font-weight: 400;\n"
"font-size: 36px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"")

        self.verticalLayout_3.addWidget(self.label_7)

        self.frame = QFrame(self.frame_10)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 50))
        self.frame.setMaximumSize(QSize(1000, 150))
        self.frame.setStyleSheet(u"background: rgba(64, 61, 57, 0.7);\n"
"border-radius: 20px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-size: 20px;\n"
"line-height: 100%;\n"
"color: #FFFFFF;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setStyleSheet(u"background:transparent;\n"
"padding:0px 20px;")
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.showPassword = QPushButton(self.frame)
        self.showPassword.setObjectName(u"showPassword")
        self.showPassword.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(56, 54, 50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"icon:url(:/img/output-onlinepngtools (1).png);\n"
"}\n"
"")
        self.showPassword.setIcon(icon6)
        self.showPassword.setIconSize(QSize(25, 25))
        self.showPassword.setCheckable(True)

        self.horizontalLayout.addWidget(self.showPassword)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 150))
        self.frame_11.setStyleSheet(u"background:transparent;\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_6 = QPushButton(self.frame_11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(150, 50))
        self.pushButton_6.setMaximumSize(QSize(300, 150))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"background: #EB5E28;\n"
"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 30px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 100, 43)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(218, 85, 37);\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.pushButton_6, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_11)


        self.gridLayout_2.addWidget(self.frame_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_3 = QGridLayout(self.page_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_16 = QFrame(self.page_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_39 = QLabel(self.frame_16)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(300, 100))
        self.label_39.setMaximumSize(QSize(500, 500))
        self.label_39.setStyleSheet(u"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 50px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: #EB5E28;\n"
"background:transparent;\n"
"\n"
"")

        self.verticalLayout_10.addWidget(self.label_39)

        self.frame_12 = QFrame(self.frame_16)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background:transparent;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 16777215))
        self.label_8.setStyleSheet(u"width: 71;\n"
"height: 49;\n"
"top: 315px;\n"
"left: 826px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 32px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: rgba(235, 94, 40, 1);\n"
"")

        self.horizontalLayout_19.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"width: 71;\n"
"height: 49;\n"
"top: 315px;\n"
"left: 826px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 32px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: rgba(235, 94, 40, 1);\n"
"")

        self.horizontalLayout_19.addWidget(self.label_9)


        self.verticalLayout_10.addWidget(self.frame_12)

        self.line_2 = QFrame(self.frame_16)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 1);\n"
"width: 1071.0041450629933;\n"
"top: 360.84px;\n"
"left: 251px;\n"
"angle: 0.15 deg;\n"
"border-width: 1px;\n"
"")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_2)

        self.frame_29 = QFrame(self.frame_16)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"background:transparent;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.scrollArea_2 = QScrollArea(self.frame_29)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(16777215, 700))
        self.scrollArea_2.setStyleSheet(u"QScrollBar:vertical {\n"
"   background:rgb(0, 0, 0);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(235, 94, 40);\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background:transparent;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    border: 1px solid grey;\n"
"  	background:transparent;\n"
"    width: 20px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 669, 382))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_30 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"background:transparent;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_40 = QLabel(self.frame_30)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(270, 0))
        self.label_40.setBaseSize(QSize(270, 0))
        self.label_40.setStyleSheet(u"width: 387;\n"
"height: 49;\n"
"top: 390px;\n"
"left: 333px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 32px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: rgba(255, 255, 255, 0.8);\n"
"")

        self.horizontalLayout_21.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_30)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"width: 160;\n"
"height: 37;\n"
"top: 396px;\n"
"left: 826px;\n"
"font-family: Kdam Thmor Pro;\n"
"font-weight: 400;\n"
"font-size: 24px;\n"
"line-height: 100%;\n"
"letter-spacing: 2px;\n"
"text-align: center;\n"
"color: rgba(255, 255, 255, 0.6);\n"
"")

        self.horizontalLayout_21.addWidget(self.label_41)


        self.verticalLayout_11.addWidget(self.frame_30)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_20.addWidget(self.scrollArea_2)


        self.verticalLayout_10.addWidget(self.frame_29)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_13)


        self.gridLayout_3.addWidget(self.frame_16, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LSB", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SECRET", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Embed message", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"your message", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"upload image", None))
        self.pushButton_9.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.showPassword_2.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Embed", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Extract message", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"upload image", None))
        self.pushButton_11.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.showPassword.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Extract", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Extract message", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"messages", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"your secret message......", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"17/10/2024", None))
    # retranslateUi

