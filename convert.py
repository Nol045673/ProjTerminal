from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Razmen(object):
    def setupUi(self, Razmen):
        Razmen.setObjectName("Razmen")
        Razmen.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Razmen)
        self.centralwidget.setStyleSheet("background-color: #22222e")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 60, 631, 81))
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
        self.input_correct_valut = QtWidgets.QLineEdit(self.centralwidget)
        self.input_correct_valut.setGeometry(QtCore.QRect(150, 240, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_correct_valut.setFont(font)
        self.input_correct_valut.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.input_correct_valut.setText("")
        self.input_correct_valut.setAlignment(QtCore.Qt.AlignCenter)
        self.input_correct_valut.setObjectName("input_correct_valut")
        self.input_correct_value = QtWidgets.QLineEdit(self.centralwidget)
        self.input_correct_value.setGeometry(QtCore.QRect(150, 310, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_correct_value.setFont(font)
        self.input_correct_value.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.input_correct_value.setText("")
        self.input_correct_value.setAlignment(QtCore.Qt.AlignCenter)
        self.input_correct_value.setObjectName("input_correct_value")
        self.output_correct_valut = QtWidgets.QLineEdit(self.centralwidget)
        self.output_correct_valut.setGeometry(QtCore.QRect(150, 380, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_correct_valut.setFont(font)
        self.output_correct_valut.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.output_correct_valut.setText("")
        self.output_correct_valut.setAlignment(QtCore.Qt.AlignCenter)
        self.output_correct_valut.setObjectName("output_correct_valut")
        self.output_correct_valut_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.output_correct_valut_2.setGeometry(QtCore.QRect(150, 450, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_correct_valut_2.setFont(font)
        self.output_correct_valut_2.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.output_correct_valut_2.setText("")
        self.output_correct_valut_2.setAlignment(QtCore.Qt.AlignCenter)
        self.output_correct_valut_2.setObjectName("output_correct_valut_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 520, 381, 61))
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 320, 120, 181))
        self.frame_2.setStyleSheet("background-color: #fb5b5d")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 111, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
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
        self.schet = QtWidgets.QLineEdit(self.centralwidget)
        self.schet.setGeometry(QtCore.QRect(150, 170, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schet.setFont(font)
        self.schet.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white")
        self.schet.setText("")
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
        self.schet.setAlignment(QtCore.Qt.AlignCenter)
        self.schet.setObjectName("schet")
        Razmen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Razmen)
        QtCore.QMetaObject.connectSlotsByName(Razmen)

    def retranslateUi(self, Razmen):
        _translate = QtCore.QCoreApplication.translate
        Razmen.setWindowTitle(_translate("Razmen", "MainWindow"))
        self.label.setText(_translate("Razmen", "ОБМЕН ВАЛЮТЫ"))
        self.pushButton.setText(_translate("Razmen", "ПЕРЕВЕСТИ"))
        self.label_2.setText(_translate("Razmen", "ОСНОВНЫЕ ВАЛЮТЫ:"))
        self.label_3.setText(_translate("Razmen", "EUR"))
        self.label_4.setText(_translate("Razmen", "USD"))
        self.label_5.setText(_translate("Razmen", "RUB"))
        self.pageFour.setText(_translate("MainWindow", "Вклад"))
        self.pageOne.setText(_translate("Razmen", "Разменять наличные"))
        self.pageTwo.setText(_translate("Razmen", "Ввести наличные"))
        self.pageThree.setText(_translate("Razmen", "Снять наличные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Razmen = QtWidgets.QMainWindow()
    ui = Ui_Razmen()
    ui.setupUi(Razmen)
    Razmen.show()
    sys.exit(app.exec_())
