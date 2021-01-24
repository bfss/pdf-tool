# -*- coding: utf-8 -*-
import os

from PySide2.QtCore import Signal, QThread


class SelectDirThread(QThread):
    """选择文件夹并统计文件数"""

    finish_signal = Signal(int)

    def __init__(self, selected_dir):
        super().__init__()
        self.selected_dir = selected_dir
        self.pdf_list = []


    def run(self):
        for root, dirs, files in os.walk(self.selected_dir):
            for f in files:
                filename, file_extension = os.path.splitext(f)
                if file_extension == '.pdf':
                    full_path = os.path.join(root, f)
                    self.pdf_list.append(full_path)
        self.finish_signal.emit(0)


    def get_result(self):
        """返回结果"""
        return self.pdf_list