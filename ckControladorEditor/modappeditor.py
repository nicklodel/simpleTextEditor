
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from pathlib import Path

def file_save(a):
     home_dir = str(Path.home())
     fname = QFileDialog.getSaveFileName(a, 'Save File', home_dir)
     if fname[0]:
            f = open(fname[0], 'w')

            with f:
                text = a.textEdit.toPlainText()
                f.write(text)
                f.close()
    
    
    
def showDialog(a):
    
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(a, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                a.textEdit.setText(data)
                f.close()