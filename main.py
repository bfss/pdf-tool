# -*- coding: utf-8 -*-
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon

from qt_material import apply_stylesheet

from ui.ui_mainwindow import Ui_MainWindow

from thread.CombinePDFThread import CombinePDFThread


class MainWindow(QMainWindow):
    """主界面"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('y12.ico'))

        self.pdf_dir = None
        self.output_dir = None

        self.ui.pushButton_select_pdf_dir.clicked.connect(self.select_pdf_dir)
        self.ui.pushButton_select_output.clicked.connect(
            self.select_output_dir)
        self.ui.pushButton_combine_pdf.clicked.connect(self.combine_pdf)

        self.ui.action_about.triggered.connect(self.about)

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
            QMessageBox.critical(
                self,
                "错误",
                "出错啦"
            )
            return
        self.ui.pushButton_select_pdf_dir.setEnabled(False)
        self.ui.pushButton_select_output.setEnabled(False)
        self.ui.pushButton_combine_pdf.setEnabled(False)

        self.combine_pdf_thread = CombinePDFThread(
            self.pdf_dir, self.output_dir)
        self.combine_pdf_thread.finish_signal.connect(
            self.combine_pdf_thread_finished)
        self.combine_pdf_thread.start()

    @Slot(int)
    def combine_pdf_thread_finished(self, flag):
        if flag == 0:
            QMessageBox.information(
                self,
                "提示",
                "完成啦"
            )
        elif flag == -1:
            QMessageBox.critical(
                self,
                "错误",
                "文件夹应包含至少一个有效的PDF文件"
            )
        elif flag == -2:
            bad_pdfs = self.combine_pdf_thread.get_bad_pdfs()
            bad_pdfs_str = '\n'.join(bad_pdfs)
            QMessageBox.critical(
                self,
                "错误",
                "合并完毕，下列这些PDF存在问题，没有被合并：\n" + bad_pdfs_str
            )
        self.ui.pushButton_select_pdf_dir.setEnabled(True)
        self.ui.pushButton_select_output.setEnabled(True)
        self.ui.pushButton_combine_pdf.setEnabled(True)

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
