#This is a quote generator app

import sys
import random

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel


def randquotegen():
    msg.setText(str(random.randint(1,100)))
    


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Generate a quote')
layout = QVBoxLayout()

btn = QPushButton('Generate a quote')
btn.clicked.connect(randquotegen)

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())        


