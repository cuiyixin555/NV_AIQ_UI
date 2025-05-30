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
# corresponding to welcome.py
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from chat_page import Ui_Chat_Page
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton
from open_user_welcome import open_user_welcome

class open_chat_page(QtWidgets.QWidget, Ui_Chat_Page): # 注意：在对象初始化的时候import的是Ui_Form的类对象

    def __init__(self, parent=None):
        super(open_chat_page, self).__init__(parent)
        self.setupUi(self) # import Ui_Login

        # Init sub-window
        self.open_user_welcome = open_user_welcome()

    # signal channel for connection
    def open_user_welcome_page(self):
        # TODO: send uname and pwd to server
        # get uname pwd
        uname = self.pUserName.text().strip()
        pwd = self.pPassword.text().strip()
        button = "1"
        flag = "@" # 表示用户的一个标记
        mes = button + flag+ uname + '#' + pwd # '#' is split signal
