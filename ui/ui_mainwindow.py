# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 578)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_merge = QAction(MainWindow)
        self.action_merge.setObjectName(u"action_merge")
        self.action_extract = QAction(MainWindow)
        self.action_extract.setObjectName(u"action_extract")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 787, 22))
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_merge = QMenu(self.menubar)
        self.menu_merge.setObjectName(u"menu_merge")
        self.menu_convert = QMenu(self.menubar)
        self.menu_convert.setObjectName(u"menu_convert")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_merge.menuAction())
        self.menubar.addAction(self.menu_convert.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_help.addAction(self.action_about)
        self.menu_merge.addAction(self.action_merge)
        self.menu_convert.addAction(self.action_extract)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PDF\u5c0f\u5de5\u5177", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_merge.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76PDF", None))
        self.action_extract.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u56fe\u7247", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_merge.setTitle(QCoreApplication.translate("MainWindow", u"\u5408\u5e76PDF", None))
        self.menu_convert.setTitle(QCoreApplication.translate("MainWindow", u"PDF\u56fe\u7247\u5de5\u5177", None))
    # retranslateUi

