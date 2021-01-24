# -*- coding: utf-8 -*-
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import Slot

from uis.ui_mainwindow import Ui_MainWindow

from dialogs.errordialog import ErrorDialog

from threads.CombinePDFThread import CombinePDFThread


class MainWindow(QMainWindow):
    """主界面"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.pdf_dir = None
        self.output_dir = None

        self.ui.pushButton_select_pdf_dir.clicked.connect(self.select_pdf_dir)
        self.ui.pushButton_select_output.clicked.connect(self.select_output_dir)
        self.ui.pushButton_combine_pdf.clicked.connect(self.combine_pdf)

        self.ui.lineEdit_select_pdf_dir.setEnabled(False)
        self.ui.lineEdit_select_output.setEnabled(False)


    @Slot()
    def select_pdf_dir(self):
        """选择PDF文件夹"""
        self.pdf_dir = QFileDialog.getExistingDirectory(self)
        self.ui.lineEdit_select_pdf_dir.setText(self.pdf_dir)
    

    @Slot()
    def select_output_dir(self):
        """选择输出文件夹"""
        self.output_dir = QFileDialog.getExistingDirectory(self)
        self.ui.lineEdit_select_output.setText(self.output_dir)


    @Slot()
    def combine_pdf(self):
        """合并pdf"""
        if not self.pdf_dir or not self.output_dir:
            ErrorDialog('出错啦').exec_()
            return
        self.ui.pushButton_select_pdf_dir.setEnabled(False)
        self.ui.pushButton_select_output.setEnabled(False)
        self.ui.pushButton_combine_pdf.setEnabled(False)

        self.combine_pdf_thread = CombinePDFThread(self.pdf_dir, self.output_dir)
        self.combine_pdf_thread.finish_signal.connect(self.combine_pdf_thread_finished)
        self.combine_pdf_thread.start()

    
    @Slot(int)
    def combine_pdf_thread_finished(self, flag):
        if flag == 0:
            ErrorDialog('完成啦').exec_()
        elif flag == -1:
            ErrorDialog('出错啦').exec_()
        self.ui.pushButton_select_pdf_dir.setEnabled(True)
        self.ui.pushButton_select_output.setEnabled(True)
        self.ui.pushButton_combine_pdf.setEnabled(True)
        
    

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())