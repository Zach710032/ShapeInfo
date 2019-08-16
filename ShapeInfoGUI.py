from PyQt5.QtWidgets import *
import math 


choices = ['circle', 'square', 'triangle']

app = QApplication([])

window = QMainWindow()
window.resize(800, 600)
window.setWindowTitle('ShapeInfo')

mainWidget = QWidget()
window.setCentralWidget(mainWidget)

layout = QVBoxLayout()

titleLabel = QLabel('Welcome to ShapeInfo Version 1.0', mainWidget)
layout.addWidget(titleLabel)

shapeCombo = QComboBox(mainWidget)
shapeCombo.addItems(choices)
layout.addWidget(shapeCombo)

inputGroupBox = QGroupBox(mainWidget)
inputGroupBox.setTitle('Input')
layout.addWidget(inputGroupBox)

outputGroupBox = QGroupBox(mainWidget)
outputGroupBox.setTitle('Output')
outputGroupBoxLayout = QVBoxLayout(outputGroupBox)
outputTextArea = QPlainTextEdit(outputGroupBox)
outputGroupBoxLayout.addWidget(outputTextArea)
layout.addWidget(outputGroupBox)

logGroupBox = QGroupBox(mainWidget)
logGroupBox.setTitle('Log')
logGroupBoxLayout = QVBoxLayout(logGroupBox)
logTextArea = QPlainTextEdit(logGroupBox)
logGroupBoxLayout.addWidget(logTextArea)
layout.addWidget(logGroupBox)


def circle(r):
    outputTextArea.insertPlainText('Circle Radius: {}'.format(r))

    circumference = r * 2 * math.pi
    outputTextArea.insertPlainText('  Circumference: {}'.format(circumference))
    
    area = r * r * math.pi
    outputTextArea.insertPlainText('  Area: {}'.format(area))


    
def square(s):

    outputTextArea.insertPlainText('Square Side Length: {}'.format(s))

    area = s * s
    outputTextArea.insertPlainText('  Area: {}'.format(area))

    perimeter = s * 4
    outputTextArea.insertPlainText('  Perimeter: {}'.format(perimeter))


    
    
def onRadiusChanged(radiusText):
    outputTextArea.clear()
    circle(float(radiusText))
    logTextArea.insertPlainText('Circle, Radius {}'.format(radiusText))

    

def onSideChanged(sideText):
    outputTextArea.clear()
    square(float(sideText))
    logTextArea.insertPlainText('Square, Side Length {}'.format(sideText))
    
    


def onShapeSelected(shape):
    
    if inputGroupBox.layout():
        for i in reversed(range(inputGroupBox.layout().count())): 
            inputGroupBox.layout().itemAt(i).widget().deleteLater()
        inputGroupBox.layout().deleteLater()
        
    if shape == 'circle':
        layout = QHBoxLayout(inputGroupBox)
        
        radiusLabel = QLabel('Radius:', inputGroupBox)
        layout.addWidget(radiusLabel)

        radiusLineEdit = QLineEdit(inputGroupBox)
        layout.addWidget(radiusLineEdit)

        radiusLineEdit.textChanged.connect(onRadiusChanged)

    if shape == 'square':
        layout = QHBoxLayout(inputGroupBox)
        
        sideLabel = QLabel('Side:', inputGroupBox)
        layout.addWidget(sideLabel)

        sideLineEdit = QLineEdit(inputGroupBox)
        layout.addWidget(sideLineEdit)

        sideLineEdit.textChanged.connect(onSideChanged)



shapeCombo.currentTextChanged.connect(onShapeSelected)
onShapeSelected(shapeCombo.currentText())


mainWidget.setLayout(layout)
window.show()

app.exec_()
