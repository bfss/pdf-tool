# -*- coding: utf-8 -*-
import os
import sys
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTranslator, QLocale, QLibraryInfo
from ui.ui_mainwindow import Ui_MainWindow
from widget.mergewindow import MergeWindow
from widget.extractwindow import ExtractWindow


class MainWindow(QMainWindow):
    """主界面"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('y12.ico'))

        self.ui.action_merge.triggered.connect(self.merge)
        self.ui.action_extract.triggered.connect(self.extract)
        self.ui.action_about.triggered.connect(self.about)

    def merge(self):
        MergeWindow(self).open()

    def extract(self):
        ExtractWindow(self).open()
    
    def about(self):
        """关于"""
        QMessageBox.information(
            self,
            "提示",
            "一款PDF小工具\n\n版本：0.1.0"
        )


if __name__ == '__main__':
    logging.basicConfig(
        filename="log.txt",
        filemode="w",
    )

    app = QApplication(sys.argv)
    translator = QTranslator()
    translations = os.path.join(os.getcwd(), 'PySide6/translations')
    if translator.load('qt_ZH_CN', translations):
        app.installTranslator(translator)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
