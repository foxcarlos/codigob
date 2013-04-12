# -*- coding: utf-8 -*-

import sys
#from PyQt4 import QtCore, QtGui
from PySide import QtCore, QtGui
from rutinas.varias import *
import os
import recursos

ruta_arch_conf = os.path.dirname(sys.argv[0])
archivo_configuracion = os.path.join(ruta_arch_conf, 'config.conf')
fc = FileConfig(archivo_configuracion)


class miQLineEdit(QtGui.QLineEdit):
    def __init__(self):
        super(miQLineEdit, self).__init__()
        self.foreColor()
        self.backColor()
        self.tag = ''
        self.listaAutoC = ''
        self.completer = ''

    def autoCompletado(self, lista):
        '''
        Este metodo permite iniciar el autocompletado en el QlineEdit.
        Ej: autoCompletado([('Carlos',),  ('Nairesther',), ( 'Paola',), ( Carla,)])

        Parametro recibidos 1:
        1-) Tipo Lista, La lista que se desea mostrar en el autocompletado
       '''
        self.listaPalabras = [f[0] for f in lista]
        completer = QtGui.QCompleter(self.listaPalabras, self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setCompleter(completer)
        self.listaAutoC = lista
        self.completer = completer

    '''
    def focusOutEvent(self, event):
        print 'lostfocus'
        return

    def focusInEvent(self, event):
        print 'GoFocus'
        return
    '''

    def foreColor(self, color = QtGui.QColor(0, 0, 0)):
        paletteC = QtGui.QPalette()
        paletteC.setColor(QtGui.QPalette.Active, QtGui.QPalette.Text, color)
        self.setPalette(paletteC)

    def backColor(self, color = QtGui.QColor(254, 230, 150)):
        paletteB = QtGui.QPalette()
        paletteB.setColor(QtGui.QPalette.Active, QtGui.QPalette.Base, color)
        self.setPalette(paletteB)

class ui_(QtGui.QWidget):
    def __init__(self):
        super(ui_, self).__init__()
        #Se crean los Botones de mantenimiento superiores

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(228, 247, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
        #self.statusBar().showMessage("Listo")

        self.btnGuardar = QtGui.QPushButton()
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/img/40px_3floppy_unmount.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnGuardar.setIcon(icon12)
        self.btnGuardar.setText('&Guardar')

        self.btnLimpiar = QtGui.QPushButton()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/erase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon5)
        self.btnLimpiar.setText(' &Limpiar ')

        self.btnSalir = QtGui.QPushButton()
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/25px_exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalir.setIcon(icon7)
        self.btnSalir.setText('  &Salir  ')

        #Crear un Espacio entre Objetos con SpaceItem
        spacerItem1 = QtGui.QSpacerItem(400, 20)

        #Se crea un Layout Horizontal para los Botones
        self.hlBotones = QtGui.QHBoxLayout()

        #Agregar los Botones superiores al Layout Horizontal
        self.hlBotones.addWidget(self.btnGuardar)
        self.hlBotones.addWidget(self.btnLimpiar)
        self.hlBotones.addItem(spacerItem1)  # Insertar un spaceIntem entre los Botones
        self.hlBotones.addWidget(self.btnSalir)

        #Se Crea la Linea Horizontal que estara debajo de los Botones Superiores
        self.line = QtGui.QFrame()
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)

        '''Aqui se crean las Etiquetas y las cajas de Edicion'''

        #Definir los Colores de Texto y de Fondo de los QLineEdit
        self.colorTexto = QtGui.QColor(0, 0, 0)
        self.colorFondo = QtGui.QColor(254, 230, 150)
        palette = QtGui.QPalette()

        #Campo Codigo de Barra
        self.vlCodigoBarra = QtGui.QVBoxLayout()
        self.lblCodigoBarra = QtGui.QLabel('Codigo de Barra:')
        self.txtCodigoBarra = miQLineEdit()
        self.vlCodigoBarra.addWidget(self.lblCodigoBarra)
        self.vlCodigoBarra.addWidget(self.txtCodigoBarra)

        #Campo Codigo de Farmaco
        self.vlCodigoFarmaco = QtGui.QVBoxLayout()
        self.lblCodigoFarmaco = QtGui.QLabel('Codigo del Farmaco:')
        self.txtCodigoFarmaco = miQLineEdit()
        self.vlCodigoFarmaco.addWidget(self.lblCodigoFarmaco)
        self.vlCodigoFarmaco.addWidget(self.txtCodigoFarmaco)

        #Campo Nombre de Farmaco
        self.vlNombreFarmaco = QtGui.QVBoxLayout()
        self.lblNombreFarmaco = QtGui.QLabel('Nombre del Farmaco:')
        self.txtNombreFarmaco = miQLineEdit()
        self.vlNombreFarmaco.addWidget(self.lblNombreFarmaco)
        self.vlNombreFarmaco.addWidget(self.txtNombreFarmaco)

        #Layout Horizontal para los Labels y las Cajas de texto
        self.hlCampos = QtGui.QHBoxLayout()
        self.hlCampos.addLayout(self.vlCodigoBarra)
        self.hlCampos.addLayout(self.vlCodigoFarmaco)
        self.hlCampos.addLayout(self.vlNombreFarmaco)

        #La Tabla
        self.tableWidget = QtGui.QTableWidget()

        #Se insertan los Objetos en el Grid Loyouts de todo el Formulario
        self.gl = QtGui.QGridLayout()
        self.gl.addLayout(self.hlBotones, 0, 1, 1, 8)
        self.gl.addWidget(self.line, 1, 1, 1, 8)
        self.gl.addLayout(self.hlCampos, 2, 1, 1, 8)
        self.gl.addWidget(self.tableWidget, 3, 1, 1, 8)

        self.setGeometry(10, 10, 880, 500)
        self.setLayout(self.gl)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    forma = ui_()
    #forma.statusBar().showMessage('Listo')
    forma.show()
    sys.exit(app.exec_())
