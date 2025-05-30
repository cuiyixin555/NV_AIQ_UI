# MIT License

# Copyright (c) 2025 CUI Xin (崔 欣)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from index import Ui_Index_Form
from open_chat_page import open_chat_page
import subprocess

class open_index(QtWidgets.QWidget, Ui_Index_Form): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_index, self).__init__(parent)
        self.setupUi(self) # import Ui_Form
        status = subprocess.call(["export NVIDIA_API_KEY=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"], shell=True)
        print("The shell cli is executed ok")

        # Instantiates a child form
        self.open_chat_page = open_chat_page()

    # signal channel for connection
    def open_user_page(self):
        self.open_chat_page.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = open_index()
    window.show()
    app.exec_()
