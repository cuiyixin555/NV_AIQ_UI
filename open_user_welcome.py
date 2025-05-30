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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton
from user_welcome import Ui_User_Welcome

class open_user_welcome(QtWidgets.QWidget, Ui_User_Welcome): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_user_welcome, self).__init__(parent)
        self.name = ""
        self.setupUi(self) # import Ui_Login

        # 实例化子窗体
        # self.open_user_chat = open_client_A()
        # self.open_friend_chat = open_client_B()
        # self.new_client_A = open_new_client_A()
        # self.open_user_portrait = open_user_portrait()
        # self.open_add_friends = open_add_friends()

    def setName(self, name):
        self.name = name

    # signal channel for connection
    def open_user_portrait_page(self):
        # self.open_user_portrait.setName(self.name)
        # self.open_user_portrait.show()
        pass

    def open_user_chat_page(self):
        # friendName = self.pFriendName.text().strip()
        # self.open_user_chat.setName(self.name)
        # self.open_user_chat.show()
        # self.open_friend_chat.setName(friendName)
        # self.open_friend_chat.show()
        # self.new_client_A.show()
        passs

    def open_add_friends_page(self):
        pass
