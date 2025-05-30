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

class Ui_Index_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 453)
        # setup welcome.png
        self.label=QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(23, 10, 585, 368))
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/Images/welcome_qq.png")))

        # setup pushButton for choose variety of datasets
        self.pushButton = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(23, 393, 585, 41))

        self.pushButton.setObjectName("pushButton")

        # setup pushButton color
        self.pushButton.setStyleSheet("background-color: rgb(0, 204, 255); font: bold 16px;")

        self.label.setText("")
        self.label.setObjectName("label")
        self.retranslateUi(Form)

        # setup the signal slot function
        self.pushButton.clicked.connect(Form.open_user_page)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QQ chat with Nvidia AI"))
        self.pushButton.setText(_translate("Form", "QQ chat with AgentIQ"))

