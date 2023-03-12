# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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
        self.lineEdit_select_pdf_dir = QLineEdit(self.groupBox)
        self.lineEdit_select_pdf_dir.setObjectName(u"lineEdit_select_pdf_dir")

        self.gridLayout_2.addWidget(self.lineEdit_select_pdf_dir, 0, 0, 1, 1)

        self.pushButton_combine_pdf = QPushButton(self.groupBox)
        self.pushButton_combine_pdf.setObjectName(u"pushButton_combine_pdf")

        self.gridLayout_2.addWidget(self.pushButton_combine_pdf, 2, 0, 1, 2)

        self.pushButton_select_pdf_dir = QPushButton(self.groupBox)
        self.pushButton_select_pdf_dir.setObjectName(u"pushButton_select_pdf_dir")

        self.gridLayout_2.addWidget(self.pushButton_select_pdf_dir, 0, 1, 1, 1)

        self.pushButton_select_output = QPushButton(self.groupBox)
        self.pushButton_select_output.setObjectName(u"pushButton_select_output")

        self.gridLayout_2.addWidget(self.pushButton_select_output, 1, 1, 1, 1)

        self.lineEdit_select_output = QLineEdit(self.groupBox)
        self.lineEdit_select_output.setObjectName(u"lineEdit_select_output")

        self.gridLayout_2.addWidget(self.lineEdit_select_output, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5408\u5e76PDF", None))
        self.pushButton_combine_pdf.setText(QCoreApplication.translate("Form", u"\u5408\u5e76\u6240\u6709PDF", None))
        self.pushButton_select_pdf_dir.setText(QCoreApplication.translate("Form", u"\u9009\u62e9PDF\u6587\u4ef6\u5939", None))
        self.pushButton_select_output.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6\u5939", None))
    # retranslateUi

