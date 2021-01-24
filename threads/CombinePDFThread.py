# -*- coding: utf-8 -*-
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


    def run(self):
        pdf_list = []
        for root, dirs, files in os.walk(self.pdf_dir):
            for f in files:
                filename, file_extension = os.path.splitext(f)
                if file_extension == '.pdf':
                    full_path = os.path.join(root, f)
                    pdf_list.append(full_path)

        if len(pdf_list) == 0:
            self.finish_signal.emit(-1)
            return

        merger = PdfFileMerger()
        for pdf in pdf_list:
            merger.append(open(pdf, 'rb'))
        combined_pdf_name = datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")
        output_file = os.path.join(self.output_dir, combined_pdf_name + '.pdf')
        merger.write(output_file)
        self.finish_signal.emit(0)