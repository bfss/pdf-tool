# -*- coding: utf-8 -*-
import os
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide2.QtCore import QThread, Signal, Slot
from ui.ui_merge import Ui_Form
from thread.CombinePDFThread import CombinePDFThread


class MergeWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("合并PDF")

        self.ui.pushButton_select_pdf_dir.clicked.connect(self.select_pdf_dir)
        self.ui.pushButton_select_output.clicked.connect(self.select_output_dir)
        self.ui.pushButton_combine_pdf.clicked.connect(self.combine_pdf)

    def enable_widgets(self, flag):
        """启用组件"""
        if flag:
            self.ui.lineEdit_select_output.setEnabled(True)
            self.ui.lineEdit_select_pdf_dir.setEnabled(True)
            self.ui.pushButton_select_pdf_dir.setEnabled(True)
            self.ui.pushButton_select_output.setEnabled(True)
            self.ui.pushButton_combine_pdf.setEnabled(True)
        else:
            self.ui.lineEdit_select_output.setEnabled(False)
            self.ui.lineEdit_select_pdf_dir.setEnabled(False)
            self.ui.pushButton_select_pdf_dir.setEnabled(False)
            self.ui.pushButton_select_output.setEnabled(False)
            self.ui.pushButton_combine_pdf.setEnabled(False)

    @Slot()
    def select_pdf_dir(self):
        """选择PDF文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        if selected_dir:
            self.ui.lineEdit_select_pdf_dir.setText(selected_dir)

    @Slot()
    def select_output_dir(self):
        """选择输出文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        if selected_dir:
            self.ui.lineEdit_select_output.setText(selected_dir)

    @Slot()
    def combine_pdf(self):
        """合并pdf"""
        pdf_dir = self.ui.lineEdit_select_pdf_dir.text().strip()
        output_dir = self.ui.lineEdit_select_output.text().strip()
        if os.path.isdir(pdf_dir) and os.path.isdir(output_dir):
            self.enable_widgets(False)
            self.combine_pdf_thread = CombinePDFThread(
                pdf_dir, output_dir)
            self.combine_pdf_thread.finish_signal.connect(
                self.combine_pdf_thread_finished)
            self.combine_pdf_thread.start()
        else:
            QMessageBox.critical(
                self,
                "错误",
                "需要选择有效的文件夹"
            )

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
        self.enable_widgets(True)