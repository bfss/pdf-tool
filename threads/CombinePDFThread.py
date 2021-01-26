# -*- coding: utf-8 -*-
import PyPDF2
from PyPDF2 import PdfFileMerger

from PySide2.QtCore import QThread, Signal

import os
from datetime import datetime


class CombinePDFThread(QThread):
    """合并pdf"""

    finish_signal = Signal(int)

    def __init__(self, pdf_dir, output_dir):
        super().__init__()
        self.pdf_dir = pdf_dir
        self.output_dir = output_dir

        self.bad_pdfs = []


    def run(self):
        pdf_count = 0
        merger = PdfFileMerger()
        for root, dirs, files in os.walk(self.pdf_dir):
            for f in files:
                filename, file_extension = os.path.splitext(f)
                if file_extension.lower() == '.pdf':
                    pdf = os.path.join(root, f)
                    try:
                        merger.append(open(pdf, 'rb'))
                        pdf_count += 1
                    except:
                        self.bad_pdfs.append(pdf)

        if pdf_count == 0:
            self.finish_signal.emit(-1)
            return
        else:
            combined_pdf_name = datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")
            output_file = os.path.join(self.output_dir, combined_pdf_name + '.pdf')
            merger.write(output_file)
            merger.close()

        if len(self.bad_pdfs) == 0:
            self.finish_signal.emit(0)
        else:
            self.finish_signal.emit(-2)

    
    def get_bad_pdfs(self):
        """返回有问题的pdf"""
        return self.bad_pdfs