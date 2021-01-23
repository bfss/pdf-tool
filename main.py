# -*- coding: utf-8 -*-
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Slot
from uis.ui_mainwindow import Ui_MainWindow

from threads.SelectDirThread import SelectDirThread
from threads.CombinePDFThread import CombinePDFThread


class MainWindow(QMainWindow):
    """主界面"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_select_pdf_dir.clicked.connect(self.select_dir)
        self.ui.pushButton_combine_pdf.clicked.connect(self.combine_pdf)


    def select_dir(self):
        """选择文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        self.select_dir_thread = SelectDirThread(selected_dir)
        self.select_dir_thread.finish_signal.connect(self.select_dir_thread_finished)
        self.select_dir_thread.start()


    def combine_pdf(self):
        """合并pdf"""
        self.combine_pdf_thread = CombinePDFThread(self.pdf_list)
        self.combine_pdf_thread.finish_signal.connect(self.combine_pdf_thread_finished)
        self.combine_pdf_thread.start()


    @Slot(int)
    def select_dir_thread_finished(self, flag):
        if flag == 0:
            self.pdf_list = self.select_dir_thread.get_result()
            print(self.pdf_list)

    
    @Slot(int)
    def combine_pdf_thread_finished(self, flag):
        if flag == 0:
            print('完毕')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())