# -*- coding: utf-8 -*-
import os
import glob
import logging
from datetime import datetime
from pypdf import PdfWriter
from PySide6.QtWidgets import (
    QDialog, 
    QFileDialog, 
    QMessageBox, 
    QAbstractItemView, 
    QProgressDialog
)
from PySide6.QtCore import QThread, Signal, Slot
from ui.ui_merge import Ui_Form


logger = logging.getLogger("merge")

class MergeWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("合并PDF")

        # 列表拖拽
        self.ui.listWidget.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.ui.listWidget.model().rowsMoved.connect(self.handle_row_moved)

        self.ui.pushButton_pdf.clicked.connect(self.select_pdf)
        self.ui.pushButton_out.clicked.connect(self.select_out)
        self.ui.pushButton_ok.clicked.connect(self.ok)

        self.pdfs = []

    @Slot()
    def handle_row_moved(self):
        self.pdfs = [self.ui.listWidget.item(i).text() for i in range(self.ui.listWidget.count())]

    @Slot()
    def select_pdf(self):
        """选择PDF文件夹"""
        pdf_dir = QFileDialog.getExistingDirectory(self)
        if pdf_dir:
            self.ui.lineEdit_pdf.setText(pdf_dir)
            self.pdfs = glob.glob(os.path.join(pdf_dir, "**/*.pdf"), recursive=True)
            self.ui.listWidget.addItems(self.pdfs)

    @Slot()
    def select_out(self):
        """选择输出文件夹"""
        selected_dir = QFileDialog.getExistingDirectory(self)
        if selected_dir:
            self.ui.lineEdit_out.setText(selected_dir)

    @Slot()
    def ok(self):
        """合并pdf"""
        if not self.pdfs:
            self.process_error("PDF列表为空")
            return
        out_dir = self.ui.lineEdit_out.text().strip()
        if not os.path.isdir(out_dir):
            self.process_error('无效的输出文件夹')
            return

        self.enable_widgets(False)
        progress_dialog = QProgressDialog("正在合并", "取消", 0, len(self.pdfs), self)
        
        self.worker = MergeThread(self.pdfs, out_dir)
        self.worker.info_signal.connect(self.process_info)
        self.worker.progress_signal.connect(progress_dialog.setValue)
        self.worker.start()

        progress_dialog.canceled.connect(self.handle_cancel)
        progress_dialog.exec()

    def handle_cancel(self):
        self.worker.terminate()
        self.process_info("合并已取消")
        self.enable_widgets(True)

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


class MergeThread(QThread):
    """合并pdf"""

    info_signal = Signal(str)
    progress_signal = Signal(int)

    def __init__(self, pdfs: list[str], out_dir: str):
        super().__init__()
        self.pdfs = pdfs
        self.out_dir = out_dir

    def run(self):
        has_bad = False
        merger = PdfWriter()
        for i, pdf in enumerate(self.pdfs):
            try:
                merger.append(open(pdf, 'rb'))
            except:
                has_bad = True
                logger.critical(f"错误的pdf文件：{pdf}")
            self.progress_signal.emit(i+1)
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        out_file = os.path.join(self.out_dir, timestamp + '.pdf')
        merger.write(out_file)
        merger.close()

        if has_bad:
            info_message = "合并完成，存在失败的文件，请查阅程序目录下的log.txt"
        else:
            info_message = "合并完成"
        self.info_signal.emit(info_message)
