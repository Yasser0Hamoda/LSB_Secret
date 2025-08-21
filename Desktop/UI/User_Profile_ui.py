# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_Profile.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(698, 552)
        Form.setMinimumSize(QSize(698, 552))
        Form.setMaximumSize(QSize(698, 552))
        Form.setStyleSheet(u"#Form{\n"
"background-color:#403D39;\n"
"border-radius:30px;\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 281, 261))
        self.label.setMinimumSize(QSize(231, 191))
        self.label.setMaximumSize(QSize(12345678, 12345678))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Text Semibold"])
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"#label{\n"
"color:white;\n"
"background-color:rgb(97, 92, 86);\n"
"border-radius:35px;\n"
"}")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.loginSwitchButton = QPushButton(Form)
        self.loginSwitchButton.setObjectName(u"loginSwitchButton")
        self.loginSwitchButton.setGeometry(QRect(500, 470, 166, 41))
        self.loginSwitchButton.setMinimumSize(QSize(166, 41))
        self.loginSwitchButton.setMaximumSize(QSize(166, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable Display Semib"])
        font1.setPointSize(13)
        self.loginSwitchButton.setFont(font1)
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
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(350, 60, 321, 377))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(16)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Display Semib"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:white;")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(307, 41))
        self.lineEdit.setMaximumSize(QSize(307, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Text Semibold"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(97, 92, 86);\n"
"border:1px solid rgb(97, 92, 86);\n"
"border-radius:15px;\n"
"color:white;\n"
"padding:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(108, 102, 96);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(108, 102, 96);\n"
"border-color:rgb(235, 94, 40);\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color:white;")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(307, 41))
        self.lineEdit_2.setMaximumSize(QSize(307, 41))
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(97, 92, 86);\n"
"border:1px solid rgb(97, 92, 86);\n"
"border-radius:15px;\n"
"color:white;\n"
"padding:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(108, 102, 96);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(108, 102, 96);\n"
"border-color:rgb(235, 94, 40);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:white;")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(307, 41))
        self.lineEdit_4.setMaximumSize(QSize(307, 41))
        self.lineEdit_4.setFont(font3)
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(97, 92, 86);\n"
"border:1px solid rgb(97, 92, 86);\n"
"border-radius:15px;\n"
"color:white;\n"
"padding:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(108, 102, 96);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(108, 102, 96);\n"
"border-color:rgb(235, 94, 40);\n"
"}")

        self.verticalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color:white;")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(307, 41))
        self.lineEdit_3.setMaximumSize(QSize(307, 41))
        self.lineEdit_3.setFont(font3)
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(97, 92, 86);\n"
"border:1px solid rgb(97, 92, 86);\n"
"border-radius:15px;\n"
"color:white;\n"
"padding:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background-color:rgb(108, 102, 96);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"background-color:rgb(108, 102, 96);\n"
"border-color:rgb(235, 94, 40);\n"
"}")

        self.verticalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"No Image", None))
        self.loginSwitchButton.setText(QCoreApplication.translate("Form", u"Update", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"User Name", None))
        self.lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"E-mail", None))
        self.lineEdit_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Password", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Gender", None))
    # retranslateUi

