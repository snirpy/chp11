from PySide6 import QtWidgets, QtGui
import sys

class MainForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("BTS SNIR2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.layoutFormulaire = QtWidgets.QFormLayout()

        self.lbl_login = QtWidgets.QLabel("Login")
        self.LEdit_login = QtWidgets.QLineEdit()
        self.LEdit_login.setPlaceholderText("Saisir votre login")

        self.lbl_pw = QtWidgets.QLabel("Password")
        self.LEdit_pw = QtWidgets.QLineEdit()
        self.LEdit_pw.setPlaceholderText("Saisir votre mot de passe")

        self.btn_connect = QtWidgets.QPushButton("Connect")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

    def addWigets_to_layouts(self):
        self.layoutFormulaire.addRow("Login   ",self.LEdit_login)
        self.layoutFormulaire.addRow("Password",self.LEdit_pw)
        self.layoutFormulaire.addRow(self.btn_connect, self.btn_Quitter)
    

        # self.layoutH1.addWidget(self.lbl_login)
        # self.layoutH1.addWidget(self.LEdit_login)

        # self.layoutH2.addWidget(self.lbl_pw)
        # self.layoutH2.addWidget(self.LEdit_pw)

        # self.layoutH3.addWidget(self.btn_connect)
        # self.layoutH3.addWidget(self.btn_Quitter)
        # self.layoutV.addLayout(self.layoutH1)
        # self.layoutV.addLayout(self.layoutH2)
        # self.layoutV.addLayout(self.layoutH3)
        # self.layoutV.addLayout(self.layoutH4)
        # self.setLayout(self.layoutV)
        self.setLayout(self.layoutFormulaire)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_connect.clicked.connect(self.goToSecond)
         
    def clear_Ledit(self):
        self.LEdit_login.setText("")
    
    def goToSecond(self):
        print("Je change de fenetre")
        form2.show()
        form.hide()
        pass


class SecondForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("BTS SNIR2 - QDialog")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()

    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        

        self.lbl_login = QtWidgets.QLabel("Login")
       
        self.lbl_image = QtWidgets.QLabel("Ici une iamge")

        self.carImage = QtGui.QPixmap("Oxygen.icns")


        # Créer deux boutons (Ajouter et Supprimer) sur la même ligne

        self.lbl_image.setPixmap(self.carImage)
       

        self.btn_connect = QtWidgets.QPushButton("Disconnect")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

    def addWigets_to_layouts(self):

        self.layoutH1.addWidget(self.lbl_login)
       

        self.layoutH2.addWidget(self.lbl_image)
   

        self.layoutH3.addWidget(self.btn_connect)
        self.layoutH3.addWidget(self.btn_Quitter)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_connect.clicked.connect(self.goToFirst)
         
    
    
    def goToFirst(self):
        print("Je retourne vers la principale")
        
        form.show()
        form2.hide()
        pass
  

    
if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    form = MainForm()
    form2 = SecondForm()
    form.show()
    form2.hide()
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()