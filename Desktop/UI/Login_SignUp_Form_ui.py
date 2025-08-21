# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login_SignUp_Form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(905, 725)
        Form.setMinimumSize(QSize(905, 725))
        Form.setMaximumSize(QSize(905, 725))
        Form.setStyleSheet(u"#Form{\n"
"background-color:rgb(37, 36, 34);\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exitButton = QPushButton(Form)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMinimumSize(QSize(121, 41))
        self.exitButton.setMaximumSize(QSize(121, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Display Semib"])
        font.setPointSize(13)
        self.exitButton.setFont(font)
        self.exitButton.setStyleSheet(u"QPushButton{\n"
"background-color: #EB5E28;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 100, 43);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(208, 81, 35);\n"
"}")

        self.horizontalLayout.addWidget(self.exitButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.loginSwitchButton = QPushButton(Form)
        self.loginSwitchButton.setObjectName(u"loginSwitchButton")
        self.loginSwitchButton.setMinimumSize(QSize(121, 41))
        self.loginSwitchButton.setMaximumSize(QSize(121, 41))
        self.loginSwitchButton.setFont(font)
        self.loginSwitchButton.setStyleSheet(u"QPushButton{\n"
"background-color: #EB5E28;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 100, 43);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(208, 81, 35);\n"
"}")

        self.horizontalLayout.addWidget(self.loginSwitchButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.signupSwitchButton = QPushButton(Form)
        self.signupSwitchButton.setObjectName(u"signupSwitchButton")
        self.signupSwitchButton.setMinimumSize(QSize(121, 41))
        self.signupSwitchButton.setMaximumSize(QSize(121, 41))
        self.signupSwitchButton.setFont(font)
        self.signupSwitchButton.setStyleSheet(u"QPushButton{\n"
"background-color: #EB5E28;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 100, 43);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(208, 81, 35);\n"
"}")

        self.horizontalLayout.addWidget(self.signupSwitchButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_3 = QWidget(self.page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(412, 565))
        self.widget_3.setMaximumSize(QSize(412, 565))
        self.widget_3.setStyleSheet(u"background:#403D39;\n"
"border-radius: 20px;")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.frame_7 = QFrame(self.widget_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 200))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(81, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(160, 149))
        self.label_8.setPixmap(QPixmap(u":/img/logo2.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.horizontalSpacer_7 = QSpacerItem(81, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_10 = QFrame(self.widget_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_8 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(276, 191))
        self.label_7.setStyleSheet(u"font: 24pt \"Kdam Thmor Pro\" ;\n"
"color:rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSpacer_9 = QSpacerItem(44, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addWidget(self.frame_10)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.frame_9 = QFrame(self.widget_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(374, 0))
        self.frame_9.setMaximumSize(QSize(374, 50))
        self.frame_9.setStyleSheet(u"  background-color:rgb(198, 191, 180); ")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setSpacing(4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_12 = QPushButton(self.frame_9)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon = QIcon()
        icon.addFile(u":/img/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.pushButton_12)

        self.userNameLoginInput = QLineEdit(self.frame_9)
        self.userNameLoginInput.setObjectName(u"userNameLoginInput")
        font1 = QFont()
        font1.setFamilies([u"Kdam Thmor Pro"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.userNameLoginInput.setFont(font1)
        self.userNameLoginInput.setStyleSheet(u"background-color:rgb(198, 191, 180);\n"
"font: 11pt \"Kdam Thmor Pro\";margin-top:5px")

        self.horizontalLayout_10.addWidget(self.userNameLoginInput)


        self.verticalLayout.addWidget(self.frame_9, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_8 = QFrame(self.widget_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(374, 0))
        self.frame_8.setMaximumSize(QSize(374, 50))
        self.frame_8.setStyleSheet(u"  background-color:rgb(198, 191, 180); ")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_11 = QPushButton(self.frame_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon1 = QIcon()
        icon1.addFile(u":/img/password.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.horizontalLayout_6.addWidget(self.pushButton_11)

        self.passwordLoginInput = QLineEdit(self.frame_8)
        self.passwordLoginInput.setObjectName(u"passwordLoginInput")
        self.passwordLoginInput.setStyleSheet(u"background-color:rgb(198, 191, 180);\n"
"font: 11pt \"Kdam Thmor Pro\";margin-top:5px")
        self.passwordLoginInput.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.passwordLoginInput)

        self.showPassword = QPushButton(self.frame_8)
        self.showPassword.setObjectName(u"showPassword")
        self.showPassword.setStyleSheet(u"QPushButton:pressed{\n"
"icon:url(:/img/output-onlinepngtools (1).png);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/img/output-onlinepngtools.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showPassword.setIcon(icon2)
        self.showPassword.setIconSize(QSize(25, 25))
        self.showPassword.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.showPassword)


        self.verticalLayout.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.rememberMe = QCheckBox(self.widget_3)
        self.rememberMe.setObjectName(u"rememberMe")
        font2 = QFont()
        font2.setFamilies([u"Kdam Thmor Pro 13"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.rememberMe.setFont(font2)
        self.rememberMe.setCursor(QCursor(Qt.PointingHandCursor))
        self.rememberMe.setStyleSheet(u"QCheckBox{\n"
"font: 10pt \"Kdam Thmor Pro\" bold;\n"
"margin-top:5px;\n"
"margin-left:20px;\n"
"color: white;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: gray;\n"
"    border-radius: 10px;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: white white black black;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: qradialgradient(spread:pad, \n"
"                            cx:0.5,\n"
"                            cy:0.5,\n"
"                            radius:0.9,\n"
"                            fx:0.5,\n"
"                            fy:0.5,\n"
"                            stop:0 rgba(0, 255, 0, 255), \n"
"                            stop:1 rgba(0, 64, 0, 255));\n"
"}\n"
"QCheckBox:checked, QCheckBox::indicator:checked {\n"
"    border-color: black black white white;\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.rememberMe)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_11 = QFrame(self.widget_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.loginButton = QPushButton(self.frame_11)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(0, 50))
        self.loginButton.setMaximumSize(QSize(300, 50))
        font3 = QFont()
        font3.setPointSize(13)
        self.loginButton.setFont(font3)
        self.loginButton.setStyleSheet(u"QPushButton{\n"
"background-color: #EB5E28;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 100, 43);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(208, 81, 35);\n"
"}")

        self.horizontalLayout_8.addWidget(self.loginButton)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addWidget(self.frame_11)

        self.horizontalSpacer_17 = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.horizontalSpacer_17)


        self.gridLayout_2.addWidget(self.widget_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_2 = QWidget(self.page_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(341, 527))
        self.widget_2.setMaximumSize(QSize(412, 565))
        self.widget_2.setSizeIncrement(QSize(412, 565))
        self.widget_2.setStyleSheet(u"background:#403D39;\n"
"border-radius: 20px;")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.frame_12 = QFrame(self.widget_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 200))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_12 = QSpacerItem(81, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(160, 149))
        self.label_9.setPixmap(QPixmap(u":/img/logo2.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_9)

        self.horizontalSpacer_13 = QSpacerItem(81, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.verticalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.widget_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)

        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(177, 191))
        font4 = QFont()
        font4.setFamilies([u"Kdam Thmor Pro"])
        font4.setPointSize(24)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"font: 24pt \"Kdam Thmor Pro\" ;\n"
"color:rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_13.addWidget(self.label_6)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"  background-color:rgb(198, 191, 180); ")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.userNameSignUpInput = QLineEdit(self.frame_3)
        self.userNameSignUpInput.setObjectName(u"userNameSignUpInput")
        self.userNameSignUpInput.setStyleSheet(u"background-color:rgb(198, 191, 180);\n"
"font: 11pt \"Kdam Thmor Pro\";\n"
"margin-top:5px;")

        self.horizontalLayout_4.addWidget(self.userNameSignUpInput)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.frame_6 = QFrame(self.widget_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setStyleSheet(u"  background-color:rgb(198, 191, 180); ")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.passwordSignUpInput = QLineEdit(self.frame_6)
        self.passwordSignUpInput.setObjectName(u"passwordSignUpInput")
        self.passwordSignUpInput.setStyleSheet(u"background-color:rgb(198, 191, 180);\n"
"font: 11pt \"Kdam Thmor Pro\";\n"
"margin-top:5px;")
        self.passwordSignUpInput.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.passwordSignUpInput)

        self.showPassword_2 = QPushButton(self.frame_6)
        self.showPassword_2.setObjectName(u"showPassword_2")
        self.showPassword_2.setStyleSheet(u"QPushButton:pressed{\n"
"icon:url(:/img/output-onlinepngtools (1).png);\n"
"}")
        self.showPassword_2.setIcon(icon2)
        self.showPassword_2.setIconSize(QSize(25, 25))
        self.showPassword_2.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.showPassword_2)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"  background-color:rgb(198, 191, 180); ")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_7 = QPushButton(self.frame_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_7)

        self.confirmPasswordSignUpInput = QLineEdit(self.frame_4)
        self.confirmPasswordSignUpInput.setObjectName(u"confirmPasswordSignUpInput")
        self.confirmPasswordSignUpInput.setStyleSheet(u"background-color:rgb(198, 191, 180);\n"
"font: 11pt \"Kdam Thmor Pro\";\n"
"margin-top:5px;")
        self.confirmPasswordSignUpInput.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.confirmPasswordSignUpInput)

        self.showPassword_3 = QPushButton(self.frame_4)
        self.showPassword_3.setObjectName(u"showPassword_3")
        self.showPassword_3.setStyleSheet(u"QPushButton:pressed{\n"
"icon:url(:/img/output-onlinepngtools (1).png);\n"
"}")
        self.showPassword_3.setIcon(icon2)
        self.showPassword_3.setIconSize(QSize(25, 25))
        self.showPassword_3.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.showPassword_3)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)

        self.frame_14 = QFrame(self.widget_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_16 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)

        self.signUpButton = QPushButton(self.frame_14)
        self.signUpButton.setObjectName(u"signUpButton")
        self.signUpButton.setMinimumSize(QSize(0, 50))
        self.signUpButton.setMaximumSize(QSize(300, 50))
        self.signUpButton.setSizeIncrement(QSize(0, 0))
        self.signUpButton.setBaseSize(QSize(0, 0))
        self.signUpButton.setFont(font3)
        self.signUpButton.setStyleSheet(u"QPushButton{\n"
"background-color: #EB5E28;\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 100, 43);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(208, 81, 35);\n"
"}")

        self.horizontalLayout_14.addWidget(self.signUpButton)

        self.horizontalSpacer_18 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)


        self.verticalLayout_4.addWidget(self.frame_14)

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)


        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.retranslateUi(Form)
        self.exitButton.pressed.connect(Form.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.exitButton.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.loginSwitchButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.signupSwitchButton.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.label_8.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Welcome Back", None))
        self.pushButton_12.setText("")
        self.userNameLoginInput.setPlaceholderText(QCoreApplication.translate("Form", u"User Name", None))
        self.pushButton_11.setText("")
        self.passwordLoginInput.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.showPassword.setText("")
        self.rememberMe.setText(QCoreApplication.translate("Form", u"Remember Me", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"LOG IN", None))
#if QT_CONFIG(shortcut)
        self.loginButton.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_9.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Sign Up", None))
        self.pushButton_6.setText("")
        self.userNameSignUpInput.setPlaceholderText(QCoreApplication.translate("Form", u"User Name", None))
        self.pushButton_9.setText("")
        self.passwordSignUpInput.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.showPassword_2.setText("")
        self.pushButton_7.setText("")
        self.confirmPasswordSignUpInput.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.showPassword_3.setText("")
        self.signUpButton.setText(QCoreApplication.translate("Form", u"SIGN UP", None))
#if QT_CONFIG(shortcut)
        self.signUpButton.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

