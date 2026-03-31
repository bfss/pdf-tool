# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extract.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(653, 479)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_pdf = QLineEdit(self.frame)
        self.lineEdit_pdf.setObjectName(u"lineEdit_pdf")

        self.gridLayout_2.addWidget(self.lineEdit_pdf, 0, 1, 1, 1)

        self.pushButton_pdf = QPushButton(self.frame)
        self.pushButton_pdf.setObjectName(u"pushButton_pdf")

        self.gridLayout_2.addWidget(self.pushButton_pdf, 0, 2, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)

        self.lineEdit_out = QLineEdit(self.frame)
        self.lineEdit_out.setObjectName(u"lineEdit_out")

        self.gridLayout_2.addWidget(self.lineEdit_out, 0, 4, 1, 1)

        self.pushButton_out = QPushButton(self.frame)
        self.pushButton_out.setObjectName(u"pushButton_out")

        self.gridLayout_2.addWidget(self.pushButton_out, 0, 5, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.pushButton_ok = QPushButton(Form)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.gridLayout_3.addWidget(self.pushButton_ok, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"PDF\u6587\u4ef6\u5939\uff1a", None))
        self.pushButton_pdf.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u6587\u4ef6\u5939\uff1a", None))
        self.pushButton_out.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5217\u8868", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u63d0\u53d6", None))
    # retranslateUi

