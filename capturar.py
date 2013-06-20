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

        #Campo Id
        self.vlId = QtGui.QVBoxLayout()
        self.lblId = QtGui.QLabel('ID:')
        self.txtId = miQLineEdit()
        self.vlId.addWidget(self.lblId)
        self.vlId.addWidget(self.txtId)
        
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

        #Campo Descripcion del Farmaco
        self.vlDescripcionFarmaco = QtGui.QVBoxLayout()
        self.lblDescripcionFarmaco = QtGui.QLabel('Descripcion del Farmaco:')
        self.txtDescripcionFarmaco = miQLineEdit()
        self.vlDescripcionFarmaco.addWidget(self.lblDescripcionFarmaco)
        self.vlDescripcionFarmaco.addWidget(self.txtDescripcionFarmaco)

        #Layout Horizontal para los Labels y las Cajas de texto
        self.hlCampos = QtGui.QHBoxLayout()
        self.hlCampos.addLayout(self.vlId)
        self.hlCampos.addLayout(self.vlCodigoBarra)
        self.hlCampos.addLayout(self.vlCodigoFarmaco)
        self.hlCampos.addLayout(self.vlNombreFarmaco)
        self.hlCampos.addLayout(self.vlDescripcionFarmaco)

        #La Tabla
        self.tableWidget = QtGui.QTableWidget()

        #Se insertan los Objetos en el Grid Loyouts de todo el Formulario
        self.gl = QtGui.QGridLayout()
        self.gl.addLayout(self.hlBotones, 0, 1, 1, 8)
        self.gl.addWidget(self.line, 1, 1, 1, 8)
        self.gl.addLayout(self.hlCampos, 2, 1, 1, 8)
        self.gl.addWidget(self.tableWidget, 3, 1, 1, 8)

        self.setGeometry(10, 10, 1015, 500)
        self.setLayout(self.gl)
        
        #Eventos de los Botones.
        self.connect(self.btnLimpiar, QtCore.SIGNAL("clicked()"), self.limpiarText)
        
        #Eventos de la Tabla
        self.connect(self.tableWidget, QtCore.SIGNAL("itemClicked(QTableWidgetItem*)"), self.clickEnTabla)
        
        #Eventos de los QLineEdit
        #self.connect(self.txtCodigoBarra, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtCodigoFarmaco, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtNombreFarmaco, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        self.connect(self.txtDescripcionFarmaco, QtCore.SIGNAL("textChanged(QString)"), self.Buscar)
        
        #Iniciar
        self.inicio()

    def inicio(self):
        ''' '''
        host,  db, user, clave = fc.opcion_consultar('POSTGRESQL')
        self.cadconex = "host='%s' dbname='%s' user='%s' password='%s'" % (host[1], db[1], user[1], clave[1])

        self.txtCodigoBarra.setFocus()
        self.iniciarForm()
        self.Buscar()
    
    def iniciarForm(self):
        '''
        '''

        #Habilitar el QLineEdit del ID  y el TableWidget ya que
        #el boton nuevo los deshabilita
        self.txtId.setEnabled(False)
        self.tableWidget.setEnabled(True)

        #Activar la Busqueda al escribir el los textbox
        self.activarBuscar = True

        #Activar Bandera para saber cuando el boton Nuevo funciona como Boton Nuevo
        #self.banderaNuevo = True
        #self.banderaModificar = True

        #Deshabilitar y Habilitar botones
        #self.btnNuevo.setEnabled(True)
        #self.btnModificar.setEnabled(False)
        #self.btnEliminar.setEnabled(False)
        #self.btnLimpiar.setEnabled(True)
        #self.btnDeshacer.setEnabled(False)
        #self.btnExportar.setEnabled(True)
        #self.btnSalir.setEnabled(True)

        #Cambiar el Caption o Text del Boton
        #self.btnNuevo.setText("&Nuevo")
        #self.btnModificar.setText('&Modificar')

        #Cambiar icono del Boton Nuevo por Nuevo
        #icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap(":/img/30px_Crystal_Clear_app_List_manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.btnNuevo.setIcon(icon1)

        #Cambiar icono del Boton Modificar por Modificar
        #icon2 = QtGui.QIcon()
        #icon2.addPixmap(QtGui.QPixmap(":/img/40px_Crystal_Clear_app_kedit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.btnModificar.setIcon(icon2)

    def Buscar(self):
        '''
        Metodo que se utiliza para realizar la busqueda segun lo que
        ingresa el usuario en las cajas de texto.
        '''
        #Crear aqui la Cabecera del TableWidget con el Nombre del campo y el Ancho
        listaCabecera = [('id', 80), 
                ('CodigoBarra' ,170),
                ('Codigo' ,170),
                ('Nombre' ,300),
                ('Descripcion' ,300 )]

        if self.activarBuscar:
            cadsq = self.armar_select()
            lista = self.obtenerDatos(cadsq)
            self.PrepararTableWidget(len(lista), listaCabecera)  # Configurar el tableWidget
            self.InsertarRegistros(lista)  # Insertar los Registros en el TableWidget
            #self.tableWidget.setCurrentCell(15, 1)
            #self.tableWidget.cellClicked(15, 1)

    def armar_select(self):
        '''
        Metodo que permite armar la consulta select a medida que el usuario
        va tecleando en los textbox
        Parametro devuelto(1) String con la cadena sql de busqueda
        '''

        #Campturar lo que tienne los LineEdit
        lcId = self.txtId.text()
        lcCodigoBarra = self.txtCodigoBarra.text()
        lcCodigoFarmaco = self.txtCodigoFarmaco.text()
        lcNombreFarmaco = self.txtNombreFarmaco.text()
        lcDescripcionFarmaco = self.txtDescripcionFarmaco.text()

        vId  = " Id = {0} AND ".format(lcId) if lcId else ''
        vCodigoBarra  = " codigobarra = '{0}' AND ".format(lcCodigoBarra) if lcCodigoBarra else ''
        vCodigoFarmaco = " cod_far like '%{0}%' AND ".format(lcCodigoFarmaco) if lcCodigoFarmaco else ''
        vNombreFarmaco = " nom_far like '%{0}%' AND ".format(lcNombreFarmaco) if lcNombreFarmaco else ''
        vDescripcionFarmaco = " des_pre like '%{0}%' AND ".format(lcDescripcionFarmaco) if lcDescripcionFarmaco else ''

        campos = vId + vCodigoBarra + vCodigoFarmaco + vNombreFarmaco + vDescripcionFarmaco
        camposConWhere = " where {0} ".format(campos[:-4]) if campos else ''

        cadenaSql = '''select id, codigobarra, cod_far, nom_far, des_pre from codigob.farmacos {0}'''.format(camposConWhere)
        return cadenaSql

    def obtenerDatos(self, cadena_pasada):
        '''
        Ejecuta la Consulta SQl a el servidor PostGreSQL segun la cadena SQL
        pasada como parametro
        parametros recibidos: (1) String
        parametros devueltos: (1) Lista
        Ej: obtener_datos('select *from tabla where condicion')
        '''

        try:
            pg = ConectarPG(self.cadconex)
            self.registros = pg.ejecutar(cadena_pasada)
            pg.cur.close()
            pg.conn.close()
        except:
            self.registros = []
        return self.registros

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
                x = columna  # columna.encode('ASCII', 'ignore')
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
        twId = self.tableWidget.item(fila, 0).text()
        twCodigoBarra = self.tableWidget.item(fila, 1).text()
        twCodigo = self.tableWidget.item(fila, 2).text()
        twNombre = self.tableWidget.item(fila, 3).text()
        twDescripcion = self.tableWidget.item(fila, 4).text()

        #Asignar a los QLineEdit el Valor de la fila del table widget
        self.txtId.setText(twId)
        cb = '' if 'None' in twCodigoBarra else twCodigoBarra
        self.txtCodigoBarra.setText(cb)
        self.txtCodigoFarmaco.setText(twCodigo)
        self.txtNombreFarmaco.setText(twNombre)
        self.txtDescripcionFarmaco.setText(twDescripcion)
        self.txtCodigoBarra.setFocus()

    def limpiarText(self):
        '''
        Limpia los QlineEdit o Textbox
        '''
        self.txtId.clear()
        self.txtCodigoBarra.clear()
        self.txtCodigoFarmaco.clear()
        self.txtNombreFarmaco.clear()
        self.txtDescripcionFarmaco.clear()
        self.iniciarForm()
        self.txtCodigoBarra.setFocus()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    forma = ui_()
    #forma.statusBar().showMessage('Listo')
    forma.show()
    sys.exit(app.exec_())
