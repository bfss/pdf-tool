# -*- coding: utf-8 -*-
import os
import glob
import logging
from datetime import datetime
from pypdf import PdfReader
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal, Slot
from ui.ui_extract import Ui_Form


logger = logging.getLogger("merge")

class ExtractWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("从PDF提取图片")

        self.ui.pushButton_pdf.clicked.connect(self.select_pdf)
        self.ui.pushButton_out.clicked.connect(self.select_out)
        self.ui.pushButton_ok.clicked.connect(self.ok)

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
        """图片提取"""
        pdf_dir = self.ui.lineEdit_pdf.text()
        out_dir = self.ui.lineEdit_out.text()
        if not os.path.isdir(pdf_dir):
            self.process_error('无效的PDF文件夹')
            return
        if not os.path.isdir(out_dir):
            self.process_error('无效的输出文件夹')
            return
        self.enable_widgets(False)
        self.worker = ExtractThread(pdf_dir, out_dir)
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


class ExtractThread(QThread):
    """从pdf提取图片"""

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
        for pdf in pdfs:
            try:
                reader = PdfReader(pdf)
                pages = reader.pages
                count = 0
                for page in pages:
                    for image in page.images:
                        pdfname = os.path.basename(pdf).split(".")[0]
                        dirname = os.path.join(self.out_dir, pdfname)
                        os.makedirs(dirname, exist_ok=True)
                        outfile = os.path.join(dirname, str(count)+".jpg")
                        with open(outfile, "wb") as f:
                            f.write(image.data)
                        count += 1
            except:
                has_bad = True
                logger.critical(f"错误的pdf文件：{pdf}")

        if has_bad:
            info_message = "提取完成，存在失败的文件，请查阅log.txt"
        else:
            info_message = "提取完成"
        self.info_signal.emit(info_message)
