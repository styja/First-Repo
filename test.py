# Import Modlues
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

# Main 
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Text")
main_window.resize(300, 200)

# Create All Obejcts
title = QLabel("Random Keywords")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("click me")
button2 = QPushButton("click me") 
button3 = QPushButton("click me")

# Design
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
# 
row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

# Events
def test_function(): 
    print("This button is working!")
    
# Show/ Run app
main_window.show()
app.exec()