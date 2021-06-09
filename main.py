

import desin
import sys
from PyQt5 import QtWidgets


class App(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = desin.Ui_MainWindow()
        self.ui.setupUi(self)
        self.set_extion()
        self.val = ""

    def reset_ce(self):
        self.val = "0"
        self.display_val()

    def set_extion(self):
        self.ui.pushButton_10.clicked.connect(self.reset_ce)
        self.ui.pushButton_11.clicked.connect(lambda: self.add_simb("0"))
        self.ui.pushButton_7.clicked.connect(lambda: self.add_simb("1"))
        self.ui.pushButton.clicked.connect(lambda: self.add_simb("7"))
        self.ui.pushButton_2.clicked.connect(lambda: self.add_simb("8"))
        self.ui.pushButton_3.clicked.connect(lambda: self.add_simb("9"))
        self.ui.pushButton_4.clicked.connect(lambda: self.add_simb("4"))
        self.ui.pushButton_5.clicked.connect(lambda: self.add_simb("5"))
        self.ui.pushButton_6.clicked.connect(lambda: self.add_simb("6"))
        self.ui.pushButton_8.clicked.connect(lambda: self.add_simb("2"))
        self.ui.pushButton_9.clicked.connect(lambda: self.add_simb("3"))
        self.ui.pushButton_13.clicked.connect(lambda: self.add_simb("+"))
        self.ui.pushButton_14.clicked.connect(lambda: self.add_simb("-"))
        self.ui.pushButton_15.clicked.connect(lambda: self.add_simb("*"))
        self.ui.pushButton_16.clicked.connect(lambda: self.add_simb("/"))
        self.ui.pushButton_12.clicked.connect(self.mathematik)

    def add_simb(self, b):
        if self.val == "0":
            self.val = b
        else:
            self.val += b
        self.display_val()

    def display_val(self):
        self.ui.lcdNumber.display(self.val)
        self.ui.label.setText(self.val)

    def mathematik(self):
        try:
            self.val = str(eval(self.val))
        except:
            self.val = "Eror"
        self.display_val()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
