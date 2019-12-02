from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDoubleValidator
import math 

outputTextArea = None
logTextArea = None
inputGroupBox = None
inputGroupBoxLayout = None
doubleValidator = QDoubleValidator()

class triangleUI:
    baseLineEdit = None
    heightLineEdit = None

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def addLogText(str):
    logTextArea.insertPlainText(str)
    logTextArea.verticalScrollBar().setValue(logTextArea.verticalScrollBar().maximum())


def circle(r):
    outputTextArea.insertPlainText('Circle Radius: {}\n'.format(r))

    circumference = r * 2 * math.pi
    outputTextArea.insertPlainText('  Circumference: {}\n'.format(circumference))
    
    area = r * r * math.pi
    outputTextArea.insertPlainText('  Area: {}\n'.format(area))
    
def square(s):

    outputTextArea.insertPlainText('Square Side Length: {}\n'.format(s))

    area = s * s
    outputTextArea.insertPlainText('  Area: {}\n'.format(area))

    perimeter = s * 4
    outputTextArea.insertPlainText('  Perimeter: {}\n'.format(perimeter))
    

def triangle(b, h):

    outputTextArea.insertPlainText('Triangle Base and Height: {}, {}\n'.format(b, h))

    area = b * h / 2
    outputTextArea.insertPlainText('  Area: {}\n'.format(area))

def onRadiusChanged(radiusText):
    outputTextArea.clear()
    if isfloat(radiusText):
        circle(float(radiusText))
        addLogText('Circle, Radius {}\n'.format(float(radiusText)))

def onSideChanged(sideText):
    outputTextArea.clear()
    if isfloat(sideText):
        square(float(sideText))
        addLogText('Square, Side Length {}\n'.format(float(sideText)))

def onTriangleBaseOrHeightChanged(baseText, heightText):
    outputTextArea.clear()
    if isfloat(baseText) and isfloat(heightText):
        
        base = float(baseText)
        height = float(heightText)
        
        triangle(base, height)

        addLogText('Triangle Base and Height: {}, {}\n'.format(base, height))

def onBaseChanged(baseText):
    onTriangleBaseOrHeightChanged(triangleUI.baseLineEdit.text(), triangleUI.heightLineEdit.text())

def onHeightChanged(heightText):
    onTriangleBaseOrHeightChanged(triangleUI.baseLineEdit.text(), triangleUI.heightLineEdit.text())

def onShapeSelected(shape):

    outputTextArea.clear()

    if inputGroupBoxLayout:
        for i in reversed(range(inputGroupBoxLayout.count())): 
            inputGroupBoxLayout.itemAt(i).widget().deleteLater()
        
    if shape == 'circle':
        radiusLabel = QLabel('Radius:', inputGroupBox)
        inputGroupBoxLayout.addWidget(radiusLabel)

        radiusLineEdit = QLineEdit(inputGroupBox)
        radiusLineEdit.setValidator(doubleValidator)
        inputGroupBoxLayout.addWidget(radiusLineEdit)

        radiusLineEdit.textChanged.connect(onRadiusChanged)

    if shape == 'square':
        sideLabel = QLabel('Side:', inputGroupBox)
        inputGroupBoxLayout.addWidget(sideLabel)

        sideLineEdit = QLineEdit(inputGroupBox)
        sideLineEdit.setValidator(doubleValidator)
        inputGroupBoxLayout.addWidget(sideLineEdit)

        sideLineEdit.textChanged.connect(onSideChanged)

    if shape == 'triangle':
        baseLabel = QLabel('Base:', inputGroupBox)
        inputGroupBoxLayout.addWidget(baseLabel)

        triangleUI.baseLineEdit = QLineEdit(inputGroupBox)
        triangleUI.baseLineEdit.setValidator(doubleValidator)
        inputGroupBoxLayout.addWidget(triangleUI.baseLineEdit)

        triangleUI.baseLineEdit.textChanged.connect(onBaseChanged)
  
        heightLabel = QLabel('Height:', inputGroupBox)
        inputGroupBoxLayout.addWidget(heightLabel)

        triangleUI.heightLineEdit = QLineEdit(inputGroupBox)
        triangleUI.heightLineEdit.setValidator(doubleValidator)
        inputGroupBoxLayout.addWidget(triangleUI.heightLineEdit)

        triangleUI.heightLineEdit.textChanged.connect(onHeightChanged)


choices = ['circle', 'square', 'triangle']

app = QApplication([])

window = QMainWindow()
window.resize(800, 600)
window.setWindowTitle('ShapeInfo')

mainWidget = QWidget()
window.setCentralWidget(mainWidget)

layout = QVBoxLayout()

titleLabel = QLabel('Welcome to ShapeInfo Version 0.3.1', mainWidget)
layout.addWidget(titleLabel)

shapeCombo = QComboBox(mainWidget)
shapeCombo.addItems(choices)
layout.addWidget(shapeCombo)

inputGroupBox = QGroupBox(mainWidget)
inputGroupBox.setObjectName('inputGroupBox')
inputGroupBoxLayout = QHBoxLayout(inputGroupBox)
inputGroupBox.setTitle('Input')
layout.addWidget(inputGroupBox)

outputGroupBox = QGroupBox(mainWidget)
outputGroupBox.setTitle('Output')
outputGroupBoxLayout = QVBoxLayout(outputGroupBox)
outputTextArea = QPlainTextEdit(outputGroupBox)
outputTextArea.setReadOnly(True)
outputGroupBoxLayout.addWidget(outputTextArea)
layout.addWidget(outputGroupBox)

logGroupBox = QGroupBox(mainWidget)
logGroupBox.setTitle('Log')
logGroupBoxLayout = QVBoxLayout(logGroupBox)
logTextArea = QPlainTextEdit(logGroupBox)
logTextArea.setReadOnly(True)
logGroupBoxLayout.addWidget(logTextArea)
layout.addWidget(logGroupBox)

shapeCombo.currentTextChanged.connect(onShapeSelected)
onShapeSelected(shapeCombo.currentText())


mainWidget.setLayout(layout)
window.show()

app.exec_()
