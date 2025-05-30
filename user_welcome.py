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

class Ui_User_Welcome(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 295)

        # 全局布局：水平
        self.wlayout=QHBoxLayout(Form)

        # 局部布局：垂直，表单, 水平
        self.vlayout = QVBoxLayout()
        self.hlayout_1 = QHBoxLayout()
        self.hlayout_2 = QHBoxLayout()
        self.formlayout = QFormLayout()

        # left: setup login.png
        self.label=QtWidgets.QLabel()
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/Images/user_welcome.png")))

        # 为左边布局添加控件
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
        self.label_1.setPixmap((QtGui.QPixmap("./asserts/Images/title_user_welcome.png")))

        # TODO: Horizon first layer
        self.pFriendName = QLineEdit()
        self.pushButton = QPushButton(Form) # 选择新朋友

        # setup styleSheet
        self.pFriendName.setPlaceholderText("请选择你的朋友")
        self.pFriendName.setFixedSize(280, 37)
        self.pFriendName.setEchoMode(QLineEdit.Normal)

        self.pushButton.setObjectName("pushButton")  # 确定选择
        self.pushButton.setFixedSize(130, 37)

        # Set pushButton styleSheet
        self.pushButton.setStyleSheet("background-color: rgb(0, 204, 255); font: bold 16px;")

        self.hlayout_1.addWidget(self.pFriendName)
        self.hlayout_1.addWidget(self.pushButton)
        self.h1wg = QWidget()
        self.h1wg.setLayout(self.hlayout_1)

        # TODO: Horizon second layer
        self.pNewName = QLineEdit()
        self.pushButton_1 = QPushButton(Form) # 添加朋友
        self.pushButton_2 = QPushButton(Form) # 选择头像

        # setup styleSheet
        self.pNewName.setPlaceholderText("请添加你的新朋友")
        self.pNewName.setFixedSize(280, 37)
        self.pNewName.setEchoMode(QLineEdit.Normal)

        self.pushButton_1.setObjectName("pushButton_1")  # 确定添加
        self.pushButton_1.setFixedSize(130, 37)

        self.pushButton_2.setObjectName("pushButton_2") # 选择头像
        self.pushButton_2.setFixedSize(450, 37)

        # Set pushButton styleSheet
        self.pushButton_1.setStyleSheet("background-color: rgb(0, 204, 255); font: bold 16px;")
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 204, 255); font: bold 16px;")

        self.hlayout_2.addWidget(self.pNewName)
        self.hlayout_2.addWidget(self.pushButton_1)
        self.h2wg = QWidget()
        self.h2wg.setLayout(self.hlayout_2)

        self.label.setText("")
        self.label.setObjectName("label")
        self.label_1.setText("")
        self.label.setObjectName("label_1")

        # 这里是formlayout的布局
        self.formlayout.addWidget(self.label_1)
        self.formlayout.addWidget(self.h1wg)
        self.formlayout.addWidget(self.h2wg)
        self.formlayout.addWidget(self.pushButton_2)

        self.fwg = QWidget()
        self.fwg.setLayout(self.formlayout)
        self.wlayout.addWidget(self.fwg)
        self.setLayout(self.wlayout)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.open_user_chat_page) # 打开自己的聊天界面
        self.pushButton_1.clicked.connect(Form.open_add_friends_page) # 添加自己的好友
        self.pushButton_2.clicked.connect(Form.open_user_portrait_page) # 打开选择头像的界面
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "欢迎使用QQ聊天室"))
        self.pushButton.setText(_translate("Form", "选择确认"))
        self.pushButton_1.setText(_translate("Form", "添加确认"))
        self.pushButton_2.setText(_translate("Form", "选择你喜欢的头像"))
