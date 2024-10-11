#ch 8.1.3 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox, QLabel) #QLabel 추가
from PyQt5.QtGui import QIcon, QFont #QFont 추가
from PyQt5 import QtCore #모듈 추가

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() #텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) #텍스트 에디트 위젯을 읽기만 가능하도록 수정

        
        self.lbl1 = QLabel('v2.3.0', self) #버전 정보 표시를 위한 lbl1 위젯 생성
        self.lbl1.setFont(QFont('Consolas', 10)) #폰트 설정 추가, Consolas, 사이즈 10
        self.btn1 = QPushButton('Calc', self) #버튼 추가
        self.btn2 = QPushButton('clear', self) #버튼 2 추가

        self.le1 = QLineEdit('0', self) #라인 에디트1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight) #라인 에디트1 문자열 배치 설정
        self.le1.setFocus(True) #포커스 설정
        self.le1.selectAll() #텍스트 전체 선택

        self.le2 = QLineEdit('0', self) #라인 에디트2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight) #라인 에디트2 문자열 배치 설정

        self.cb = QComboBox(self) #콤보 박스 추가
        self.cb.addItems(['+', '-', '*', '/', '^', '%']) #% 연산자 추가

        hbox_formular = QHBoxLayout() #새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        hbox = QHBoxLayout() # 수평 박스 레이아웃을 추가하고 버튼1, 2 추가
        hbox.addStretch(1) # 공백
        hbox.addWidget(self.lbl1) #버전 정보 표시를 위한 lbl1 위젯 생성
        hbox.addWidget(self.btn1) #버튼 1 배치
        hbox.addWidget(self.btn2) #버튼 2 배치

        vbox = QVBoxLayout() #수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1) #수직 레이아웃에 텍스트 에디트 위젯 추가

        # vbox.addWidget(self.btn1) #버튼 위치
        vbox.addLayout(hbox_formular) #hbox_formular 배치
        vbox.addLayout(hbox) #btn1 위치에 hbox를 배치
        vbox.addStretch(1) #빈 공간

        self.setLayout(vbox) #빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) #윈도 아이콘 추가
        self.resize(256,256)
        self.show()

    def setDisplay(self, text): #버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        self.te1.appendPlainText(text)

    def clearMessage(self):
        self.te1.clear()