from PyQt5 import QtCore, QtGui, QtWidgets


class Vkladi(object):
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
        self.label.setGeometry(QtCore.QRect(170, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_kard_nomber = QtWidgets.QLineEdit(self.centralwidget)
        self.input_kard_nomber.setGeometry(QtCore.QRect(30, 190, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_kard_nomber.setFont(font)
        self.input_kard_nomber.setStyleSheet("background-color: #22222e;\n"
                                             "border: 2px solid #f66867;\n"
                                             "border-radius: 30;\n"
                                             "color: white")
        self.input_kard_nomber.setText("")
        self.input_kard_nomber.setAlignment(QtCore.Qt.AlignCenter)
        self.input_kard_nomber.setObjectName("input_kard_nomber")
        self.input_sum_vklad = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sum_vklad.setGeometry(QtCore.QRect(30, 270, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_sum_vklad.setFont(font)
        self.input_sum_vklad.setStyleSheet("background-color: #22222e;\n"
                                           "border: 2px solid #f66867;\n"
                                           "border-radius: 30;\n"
                                           "color: white;")
        self.input_sum_vklad.setText("")
        self.input_sum_vklad.setAlignment(QtCore.Qt.AlignCenter)
        self.input_sum_vklad.setObjectName("input_sum_vklad")
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
        self.output_sum_month = QtWidgets.QLineEdit(self.centralwidget)
        self.output_sum_month.setGeometry(QtCore.QRect(30, 400, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_sum_month.setFont(font)
        self.output_sum_month.setStyleSheet("background-color: #22222e;\n"
                                            "border: 2px solid #f66867;\n"
                                            "border-radius: 30;\n"
                                            "color: white;")
        self.output_sum_month.setText("")
        self.output_sum_month.setAlignment(QtCore.Qt.AlignCenter)
        self.output_sum_month.setObjectName("output_sum_month")
        self.input_procent = QtWidgets.QLineEdit(self.centralwidget)
        self.input_procent.setGeometry(QtCore.QRect(560, 260, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_procent.setFont(font)
        self.input_procent.setStyleSheet("background-color: #22222e;\n"
                                         "border: 2px solid #f66867;\n"
                                         "border-radius: 30;\n"
                                         "color: white")
        self.input_procent.setText("")
        self.input_procent.setAlignment(QtCore.Qt.AlignCenter)
        self.input_procent.setObjectName("input_procent")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(569, 210, 191, 31))
        self.frame_2.setStyleSheet("background-color: #fb5b5d")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(70, 340, 411, 41))
        self.frame_3.setStyleSheet("background-color: #fb5b5d")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(70, 0, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Вклад наличных"))
        self.pushButton.setText(_translate("MainWindow", "ЗАЧИСЛИТЬ"))
        self.pageOne.setText(_translate("MainWindow", "Разменять наличные"))
        self.pageTwo.setText(_translate("MainWindow", "Ввести наличные"))
        self.pageThree.setText(_translate("MainWindow", "Снять наличные"))
        self.pageFour.setText(_translate("MainWindow", "Вклад"))
        self.label_3.setText(_translate("MainWindow", "Процент:"))
        self.label_2.setText(_translate("MainWindow", "Ежемесячные выплаты:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Vkladi()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
