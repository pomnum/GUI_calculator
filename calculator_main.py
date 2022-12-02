import sys
import numpy as np
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_clear_equal = QHBoxLayout()
        layout_operation = QGridLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("Equation: ")
        label_solution = QLabel("Number: ")
        self.equation = QLineEdit("")
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        ### layout_equation_solution.addRow(label_equation, self.equation)
        layout_equation_solution.addRow(label_solution, self.solution)

        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_remain = QPushButton("%")
        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_sroot = QPushButton("2^√x")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        button_remain.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_reciprocal.clicked.connect(lambda state, operation = "": self.button_reciprocal_clicked(operation))
        button_square.clicked.connect(lambda state, operation = "": self.button_square_clicked(operation))
        button_sroot.clicked.connect(lambda state, operation = "": self.button_sroot_clicked(operation))
        
        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_number.addWidget(button_plus, 2, 3)
        layout_number.addWidget(button_minus, 1, 3)
        layout_number.addWidget(button_product, 0, 3)
        layout_operation.addWidget(button_remain, 0, 0)

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_ce = QPushButton("CE")
        button_backspace = QPushButton("Backspace")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_ce.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_operation.addWidget(button_ce, 0, 1)
        layout_operation.addWidget(button_clear, 0, 2)
        layout_operation.addWidget(button_backspace, 0, 3)
        layout_number.addWidget(button_equal, 3, 3)
        layout_operation.addWidget(button_reciprocal, 1, 0)
        layout_operation.addWidget(button_square, 1, 1)
        layout_operation.addWidget(button_sroot, 1, 2)
        layout_operation.addWidget(button_division, 1, 3)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        solution = self.solution.text()
        solution += str(num)
        self.solution.setText(solution)

    def button_operation_clicked(self, operation):
        solution = self.solution.text()
        solution += operation
        self.solution.setText(solution)

    def button_equal_clicked(self):
        solution = self.solution.text()
        solution = eval(solution)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        solution = self.solution.text()
        solution = solution[:-1]
        self.solution.setText(solution)

    def button_reciprocal_clicked(self, operation):
        solution = self.solution.text()
        solution = float(solution)
        solution = np.reciprocal(solution)
        self.solution.setText(str(solution))

    def button_square_clicked(self, operation):
        solution = self.solution.text()
        solution = float(solution)
        solution = np.square(solution)
        self.solution.setText(str(solution))

    def button_sroot_clicked(self, operation):
        solution = self.solution.text()
        solution = float(solution)
        solution = np.sqrt(solution)
        self.solution.setText(str(solution))        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())