# -*- coding: utf-8 -*-
import os
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon
from qt_material import apply_stylesheet
from ui.ui_mainwindow import Ui_MainWindow
from widget.mergewindow import MergeWindow


class MainWindow(QMainWindow):
    """主界面"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('y12.ico'))

        self.ui.action_merge.triggered.connect(self.merge)
        self.ui.action_about.triggered.connect(self.about)

    def merge(self):
        MergeWindow(self).open()

    def about(self):
        """关于"""
        QMessageBox.information(
            self,
            "提示",
            "一款合并pdf的小工具\n\n版本：0.0.1"
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)

    apply_stylesheet(app, theme='dark_teal.xml')

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
