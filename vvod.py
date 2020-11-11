from PyQt5 import QtCore, QtGui, QtWidgets


class Enter_nal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 80, 631, 81))
        self.frame.setStyleSheet("background-color: #fb5b5d")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 10, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_chet_vvod = QtWidgets.QLineEdit(self.centralwidget)
        self.input_chet_vvod.setGeometry(QtCore.QRect(150, 280, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_chet_vvod.setFont(font)
        self.input_chet_vvod.setStyleSheet("background-color: #22222e;\n"
                                           "border: 2px solid #f66867;\n"
                                           "border-radius: 30;\n"
                                           "color: white")
        self.input_chet_vvod.setText("")
        self.input_chet_vvod.setAlignment(QtCore.Qt.AlignCenter)
        self.input_chet_vvod.setObjectName("input_correct_valut")
        self.input_sum_vvod = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sum_vvod.setGeometry(QtCore.QRect(150, 390, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_sum_vvod.setFont(font)
        self.input_sum_vvod.setStyleSheet("background-color: #22222e;\n"
                                          "border: 2px solid #f66867;\n"
                                          "border-radius: 30;\n"
                                          "color: white;")
        self.input_sum_vvod.setText("")
        self.input_sum_vvod.setAlignment(QtCore.Qt.AlignCenter)
        self.input_sum_vvod.setObjectName("input_correct_value")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 520, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    color: white;\n"
                                      "    background-color: #fb5b5d;\n"
                                      "    border-radius: 30;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color: #fa4244\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pageOne = QtWidgets.QPushButton(self.centralwidget)
        self.pageOne.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pageOne.setFont(font)
        self.pageOne.setStyleSheet("QPushButton{\n"
                                   "    color: white;\n"
                                   "    background-color: #fb5b5d;\n"
                                   "    border-radius: 30;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "    background-color: #fa4244\n"
                                   "}")
        self.pageOne.setObjectName("pageOne")
        self.pageTwo = QtWidgets.QPushButton(self.centralwidget)
        self.pageTwo.setGeometry(QtCore.QRect(210, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pageTwo.setFont(font)
        self.pageTwo.setStyleSheet("QPushButton{\n"
                                   "    color: white;\n"
                                   "    background-color: #fb5b5d;\n"
                                   "    border-radius: 30;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed{\n"
                                   "    background-color: #fa4244\n"
                                   "}")
        self.pageTwo.setObjectName("pageTwo")
        self.pageFour = QtWidgets.QPushButton(self.centralwidget)
        self.pageFour.setGeometry(QtCore.QRect(580, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pageFour.setFont(font)
        self.pageFour.setStyleSheet("QPushButton{\n"
                                    "    color: white;\n"
                                    "    background-color: #fb5b5d;\n"
                                    "    border-radius: 30;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed{\n"
                                    "    background-color: #fa4244\n"
                                    "}")
        self.pageFour.setObjectName("pageFour")
        self.pageThree = QtWidgets.QPushButton(self.centralwidget)
        self.pageThree.setGeometry(QtCore.QRect(400, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pageThree.setFont(font)
        self.pageThree.setStyleSheet("QPushButton{\n"
                                     "    color: white;\n"
                                     "    background-color: #fb5b5d;\n"
                                     "    border-radius: 30;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed{\n"
                                     "    background-color: #fa4244\n"
                                     "}")
        self.pageThree.setObjectName("pageThree")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Зачисление наличных"))
        self.pushButton.setText(_translate("MainWindow", "ВВЕСТИ"))
        self.pageFour.setText(_translate("MainWindow", "Вклад"))
        self.pageOne.setText(_translate("MainWindow", "Разменять наличные"))
        self.pageTwo.setText(_translate("MainWindow", "Ввести наличные"))
        self.pageThree.setText(_translate("MainWindow", "Снять наличные"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Enter_nal()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
