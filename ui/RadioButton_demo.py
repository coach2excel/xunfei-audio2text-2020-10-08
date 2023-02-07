import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)


class basicRadiobuttonExample(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Which city do you live in?')
        self.rbtn1 = QRadioButton('New York')
        self.rbtn2 = QRadioButton('Houston')
        self.label2 = QLabel("")

        self.rbtn1.toggled.connect(self.onClicked)
        self.rbtn2.toggled.connect(self.onClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
        layout.addWidget(self.label2)

        self.setGeometry(200, 200, 300, 150)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Radio Button Example')

        self.show()

    def onClicked(self):
        radioBtn = self.sender()
        print(radioBtn.text())#Jet:此法有问题，实际上会调用两次！！！
        if radioBtn.isChecked():
            self.label2.setText("You live in " + radioBtn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = basicRadiobuttonExample()
    sys.exit(app.exec_())
