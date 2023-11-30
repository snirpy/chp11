from PySide6 import QtWidgets, QtGui

class MainForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QtWidgets.QStackedWidget(self)

        self.main_form = QtWidgets.QWidget()
        self.setup_main_form()

        self.second_form = QtWidgets.QWidget()
        self.setup_second_form()

        self.stacked_widget.addWidget(self.main_form)
        self.stacked_widget.addWidget(self.second_form)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        self.setWindowTitle("Main Form")
        self.setGeometry(100, 100, 400, 200)

    def setup_main_form(self):
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Main Form Content")
        button = QtWidgets.QPushButton("Switch to Second Form")
        button.clicked.connect(self.switch_to_second_form)

        layout.addWidget(label)
        layout.addWidget(button)

        self.main_form.setLayout(layout)

    def switch_to_second_form(self):
        self.stacked_widget.setCurrentIndex(1)

    def setup_second_form(self):
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Second Form Content")
        button = QtWidgets.QPushButton("Switch to Main Form")
        button.clicked.connect(self.switch_to_main_form)

        layout.addWidget(label)
        layout.addWidget(button)

        self.second_form.setLayout(layout)

    def switch_to_main_form(self):
        self.stacked_widget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_form = MainForm()
    main_form.show()
    app.exec()
