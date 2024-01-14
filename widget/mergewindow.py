# -*- coding: utf-8 -*-
import os
import glob
import logging
from datetime import datetime
from PyPDF2 import PdfMerger
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal, Slot
from ui.ui_merge import Ui_Form


logger = logging.getLogger("merge")

class MergeWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("合并PDF")

        self.ui.pushButton_pdf.clicked.connect(self.select_pdf)
        self.ui.pushButton_out.clicked.connect(self.select_out)
        self.ui.pushButton_ok.clicked.connect(self.ok)

        self.worker = None

    def enable_widgets(self, flag):
        """启用组件"""
        self.ui.lineEdit_out.setEnabled(flag)
        self.ui.lineEdit_pdf.setEnabled(flag)
        self.ui.pushButton_pdf.setEnabled(flag)
        self.ui.pushButton_out.setEnabled(flag)
        self.ui.pushButton_ok.setEnabled(flag)

    @Slot()
    def select_pdf(self):
        """选择PDF文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        if selected_dir:
            self.ui.lineEdit_pdf.setText(selected_dir)

    @Slot()
    def select_out(self):
        """选择输出文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        if selected_dir:
            self.ui.lineEdit_out.setText(selected_dir)

    @Slot()
    def ok(self):
        """合并pdf"""
        pdf_dir = self.ui.lineEdit_pdf.text()
        out_dir = self.ui.lineEdit_out.text()
        if os.path.isdir(pdf_dir):
            self.process_error('无效的PDF文件夹')
            return
        if os.path.isdir(out_dir):
            self.process_error('无效的输出文件夹')
            return
        
        self.enable_widgets(False)
        self.worker = MergeThread(pdf_dir, out_dir)
        self.worker.info_signal.connect(self.process_info)
        self.worker.error_signal.connect(self.process_error)
        self.worker.start()

    def process_info(self, message):
        QMessageBox.information(
            self,
            "提示",
            message
        )
        self.enable_widgets(True)

    def process_error(self, message):
        QMessageBox.critical(
            self,
            "错误",
            message
        )
        self.enable_widgets(True)


class MergeThread(QThread):
    """合并pdf"""

    info_signal = Signal(str)
    error_signal = Signal(str)

    def __init__(self, pdf_dir, out_dir):
        super().__init__()
        self.pdf_dir = pdf_dir
        self.out_dir = out_dir

    def run(self):
        pdfs = glob.glob(os.path.join(self.pdf_dir, "**/*.pdf"), recursive=True)
        if not pdfs:
            self.error_signal.emit("没有找到PDF文件")
            return
        has_bad = False
        merger = PdfMerger()
        for pdf in pdfs:
            try:
                merger.append(open(pdf, 'rb'))
            except:
                has_bad = True
                logger.critical(f"错误的pdf文件：{pdf}")
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        out_file = os.path.join(self.out_dir, timestamp + '.pdf')
        merger.write(out_file)
        merger.close()

        if has_bad:
            info_message = "合并完成，存在失败的文件，请查阅log.txt"
        else:
            info_message = "合并完成"
        self.info_signal.emit(info_message)
