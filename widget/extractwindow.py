# -*- coding: utf-8 -*-
import os
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide2.QtCore import QThread, Signal, Slot
from ui.ui_extract import Ui_Form
from thread.extractthread import ExtractThread


class ExtractWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("从PDF提取图片")

        self.ui.pushButton_pdf.clicked.connect(self.select_pdf)
        self.ui.pushButton_output.clicked.connect(self.select_output)
        self.ui.pushButton_ok.clicked.connect(self.ok)

    def enable_widgets(self, flag):
        """启用组件"""
        if flag:
            self.ui.lineEdit_output.setEnabled(True)
            self.ui.lineEdit_pdf.setEnabled(True)
            self.ui.pushButton_pdf.setEnabled(True)
            self.ui.pushButton_output.setEnabled(True)
            self.ui.pushButton_pdf.setEnabled(True)
        else:
            self.ui.lineEdit_output.setEnabled(False)
            self.ui.lineEdit_pdf.setEnabled(False)
            self.ui.pushButton_pdf.setEnabled(False)
            self.ui.pushButton_output.setEnabled(False)
            self.ui.pushButton_pdf.setEnabled(False)

    @Slot()
    def select_pdf(self):
        """选择PDF文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        if selected_dir:
            self.ui.lineEdit_pdf.setText(selected_dir)

    @Slot()
    def select_output(self):
        """选择输出文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        if selected_dir:
            self.ui.lineEdit_output.setText(selected_dir)

    @Slot()
    def ok(self):
        """图片提取"""
        pdf_dir = self.ui.lineEdit_pdf.text().strip()
        output_dir = self.ui.lineEdit_output.text().strip()
        if os.path.isdir(pdf_dir) and os.path.isdir(output_dir):
            self.enable_widgets(False)
            self.combine_pdf_thread = ExtractThread(
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