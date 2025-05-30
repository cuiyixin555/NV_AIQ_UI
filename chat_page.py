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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton

class Ui_Chat_Page(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 295)

        # Global Layout：Horizon
        self.wlayout=QHBoxLayout(Form)

        # Local Layout：Vertical，Form, Horizon
        self.vlayout = QVBoxLayout()
        self.formlayout = QFormLayout()
        self.standardlayout = QHBoxLayout()

        # left: setup login.png
        self.label=QtWidgets.QLabel()
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/Images/user_login.png")))

        # Add controls to the left layout
        self.vlayout.addWidget(self.label)
        self.vwg = QWidget()
        self.vwg.setLayout(self.vlayout)
        self.wlayout.addWidget(self.vwg)

        # right: setup input text
        self.label_1=QtWidgets.QLabel()
        self.label_1.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label_1.setPixmap((QtGui.QPixmap("./asserts/Images/title_user_login.png")))

        self.pUserName=QLineEdit()
        self.pPassword=QLineEdit()

        self.pUserName.setPlaceholderText("Put question you want")

        # Set up the presentation effect
        self.pUserName.setEchoMode(QLineEdit.Normal)
        self.pPassword.setEchoMode(QLineEdit.Normal)
        self.pUserName.setFixedSize(445, 31)
        self.pPassword.setFixedSize(445, 102)

        # setup pushButton for choose variety of datasets
        self.pushButton = QPushButton(Form) # 注册

        self.pushButton.setObjectName("pushButton") # 注册
        self.pushButton.setFixedSize(445, 31) # 注册

        self.label.setText("")
        self.label.setObjectName("label")
        self.label_1.setText("")
        self.label.setObjectName("label_1")

        # 这里是formlayout的布局
        self.formlayout.addWidget(self.label_1)
        self.formlayout.addWidget(self.pUserName) # QLineEdit
        self.formlayout.addWidget(self.pPassword) # QLineEdit
        self.formlayout.addWidget(self.pushButton)  # Register

        self.fwg = QWidget()
        self.fwg.setLayout(self.formlayout)
        self.wlayout.addWidget(self.fwg)
        self.setLayout(self.wlayout)

        # setup pushButton stylesheet
        self.pushButton.setStyleSheet("background-color: rgb(0, 204, 255); font: bold 14px;")

        self.retranslateUi(Form)
        # self.pushButton.clicked.connect(Form.open_register_page) # chat with AgentIQ

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QQ chat with AgentIQ"))
        self.pushButton.setText(_translate("Form", "Chat with AgentIQ"))
