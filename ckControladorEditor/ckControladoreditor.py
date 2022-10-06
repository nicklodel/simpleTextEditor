import modappeditor as mapp

def eventEditar(a):
    edit=mapp.showDialog(a)
    return edit
    
def eventGuardar(a):
    save=mapp.file_save(a)
    return save
     
# -*- coding: utf-8 -*-

