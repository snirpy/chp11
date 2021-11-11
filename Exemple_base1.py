import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog,QLabel,QHBoxLayout,QMessageBox)

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        # self.setWindowTitle('BTS SNIR2')
        self.label_login = QLabel("Login  : ")
        self.label_password = QLabel("Passwod:")
        self.etat = QLabel("Déconnecté")

        self.lineEdit_username = QLineEdit("")
        self.lineEdit_username.setPlaceholderText("Enter Username Here")
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("Enter Password Here")
        self.lineEdit_password.setEchoMode((QLineEdit.Password))
        
        self.btn_seConnecter = QPushButton("Se connecter")
        self.btn_seDeconnecter = QPushButton("Se déconnecter")
        self.btn_seDeconnecter.hide()
        # Create layout and add widgets
        layoutVer = QVBoxLayout()
        layoutHor1 = QHBoxLayout()
        layoutHor2 = QHBoxLayout()
        layoutHor3 = QHBoxLayout()

        layoutHor1.addWidget(self.label_login)
        layoutHor1.addWidget(self.lineEdit_username)

        layoutHor2.addWidget(self.label_password)
        layoutHor2.addWidget(self.lineEdit_password)

        layoutHor3.addWidget(self.btn_seConnecter)
        layoutHor3.addWidget(self.btn_seDeconnecter)



        # layoutVer.addWidget(self.lineEdit_password)
        layoutVer.addLayout(layoutHor1)
        layoutVer.addLayout(layoutHor2)
        layoutVer.addLayout(layoutHor3)
        # layoutVer.addWidget(self.button)
        layoutVer.addWidget(self.etat)

        # Set dialog layout
        self.setLayout(layoutVer)

        # Add button signal to greetings slot
        self.btn_seConnecter.clicked.connect(self.seConnecter)
        self.btn_seDeconnecter.clicked.connect(self.seDeconnecter)
        self.messagebox = QMessageBox()
        self.messagebox.setText("Erreur de connexion")

    # Greets the user
    def seConnecter(self):
        if self.lineEdit_username.text() == "ilyas" and self.lineEdit_password.text() == "pass":
        # print(f"Hello {self.lineEdit_username.text()}")
            self.etat.setText("Connecté")
            # self.button.setText("Se déconnecter")
            self.lineEdit_username.setPlaceholderText("Enter Username Here")
            self.lineEdit_password.setPlaceholderText("Enter Password Here")
            # self.button.hide()
            self.label_login.hide()
            self.label_password.hide()
            self.lineEdit_username.hide()
            self.lineEdit_password.hide()
            self.btn_seDeconnecter.show()
            self.btn_seConnecter.hide()
            
            
        else:
            self.lineEdit_username.setText("")
            self.lineEdit_password.setText("")
            self.messagebox.show()

    def seDeconnecter(self):
        
        # print(f"Hello {self.lineEdit_username.text()}")
        self.etat.setText("Décoonnecté")
        self.lineEdit_username.setText("")
        self.lineEdit_password.setText("")
        # self.lineEdit_username.setPlaceholderText("Enter Username Here")
        # self.lineEdit_password.setPlaceholderText("Enter Password Here") 
        # self.button.setText("Se déconnecter")

        self.label_login.show()
        self.label_password.show()
        self.lineEdit_username.show()
        self.lineEdit_password.show()
        self.btn_seConnecter.show()
        self.btn_seDeconnecter.hide()
        

            
            
            

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())