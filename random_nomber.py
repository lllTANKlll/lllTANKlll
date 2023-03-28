from PyQt5.QtWidgets import*
from random import*

app = QApplication([])
okno = QWidget()
okno.resize(300,300)


knopka = QPushButton(okno)
knopka.setText("прив")
knopka.move(200,200)
knopka.resize(100,100)

bokvi = QLabel(okno)
bokvi.setText('Щёлк')
bokvi.move(50,50)

def nazal(okno):
    asd = randint(1,100)
    bokvi.setText(str(asd))


knopka.clicked.connect(nazal)



okno.show()
app.exec_()
