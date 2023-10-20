"""
Ce code est en Python et utilise la bibliothèque PySide6 pour créer une fenêtre de dialogue (QDialog) avec une interface utilisateur permettant de saisir deux nombres, de les additionner et d'afficher le résultat. Voici une explication du code par sections :

Importations :

Le code commence par importer la classe QDialog de la bibliothèque PySide6, qui est utilisée pour créer la fenêtre de dialogue.
Définition de la classe MaFenetre :

La classe MaFenetre est définie, dérivée de QtWidgets.QDialog.
Le constructeur __init__ est défini, où diverses initialisations sont effectuées, notamment la définition de la taille de la fenêtre et du titre.
Les méthodes create_layouts, create_widgets, addWigets_to_layouts, et setup_connections sont appelées pour configurer l'interface utilisateur et établir les connexions entre les widgets.
Création de mises en page (create_layouts) :

Plusieurs mises en page sont créées, notamment une mise en page verticale (layoutV) et plusieurs mises en page horizontales (layoutH0, layoutH1, layoutH2, ...). Ces mises en page seront utilisées pour organiser les widgets dans la fenêtre.
Création de widgets (create_widgets) :

Plusieurs widgets sont créés, tels que des boutons radio, des étiquettes (labels), des zones de texte (line edits), des boutons et des étiquettes pour afficher les résultats.
Certains widgets sont initialisés avec des valeurs par défaut.
Ajout de widgets aux mises en page (addWigets_to_layouts) :

Les widgets créés sont ajoutés aux mises en page appropriées pour organiser l'interface utilisateur.
Les mises en page horizontales sont ensuite ajoutées à la mise en page verticale, et cette dernière est définie comme la mise en page de la fenêtre.
Configuration des connexions (setup_connections) :

Les connexions entre les signaux (événements) et les slots (méthodes) sont configurées, de manière à déclencher des actions en réponse aux interactions de l'utilisateur.
Par exemple, lorsque l'utilisateur clique sur le bouton "Calculer," la méthode calculer est appelée.
Méthodes pour gérer les interactions :

Plusieurs méthodes sont définies pour gérer les interactions de l'utilisateur, telles que activer, desactiver, calculer, et effacer. Ces méthodes modifient l'état des widgets et effectuent des opérations en conséquence.
Création de l'application et de la fenêtre :

Une instance de QApplication est créée.
Une instance de MaFenetre est créée, et la fenêtre est affichée à l'aide de show().
L'application est exécutée avec app.exec().
"""

from PySide6 import QtWidgets

# Définition de la classe MaFenetre qui hérite de QDialog
class MaFenetre(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 100)
        self.setWindowTitle("BTS SNIR2 - QDialog")  # Définit le titre de la fenêtre de dialogue comme "BTS SNIR2 - QDialog"
        self.create_layouts()  # Crée les mises en page
        self.create_widgets()  # Crée les widgets
        self.addWigets_to_layouts()  # Ajoute les widgets aux mises en page
        self.setup_connections()  # Configure les connexions

    def create_layouts(self):
        # Crée différentes mises en page (Layout)
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH0 = QtWidgets.QHBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()
        self.layoutH5 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        # Crée les widgets et configure des valeurs par défaut
        self.radioBt_activer = QtWidgets.QRadioButton("Activer")
        self.radioBt_desactiver = QtWidgets.QRadioButton("Désactiver")

        self.lbl_Nombre1 = QtWidgets.QLabel("Nombre1")
        self.LEdit_Nombre1 = QtWidgets.QLineEdit()
        self.LEdit_Nombre1.setPlaceholderText("Saisir votre Nombre1")

        self.lbl_Nombre2 = QtWidgets.QLabel("Nombre2")
        self.LEdit_Nombre2 = QtWidgets.QLineEdit()
        self.LEdit_Nombre2.setPlaceholderText("Saisir votre Nombre2")

        self.lbl_calcul = QtWidgets.QLabel("La somme")
        self.lbl_resultat = QtWidgets.QLabel("......")

        self.btn_Calculer = QtWidgets.QPushButton("Calculer")
        self.btn_Effacer = QtWidgets.QPushButton("Effacer")

        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

        self.radioBt_desactiver.setChecked(True)  # Bouton radio désactivé par défaut
        self.LEdit_Nombre1.setDisabled(True)  # Zone de texte désactivée par défaut
        self.LEdit_Nombre2.setDisabled(True)  # Zone de texte désactivée par défaut

    def addWigets_to_layouts(self):
        # Ajoute les widgets aux mises en page (Layout)
        self.layoutH0.addWidget(self.radioBt_activer)
        self.layoutH0.addWidget(self.radioBt_desactiver)

        self.layoutH1.addWidget(self.lbl_Nombre1)
        self.layoutH1.addWidget(self.LEdit_Nombre1)

        self.layoutH2.addWidget(self.lbl_Nombre2)
        self.layoutH2.addWidget(self.LEdit_Nombre2)

        self.layoutH3.addWidget(self.lbl_calcul)
        self.layoutH3.addWidget(self.lbl_resultat)

        self.layoutH4.addWidget(self.btn_Calculer)
        self.layoutH4.addWidget(self.btn_Effacer)

        self.layoutH5.addWidget(self.btn_Quitter)

        self.layoutV.addLayout(self.layoutH0)
        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.layoutV.addLayout(self.layoutH5)
        self.setLayout(self.layoutV)  # Définit la mise en page de la fenêtre

    def setup_connections(self):
        # Configure les connexions entre les signaux (événements) et les slots (méthodes)
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Calculer.clicked.connect(self.calculer)
        self.btn_Effacer.clicked.connect(self.effacer)
        self.radioBt_activer.clicked.connect(self.activer)
        self.radioBt_desactiver.clicked.connect(self.desactiver)

    def activer(self):
        # Active les zones de texte lorsque le bouton radio "Activer" est sélectionné
        if self.radioBt_activer.isChecked():
            print("Activer") # une vérification sur la console que la méthode fonctionne
            self.LEdit_Nombre1.setDisabled(False)
            self.LEdit_Nombre2.setDisabled(False)

    def desactiver(self):
        # Désactive les zones de texte lorsque le bouton radio "Désactiver" est sélectionné
        if self.radioBt_desactiver.isChecked():
            print("Désactiver") # une vérification sur la console que la méthode fonctionne
            self.LEdit_Nombre1.setDisabled(True)
            self.LEdit_Nombre2.setDisabled(True)

    def calculer(self):
        # Effectue un calcul et affiche le résultat
        # on vérifie d'abord que les deux champs ne sont pas vide
        # attention ici il n'y a pas de gestion des erreurs
        if self.LEdit_Nombre1.text() != "" and self.LEdit_Nombre2.text() != "":
            somme = int(self.LEdit_Nombre1.text()) + int(self.LEdit_Nombre2.text())
            print("le texte saisi:", str(somme))
            self.lbl_resultat.setText(str(somme))

    def effacer(self):
        # Réinitialise les zones de texte et l'affichage du résultat
        self.lbl_resultat.setText("....")
        self.LEdit_Nombre1.setText("")
        self.LEdit_Nombre2.setText("")

app = QtWidgets.QApplication([])  # Crée une application Qt
form = MaFenetre()  # Crée une instance de la classe MaFenetre
form.show()  # Affiche la fenêtre
app.exec()  # Exécute l'application
