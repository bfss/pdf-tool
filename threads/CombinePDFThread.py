# -*- coding: utf-8 -*-
from PyPDF2 import PdfFileMerger

from PySide6.QtCore import QThread, Signal

from datetime import datetime

class CombinePDFThread(QThread):
    """合并pdf"""

    finish_signal = Signal(int)

    def __init__(self, pdf_list):
        super().__init__()
        self.pdf_list = pdf_list


    def run(self):
        merger = PdfFileMerger()
        print(self.pdf_list)
        for pdf in self.pdf_list:
            merger.append(open(pdf, 'rb'))
        combined_pdf_name = datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")
        merger.write(combined_pdf_name + '.pdf')
        self.finish_signal.emit(0)