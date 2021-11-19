from PySide6.QtWidgets import QApplication, QDialog, QGroupBox, QHBoxLayout, QLabel, QPushButton,QMainWindow, QRadioButton, QVBoxLayout, QWidget
from PySide6 import QtGui, QtCore

class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.create_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()
        self.create_main_window()
        

    def create_main_window(self):
        self.setWindowTitle("Learning RadioButton")
        self.resize(450,250)
        
        self.setWindowIcon(QtGui.QIcon(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/Windows.ico'))
       

        self.layoutH2.addWidget(self.button_quitter)
        self.layoutH3.addWidget(self.label)
        VBox = QVBoxLayout()
        VBox.addWidget(self.groupBox1)
        
        VBox.addLayout(self.layoutH3)
        VBox.addLayout(self.layoutH2)
        self.layoutH2.setContentsMargins(150,0,150,0)
        # self.setLayout(VBox)

        self.widget = QWidget()
        self.widget.setLayout(VBox)
        self.setCentralWidget(self.widget)


        
    def create_widgets(self):
        self.Radio_btn1 = QRadioButton("Windows",self)
        self.Radio_btn1.setIcon(QtGui.QIcon(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/Windows.ico'))
        
        # self.Button.setGeometry(QtCore.QRect(300,350,150,50))
        self.Radio_btn1.setIconSize(QtCore.QSize(40,40))
        self.Radio_btn1.setToolTip("<h3>Click here to see something cool</h3>")
        self.Radio_btn1.setChecked(True)
        self.Radio_btn1.toggled.connect(self.show_window)
        self.Radio_btn1.setFont(QtGui.QFont("Sanserif",12))
        # self.Radio_btn1.setStyleSheet('font-weight: bold')
        self.Radio_btn1.setStyleSheet('color:#303D46')


        self.Radio_btn2 = QRadioButton("MacOs",self)
        self.Radio_btn2.setIcon(QtGui.QIcon(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/mac.ico'))
        # self.Button.setGeometry(QtCore.QRect(300,350,150,50))
        self.Radio_btn2.setIconSize(QtCore.QSize(40,40))
        self.Radio_btn2.setToolTip("<h3>Click here to see something cool</h3>")
        self.Radio_btn2.toggled.connect(self.show_mac)
        self.Radio_btn2.setFont(QtGui.QFont("Sanserif",12))
        # self.Radio_btn2.setStyleSheet('font-weight: bold')
        self.Radio_btn2.setStyleSheet('color:#1F7B99')


        self.Radio_btn3 = QRadioButton("Linux",self)
        self.Radio_btn3.setIcon(QtGui.QIcon(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/linux.ico'))
        # self.Button.setGeometry(QtCore.QRect(300,350,150,50))
        self.Radio_btn3.setIconSize(QtCore.QSize(40,40))
        self.Radio_btn3.setToolTip("<h3>Click here to see something cool</h3>")
        self.Radio_btn3.toggled.connect(self.show_linux)
        self.Radio_btn3.setFont(QtGui.QFont("Sanserif",12))
        # self.Radio_btn3.setStyleSheet('font-weight: bold')
        self.Radio_btn3.setStyleSheet('color:#1F7B99')

        self.button_quitter = QPushButton("Quitter",self)
        self.button_quitter.setIcon(QtGui.QIcon(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/quit.ico'))
        # self.Button.setGeometry(QtCore.QRect(300,350,150,50))
        self.button_quitter.setIconSize(QtCore.QSize(40,40))
        self.button_quitter.setToolTip("<h3>Click here to see something cool</h3>")
        




        self.label= QLabel("Windows is your operating system",self)
        self.label.setFont(QtGui.QFont("Sanserif",12))
        self.label.setStyleSheet('font-weight: bold')
        # self.groupBox1.setStyleSheet('color:#1F7B99')
        # self.label.setGeometry(QtCore.QRect(30,30,300,300))
        # pixmap = QtGui.QPixmap(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/Girls-Blue-Dress.ico')
        # self.label.setPixmap(pixmap)
        # self.label.resize(280,280)
        # self.setCentralWidget(Button)
        # self.Button.move(300,350)

        # self.label_invisible= QLabel()

    def create_layouts(self):
        self.layoutH3 = QHBoxLayout()
        self.layoutH2 = QHBoxLayout()
        self.layout_main = QHBoxLayout()
        self.groupBox1 = QGroupBox("What is your operating system?")
        self.groupBox1.setContentsMargins(50,20,50,0)
        

    def add_widgets_to_layouts(self):

        # self.layoutH1.addWidget(self.label)

        self.layout_main.addWidget(self.Radio_btn1)
        self.layout_main.addWidget(self.Radio_btn2)
        self.layout_main.addWidget(self.Radio_btn3)
        # self.layoutH2.addWidget(self.label_invisible)

        # self.layout_main.addLayout(self.layoutH1)
        # self.layout_main.addLayout(self.layoutH2)

        self.groupBox1.setLayout(self.layout_main)

    def show_window(self):
        
        # pixmap = QtGui.QPixmap(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/Windows.ico')
        # self.label.setPixmap(pixmap)
        self.label.setText(self.Radio_btn1.text() + " is your operating system")

    def show_mac(self):
        pass
        # pixmap = QtGui.QPixmap(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/mac.ico')
        # self.label.setPixmap(pixmap)
        self.label.setText(self.Radio_btn2.text() + " is your operating system")

    def show_linux(self):
        pass
        # pixmap = QtGui.QPixmap(r'C:\Users\x260\Desktop\tempo\codagePython\PySide6\base\LearnPYside/linux.ico')
        # self.label.setPixmap(pixmap)
        self.label.setText(self.Radio_btn3.text() + " is your operating system")
    
    def setup_connections(self):
        self.Radio_btn1.clicked.connect(self.show_window)
        self.Radio_btn2.clicked.connect(self.show_mac)
        self.Radio_btn3.clicked.connect(self.show_linux)
        self.button_quitter.clicked.connect(self.close)

    
       
appli = QApplication([])
mon_window = MaFenetre()
mon_window.show()
appli.exec()