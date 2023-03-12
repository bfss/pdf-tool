# -*- coding: utf-8 -*-
import os
import glob
from datetime import datetime
from PyPDF2 import PdfReader
from PySide2.QtCore import QThread, Signal


class ExtractThread(QThread):
    """从pdf提取图片"""

    finish_signal = Signal(int)

    def __init__(self, pdf_dir, output_dir):
        super().__init__()
        self.pdf_dir = pdf_dir
        self.output_dir = output_dir

        self.bad_pdfs = []


    def run(self):
        pdfs = glob.glob(os.path.join(self.pdf_dir, "**/*.pdf"), recursive=True)
        if pdfs:
            for pdf in pdfs:
                try:
                    reader = PdfReader(pdf)
                    pages = reader.pages
                    count = 0
                    for page in pages:
                        for image in page.images:
                            pdfname = os.path.basename(pdf).split(".")[0]
                            dirname = os.path.join(self.output_dir, pdfname)
                            os.makedirs(dirname, exist_ok=True)
                            outfile = os.path.join(dirname, str(count)+".jpg")
                            with open(outfile, "wb") as f:
                                f.write(image.data)
                            count += 1
                except:
                    self.bad_pdfs.append(pdf)
        else:
            self.finish_signal.emit(-1)
            return
        
        if len(self.bad_pdfs) == 0:
            self.finish_signal.emit(0)
        else:
            self.finish_signal.emit(-2)

    
    def get_bad_pdfs(self):
        """返回有问题的pdf"""
        return self.bad_pdfs