#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
#from PyQt4 import QtCore, QtGui
from PySide import QtCore, QtGui
from rutinas.varias import *
import os
import recursos
import dbf
#import pdb 

ruta_arch_conf = os.path.dirname(sys.argv[0])
archivo_configuracion = os.path.join(ruta_arch_conf, 'config.conf')
fc = FileConfig(archivo_configuracion)
#pdb.set_trace()


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
        
        #Eventos        
        #self.connect(self.tableWidget, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.clickEnTabla)
        self.connect(self.tableWidget, QtCore.SIGNAL("itemActivated(QTableWidgetItem*)"), self.clickEnTabla)
        self.connect(self.tableWidget, QtCore.SIGNAL("itemEntered(QTableWidgetItem*)"), self.clickEnTabla)
        self.connect(self.tableWidget, QtCore.SIGNAL("itemPressed(QTableWidgetItem*)"), self.clickEnTabla)

        #Iniciar
        self.inicio()

    def inicio(self):
        self.txtCodigoBarra.setFocus()
        self.Buscar()

    def Buscar(self):
        '''
        Metodo que se utiliza para realizar la busqueda segun lo que
        ingresa el usuario en las cajas de texto.
        '''
        #Crear aqui la Cabecera del TableWidget con el Nombre del campo y el Ancho
        listaCabecera = [('Codigo' ,170),
                ('Nombre' ,300),
                ('Descripcion' ,300 )]

        #if self.activarBuscar:
        #cadsq = self.armar_select()
        lista = self.obtenerDatos()  # (cadsq)
        self.PrepararTableWidget(len(lista), listaCabecera)  # Configurar el tableWidget
        self.InsertarRegistros(lista)  # Insertar los Registros en el TableWidget
        self.tableWidget.setCurrentCell(15, 1)
        #self.tableWidget.cellClicked(15, 1)

    def obtenerDatos(self):
        t = 'farmacos.dbf'
        farmacos = dbf.Table(t)
        farmacos.open()
        
        lista = []
        for reg in farmacos:
            c1 = reg[1]
            c2 = reg[8]
            c3 = reg[9]
            registro = '%s, %s, %s' %(c1, c2, c3)
            lista.append((c1, c2, c3))
        return lista

    def PrepararTableWidget(self, cantidadReg = 0, Columnas = []):
        '''
        Parametros pasados (2) (CantidadReg: Entero) y (Columnas :Lista)
        Ej: PrepararTableWidget(50, ['ID', 'FECHA', 'PUERTO'])

        Meotodo que permite asignar y ajustar  las columnas que tendra el tablewidget
        basados en la cantidad de conlumnas y la cantidad de registros que le son
        pasados como parametro
        '''

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 244, 226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)

        brush = QtGui.QBrush(QtGui.QColor(254, 206, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)

        self.tableWidget.setColumnCount(len(Columnas))
        self.tableWidget.setRowCount(cantidadReg)

        #Armar Cabeceras de las Columnas
        cabecera = []
        for f in Columnas:
            nombreCampo = f[0]
            cabecera.append(nombreCampo)

        for f in Columnas:
            posicion = Columnas.index(f)
            nombreCampo = f[0]
            ancho = f[1]
            self.tableWidget.horizontalHeader().resizeSection(posicion, ancho)

        self.tableWidget.setPalette(palette)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setHorizontalHeaderLabels(cabecera)

        self.tableWidget.setSelectionMode(QtGui.QTableWidget.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QTableView.SelectRows)

    def InsertarRegistros(self, cursor):
        '''
        Metodo que permite asignarle registros al tablewidget
        parametros recibitos (1) Tipo (Lista)
        Ej:RowSource(['0', 'Carlos', 'Garcia'], ['1', 'Nairesther', 'Gomez'])
        '''

        ListaCursor = cursor
        for pos, fila in enumerate(ListaCursor):
            for posc, columna in enumerate(fila):
                x = columna.encode('ASCII', 'ignore')
                self.tableWidget.setItem(pos, posc, QtGui.QTableWidgetItem(str(x)))

    def clickEnTabla(self):
        '''
        Este metodo se activa al momento de hace click en el tableWidget y permite
        mostrar el contenido de los campos de la fila seleccionada en el tableWidget
        en los textbox bien sea para Verlos, modificarlos o Eliminarlos
        '''

        #self.activarBuscar = False
        fila = self.tableWidget.currentRow()
        #total_columnas = self.tableWidget.columnCount()

        #Capturar la Fila seleccionada del Table Widget
        twCodigo = self.tableWidget.item(fila, 0).text()
        twNombre = self.tableWidget.item(fila, 1).text()
        twDescripcion = self.tableWidget.item(fila, 2).text()

        #Asignar a los QLineEdit el Valor de la fila del table widget
        self.txtCodigoBarra.setText('')
        self.txtCodigoFarmaco.setText(twCodigo)
        self.txtNombreFarmaco.setText(twNombre)
        self.txtCodigoBarra.setFocus()
        #self.txtDescripcion.setText(twDescripcion)
       #self.cbxTipoContacto.currentText()
       # self.btnModificar.setEnabled(True)
       # self.btnEliminar.setEnabled(True)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    forma = ui_()
    #forma.statusBar().showMessage('Listo')
    forma.show()
    sys.exit(app.exec_())
