import sys

from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from mainwindow_class import MainWindowButtons


class MainWindow(MainWindowButtons):
    def initUI(self):
        super().initUI()
        self.expression_stack = ['0', '', '']

        self.current_text = QLabel('0', self)
        self.current_text.move(0, 25)
        self.current_text.resize(300, 55)
        self.current_text.setFont(QFont('Consolas', 50))
        self.current_text.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.upper_text = QLabel('', self)
        self.upper_text.move(250, 5)
        self.upper_text.setFont(QFont('Arial', 15))

        self.ce_btn.clicked.connect(self.ce_click)
        self.c_btn.clicked.connect(self.c_click)

        self.zero_btn.clicked.connect(self.number_click)
        self.one_btn.clicked.connect(self.number_click)
        self.two_btn.clicked.connect(self.number_click)
        self.three_btn.clicked.connect(self.number_click)
        self.four_btn.clicked.connect(self.number_click)
        self.five_btn.clicked.connect(self.number_click)
        self.six_btn.clicked.connect(self.number_click)
        self.seven_btn.clicked.connect(self.number_click)
        self.eight_btn.clicked.connect(self.number_click)
        self.nine_btn.clicked.connect(self.number_click)

        self.divide_btn.clicked.connect(self.divide_click)
        # self.multiply_btn.clicked.connect(self.multiply_click)
        # self.minus_btn.clicked.connect(self.minus_click)
        # self.plus_btn.clicked.connect(self.plus_click)

        self.plus_minus_btn.clicked.connect(self.plus_minus_click)

    def get_current_text(self):
        return self.current_text.text()

    def set_current_text(self, txt):
        self.current_text.setText(txt)

    def show_error(self):
        self.set_current_text('ERROR')

    def number_click(self):
        if self.get_current_text() == '0' or self.get_current_text() == 'ERROR':
            self.set_current_text('')
        self.set_current_text(self.get_current_text() + self.sender().text())
        if self.expression_stack[2]
        if len(self.get_current_text()) > 8:
            self.show_error()

    def ce_click(self):
        self.set_current_text('0')
        self.expression_stack[1] = ''

    def c_click(self):
        self.ce_click()
        self.upper_text.setText('')
        self.expression_stack = ['0', '', '']

    def plus_minus_click(self):
        if self.get_current_text() != 'ERROR':
            self.set_current_text(str(-int(self.get_current_text())))
    
    def divide_click(self):
        self.expression_stack[2] = '/'
        # TODO: division



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.setStyleSheet("QPushButton{font-size: 18pt;font-family: consolas;}")
    main_window.show()
    sys.exit(app.exec())