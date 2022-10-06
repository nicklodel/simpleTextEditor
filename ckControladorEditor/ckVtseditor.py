from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction)
from PyQt5.QtGui import QIcon
import ckControladoreditor as ctrl

class Editor(QMainWindow):

    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.editarArchivo)
        
        saveFile = QAction(QIcon('save.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save new File')
        saveFile.triggered.connect(self.guardarArchivo)
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        
        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('Editor de textos')
        self.show()


    def editarArchivo(self):
        edit = ctrl.eventEditar(self)
        return edit
    def guardarArchivo(self):
        save = ctrl.eventGuardar(self)
        return save
