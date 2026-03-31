# -*- coding: utf-8 -*-
import os
import glob
import logging
from datetime import datetime
from pypdf import PdfReader
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import QThread, Signal, Slot
from ui.ui_extract import Ui_Form


logger = logging.getLogger("提取图片")

class ExtractWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("提取PDF图片")

        self.ui.pushButton_pdf.clicked.connect(self.select_pdf)
        self.ui.pushButton_out.clicked.connect(self.select_out)
        self.ui.pushButton_ok.clicked.connect(self.ok)

        self.pdfs = []

    @Slot()
    def select_pdf(self):
        """选择PDF文件夹"""
        pdf_dir = QFileDialog.getExistingDirectory(self)
        if pdf_dir:
            self.ui.lineEdit_pdf.setText(pdf_dir)
            self.pdfs = glob.glob(os.path.join(pdf_dir, "*.pdf"))
            self.ui.listWidget.addItems(self.pdfs)

    @Slot()
    def select_out(self):
        """选择输出文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        if selected_dir:
            self.ui.lineEdit_out.setText(selected_dir)

    @Slot()
    def ok(self):
        """图片提取"""
        if not self.pdfs:
            self.process_error("PDF列表为空")
            return
        out_dir = self.ui.lineEdit_out.text().strip()
        if not os.path.isdir(out_dir):
            self.process_error('无效的输出文件夹')
            return
        self.enable_widgets(False)
        self.worker = ExtractThread(self.pdfs, out_dir)
        self.worker.info_signal.connect(self.process_info)
        self.worker.error_signal.connect(self.process_error)
        self.worker.start()

    def process_info(self, message: str):
        QMessageBox.information(
            self,
            "提示",
            message
        )
        self.enable_widgets(True)

    def process_error(self, message: str):
        QMessageBox.critical(
            self,
            "错误",
            message
        )
        self.enable_widgets(True)

    def enable_widgets(self, flag: bool):
        """启用组件"""
        self.ui.lineEdit_out.setEnabled(flag)
        self.ui.lineEdit_pdf.setEnabled(flag)
        self.ui.pushButton_pdf.setEnabled(flag)
        self.ui.pushButton_out.setEnabled(flag)
        self.ui.listWidget.setEnabled(flag)
        self.ui.pushButton_ok.setEnabled(flag)


class ExtractThread(QThread):
    """从pdf提取图片"""

    info_signal = Signal(str)
    error_signal = Signal(str)

    def __init__(self, pdfs: list[str], out_dir: str):
        super().__init__()
        self.pdfs = pdfs
        self.out_dir = out_dir

    def run(self):
        has_bad = False
        for pdf in self.pdfs:
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
            info_message = "提取完成，存在失败的文件，请查阅程序目录下的log.txt"
        else:
            info_message = "提取完成"
        self.info_signal.emit(info_message)
