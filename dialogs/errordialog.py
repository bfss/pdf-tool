# -*- encoding: utf-8 -*-
from PySide2.QtWidgets import QMessageBox


class ErrorDialog(QMessageBox):
    """错误弹窗"""
    def __init__(self, error_message):
        super().__init__()
        self.setWindowTitle('提示')
        self.setButtonText(1, '好的')
        self.setText(error_message)
