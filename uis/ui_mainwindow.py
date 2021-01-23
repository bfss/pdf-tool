# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit_select_pdf_dir = QLineEdit(self.groupBox)
        self.lineEdit_select_pdf_dir.setObjectName(u"lineEdit_select_pdf_dir")

        self.gridLayout_2.addWidget(self.lineEdit_select_pdf_dir, 0, 0, 1, 1)

        self.pushButton_select_pdf_dir = QPushButton(self.groupBox)
        self.pushButton_select_pdf_dir.setObjectName(u"pushButton_select_pdf_dir")

        self.gridLayout_2.addWidget(self.pushButton_select_pdf_dir, 0, 1, 1, 1)

        self.pushButton_combine_pdf = QPushButton(self.groupBox)
        self.pushButton_combine_pdf.setObjectName(u"pushButton_combine_pdf")

        self.gridLayout_2.addWidget(self.pushButton_combine_pdf, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PDF\u5c0f\u5de5\u5177", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5408\u5e76PDF", None))
        self.pushButton_select_pdf_dir.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9PDF\u6587\u4ef6\u5939", None))
        self.pushButton_combine_pdf.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u6240\u6709PDF", None))
    # retranslateUi

