# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(572, 401)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_pdf = QLineEdit(self.groupBox)
        self.lineEdit_pdf.setObjectName(u"lineEdit_pdf")

        self.gridLayout_2.addWidget(self.lineEdit_pdf, 0, 1, 1, 1)

        self.pushButton_pdf = QPushButton(self.groupBox)
        self.pushButton_pdf.setObjectName(u"pushButton_pdf")

        self.gridLayout_2.addWidget(self.pushButton_pdf, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_out = QLineEdit(self.groupBox)
        self.lineEdit_out.setObjectName(u"lineEdit_out")

        self.gridLayout_2.addWidget(self.lineEdit_out, 1, 1, 1, 1)

        self.pushButton_out = QPushButton(self.groupBox)
        self.pushButton_out.setObjectName(u"pushButton_out")

        self.gridLayout_2.addWidget(self.pushButton_out, 1, 2, 1, 1)

        self.pushButton_ok = QPushButton(self.groupBox)
        self.pushButton_ok.setObjectName(u"pushButton_ok")

        self.gridLayout_2.addWidget(self.pushButton_ok, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5408\u5e76PDF", None))
        self.label.setText(QCoreApplication.translate("Form", u"PDF\u6587\u4ef6\u5939\uff1a", None))
        self.pushButton_pdf.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u6587\u4ef6\u5939\uff1a", None))
        self.pushButton_out.setText(QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5408\u5e76", None))
    # retranslateUi

