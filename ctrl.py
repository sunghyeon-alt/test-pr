#ch 7.6.2 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self): #^,% 연산자 제거
        try:
            num1 = float(self.view.le1.text()) #첫 번째 라인 에디트에 입력된 숫자를 읽어옴
            num2 = float(self.view.le2.text()) #두 번째 라인 에디트에 입력된 숫자를 읽어옴
            operator = self.view.cb.currentText() #콤보 박스에 선택된 연산자 확인

            if operator == '+':
                return f'{num1} + {num2} = {self.sum(num1, num2)}'
            elif operator == '-':
                return f'{num1} - {num2} = {self.sub(num1, num2)}'
            elif operator == '*':
                return f'{num1} * {num2} = {self.mul(num1, num2)}'
            elif operator == '/':
                return f'{num1} / {num2} = {self.div(num1, num2)}'
            else:
                return "Calculation Error"
        except:
            return "Calculation Error"

    def connectSignals(self): #btn1을 클릭하면 calculate 결과가 화면에 표시되도록 수정
        self.view.btn1.clicked.connect(lambda:\
                                       self.view.setDisplay(self.calculate())) #버튼1 연결을 변경
        self.view.btn2.clicked.connect(self.view.clearMessage) 

    def sum(self, a, b): #예외 처리 제거: 향후 calculate 함수에서 처리하도록 구현 예정
        return a + b

    def sub(self, a, b): #뺄셈 함수 추가
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b): #예외 처리를 사용하도록 수정
        try:
            if (b == 0):
                raise Exception("DIvisor Error")
        except Exception as e:
            return e
        
        return a / b
    
    def pow(self, a, b):
        try:
            if (a == 0):
                raise Exception("Base Error")
        except Exception as e:
            return e
        
        return pow(a, b)
    
    def mod(self, a, b):
        try:
            if (b == 0):
                raise Exception("Divisor Error")
        
        except Exception as e:
            return e
        
        return a % b