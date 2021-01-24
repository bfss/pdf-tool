# -*- encoding: utf-8 -*-
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Slot

from uis.ui_errordialog import Ui_Dialog


class ErrorDialog(QDialog):
    """错误弹窗"""
    def __init__(self, error_message):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label_error_message.setText(error_message)

