# нужные мне библеотеки
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from currency_converter import CurrencyConverter

# импортирую графические вкладки
from convert import Ui_Razmen
from output_money import Snyat
from error import ErrorUi
from vvod import Enter_nal
from vklad_money import Vkladi


class PageOneProj(QMainWindow):             # первая страница терминала
    def __init__(self):
        super(PageOneProj, self).__init__()
        self.show_err = Error()             # указал окно ошибки
        self.uiOne = Ui_Razmen()            # устанавливаю граф. окно
        self.uiOne.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Терминал')
        self.uiOne.input_correct_valut.setPlaceholderText('Из валюты:')         # пояснения для пользоателей
        self.uiOne.input_correct_value.setPlaceholderText('Сумма:')
        self.uiOne.output_correct_valut.setPlaceholderText('В валюты:')
        self.uiOne.output_correct_valut_2.setPlaceholderText('Вывод:')
        self.uiOne.schet.setPlaceholderText('Номер карты(16 цифр):')
        self.uiOne.pageFour.clicked.connect(self.buttonPageFour)               # вкладочки для перехода между страницами
        self.uiOne.pageThree.clicked.connect(self.buttonPageThree)
        self.uiOne.pageTwo.clicked.connect(self.buttonPageTwo)
        self.uiOne.pageOne.clicked.connect(self.buttonPageOne)
        self.uiOne.pushButton.clicked.connect(self.converter)
        self.show()

    @pyqtSlot()
    def converter(self):                # конвертация валюты с проверкой на дурака
        corvect = CurrencyConverter()       # использую библеотеку конвертора
        schet_kard = self.uiOne.schet.text()
        input_currency = self.uiOne.input_correct_valut.text()
        input_amount = self.uiOne.input_correct_value.text()
        output_currency = self.uiOne.output_correct_valut.text()
        if schet_kard.isdigit() and len(schet_kard) == 16:      # проверка на дурака
            if input_amount.isdigit() and input_currency.isupper() and output_currency.isupper():
                input_amount = int(self.uiOne.input_correct_value.text())
                output_amount = round(corvect.convert(input_amount, '%s' % input_currency, '%s' % output_currency), 2)
                # формула конвертации валют и ее последующий вывод
                self.uiOne.output_correct_valut_2.setText(str(output_amount))
            else:
                self.show_err.show()
        else:
            self.show_err.show()

    @pyqtSlot()             # переходы со страницы на страницу (их 4)
    def buttonPageFour(self):
        self.cams = PageFourProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageThree(self):
        self.cams = PageThreeProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageTwo(self):
        self.cams = PageTwoProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageOne(self):
        self.cams = PageOneProj()
        self.cams.show()
        self.close()


class PageThreeProj(QMainWindow):       # третья страница терминала со снятием наличных
    def __init__(self):
        super(PageThreeProj, self).__init__()
        self.show_err = Error()
        self.uiThree = Snyat()          # устанавливаю граф. окно
        self.uiThree.setupUi(self)
        self.init_UI()

    def init_UI(self):          # все тоже счамое что и в первой странице
        self.uiThree.input_chet.setPlaceholderText('Номер карты(16 цифр):')
        self.uiThree.input_value.setPlaceholderText('Сумма:')
        self.uiThree.pageFour.clicked.connect(self.buttonPageFour)
        self.uiThree.pageThree.clicked.connect(self.buttonPageThree)
        self.uiThree.pageTwo.clicked.connect(self.buttonPageTwo)
        self.uiThree.pageOne.clicked.connect(self.buttonPageOne)
        self.uiThree.pushButton.clicked.connect(self.vivod_s_scheta)
        self.show()

    def vivod_s_scheta(self):           # вывод со счёта с опустошением строки конечно проверкой
        self.input_snyat_summ = self.uiThree.input_value.text()
        self.input_snyat_schet = self.uiThree.input_chet.text()
        if self.input_snyat_schet.isdigit() and len(self.input_snyat_schet) == 16:      # сама проверка
            if self.input_snyat_summ.isdigit():
                self.uiThree.input_chet.setText('')     # очищение
                self.uiThree.input_value.setText('')
            else:
                self.show_err.show()
        else:
            self.show_err.show()

    @pyqtSlot()         # снова переходы
    def buttonPageFour(self):
        self.cams = PageFourProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageThree(self):
        self.cams = PageThreeProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageTwo(self):
        self.cams = PageTwoProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageOne(self):
        self.cams = PageOneProj()
        self.cams.show()
        self.close()


class PageTwoProj(QMainWindow):             # вторая страница проекта
    def __init__(self):
        super(PageTwoProj, self).__init__()
        self.show_err = Error()
        self.uiTwo = Enter_nal()            # устанавливаю граф. окно
        self.uiTwo.setupUi(self)
        self.init_UI()

    def init_UI(self):          # кнопочки строчки и т.д. как в предыдущих
        self.uiTwo.input_chet_vvod.setPlaceholderText('Номер карты(16 цифр):')
        self.uiTwo.input_sum_vvod.setPlaceholderText('Сумма:')
        self.uiTwo.pageFour.clicked.connect(self.buttonPageFour)
        self.uiTwo.pageThree.clicked.connect(self.buttonPageThree)
        self.uiTwo.pageTwo.clicked.connect(self.buttonPageTwo)
        self.uiTwo.pageOne.clicked.connect(self.buttonPageOne)
        self.uiTwo.pageOne.clicked.connect(self.buttonPageOne)
        self.uiTwo.pushButton.clicked.connect(self.vvod_s_scheta)
        self.show()

    def vvod_s_scheta(self):        # ввод наличных на некий счёт с некой суммой
        self.input_sum_vvod = self.uiTwo.input_sum_vvod.text()
        self.input_chet_vvod = self.uiTwo.input_chet_vvod.text()
        if self.input_chet_vvod.isdigit() and len(self.input_chet_vvod) == 16:      # сама проверка
            if self.input_sum_vvod.isdigit():
                self.uiTwo.input_chet_vvod.setText('')  # очищение
                self.uiTwo.input_sum_vvod.setText('')
            else:
                self.show_err.show()
        else:
            self.show_err.show()

    @pyqtSlot()             # переходики переходики
    def buttonPageFour(self):
        self.cams = PageFourProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageThree(self):
        self.cams = PageThreeProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageTwo(self):
        self.cams = PageTwoProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageOne(self):
        self.cams = PageOneProj()
        self.cams.show()
        self.close()


class PageFourProj(QMainWindow):            # последняя страница с вкладом
    def __init__(self):
        super(PageFourProj, self).__init__()
        self.show_err = Error()
        self.uiFour = Vkladi()              # устанавливаю граф. окно
        self.uiFour.setupUi(self)
        self.procent = 10           # эту ставку должен менять сам банк а не пользователь
        self.init_UI()

    def init_UI(self):          # некий счёт с некой суммой и выводом
        self.uiFour.input_kard_nomber.setPlaceholderText('Номер карты(16 цифр):')
        self.uiFour.input_sum_vklad.setPlaceholderText('Сумма:')
        self.uiFour.input_procent.setText(str(self.procent))        # показываю ставку банка пользователю
        self.uiFour.output_sum_month.setPlaceholderText('Вывод:')
        self.uiFour.pageFour.clicked.connect(self.buttonPageFour)
        self.uiFour.pageThree.clicked.connect(self.buttonPageThree)
        self.uiFour.pageTwo.clicked.connect(self.buttonPageTwo)
        self.uiFour.pageOne.clicked.connect(self.buttonPageOne)
        self.uiFour.pushButton.clicked.connect(self.nachislit)
        self.show()

    def nachislit(self):            # показываю какие ежемесячные выплаты ожидают клиента с некой суммой
        schet_kard = self.uiFour.input_kard_nomber.text()
        input_amount = self.uiFour.input_sum_vklad.text()
        if schet_kard.isdigit() and len(schet_kard) == 16:
            if input_amount.isdigit():
                input_amount = int(self.uiFour.input_sum_vklad.text())
                output_amount = input_amount * (self.procent / 100)     # формула выплат
                self.uiFour.output_sum_month.setText(str(output_amount))
            else:
                self.show_err.show()
        else:
            self.show_err.show()

    @pyqtSlot()         # снова ппереходы
    def buttonPageFour(self):
        self.cams = PageFourProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageThree(self):
        self.cams = PageThreeProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageTwo(self):
        self.cams = PageTwoProj()
        self.cams.show()
        self.close()

    @pyqtSlot()
    def buttonPageOne(self):
        self.cams = PageOneProj()
        self.cams.show()
        self.close()


class Error(QMainWindow):     # окно с ошибкой , будет выходить при неправильном заполнении строк и можно просто закрыть
    def __init__(self):
        super(Error, self).__init__()
        self.uiEr = ErrorUi()           # устанавливаю граф. окно
        self.uiEr.setupUi(self)

    def init_Ui(self):
        self.setWindowTitle('Ошибка')
        self.show()


# вот конец
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PageOneProj()
    sys.exit(app.exec())
