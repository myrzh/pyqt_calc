from PyQt5.QtWidgets import QWidget, QPushButton


class MainWindowButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setFixedSize(300, 450)

        self.point_btn = QPushButton(self)
        self.point_btn.resize(75, 75)
        self.point_btn.move(0, 375)
        self.point_btn.setText('.')

        self.plus_minus_btn = QPushButton(self)
        self.plus_minus_btn.resize(75, 75)
        self.plus_minus_btn.move(75, 375)
        self.plus_minus_btn.setText('±')

        self.equal_btn = QPushButton(self)
        self.equal_btn.resize(150, 75)
        self.equal_btn.move(150, 375)
        self.equal_btn.setText('=')

        ##############################################

        self.c_btn = QPushButton(self)
        self.c_btn.resize(75, 75)
        self.c_btn.move(0, 300)
        self.c_btn.setText('C')

        self.zero_btn = QPushButton(self)
        self.zero_btn.resize(75, 75)
        self.zero_btn.move(75, 300)
        self.zero_btn.setText('0')

        self.ce_btn = QPushButton(self)
        self.ce_btn.resize(75, 75)
        self.ce_btn.move(150, 300)
        self.ce_btn.setText('CE')

        self.plus_btn = QPushButton(self)
        self.plus_btn.resize(75, 75)
        self.plus_btn.move(225, 300)
        self.plus_btn.setText('+')

        ##############################################

        self.one_btn = QPushButton(self)
        self.one_btn.resize(75, 75)
        self.one_btn.move(0, 225)
        self.one_btn.setText('1')

        self.two_btn = QPushButton(self)
        self.two_btn.resize(75, 75)
        self.two_btn.move(75, 225)
        self.two_btn.setText('2')

        self.three_btn = QPushButton(self)
        self.three_btn.resize(75, 75)
        self.three_btn.move(150, 225)
        self.three_btn.setText('3')

        self.minus_btn = QPushButton(self)
        self.minus_btn.resize(75, 75)
        self.minus_btn.move(225, 225)
        self.minus_btn.setText('–')

        ##############################################

        self.four_btn = QPushButton(self)
        self.four_btn.resize(75, 75)
        self.four_btn.move(0, 150)
        self.four_btn.setText('4')

        self.five_btn = QPushButton(self)
        self.five_btn.resize(75, 75)
        self.five_btn.move(75, 150)
        self.five_btn.setText('5')

        self.six_btn = QPushButton(self)
        self.six_btn.resize(75, 75)
        self.six_btn.move(150, 150)
        self.six_btn.setText('6')

        self.multiply_btn = QPushButton(self)
        self.multiply_btn.resize(75, 75)
        self.multiply_btn.move(225, 150)
        self.multiply_btn.setText('×')

        ##############################################

        self.seven_btn = QPushButton(self)
        self.seven_btn.resize(75, 75)
        self.seven_btn.move(0, 75)
        self.seven_btn.setText('7')

        self.eight_btn = QPushButton(self)
        self.eight_btn.resize(75, 75)
        self.eight_btn.move(75, 75)
        self.eight_btn.setText('8')

        self.nine_btn = QPushButton(self)
        self.nine_btn.resize(75, 75)
        self.nine_btn.move(150, 75)
        self.nine_btn.setText('9')

        self.divide_btn = QPushButton(self)
        self.divide_btn.resize(75, 75)
        self.divide_btn.move(225, 75)
        self.divide_btn.setText('÷')

        ##############################################
        