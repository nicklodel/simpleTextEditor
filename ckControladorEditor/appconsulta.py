import sys
from PyQt5 import QtWidgets
import ckVtseditor as vts

app = QtWidgets.QApplication(sys.argv) #Crea una aplicacion
form = vts.Editor() #Crea una instancia del formulario
sys.exit(app.exec_()) # -*- coding: utf-8 -*-

