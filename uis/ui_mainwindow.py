# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PDF\u5c0f\u5de5\u5177", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5408\u5e76PDF", None))
        self.pushButton_combine_pdf.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u6240\u6709PDF", None))
        self.pushButton_select_pdf_dir.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9PDF\u6587\u4ef6\u5939", None))
        self.pushButton_select_output.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

