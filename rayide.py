# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/philippeoz/RayIDE/rayide.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os, syntax

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_rayide(object):
    file_path = ""

    def setupUi(self, rayide):
        rayide.setObjectName(_fromUtf8("rayide"))
        rayide.resize(560, 397)
        self.gridLayout_2 = QtGui.QGridLayout(rayide)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(rayide)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_2.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(rayide)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_3.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/save.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtGui.QPushButton(rayide)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/run.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(rayide)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        
        self.textEdit = QtGui.QTextEdit(self.splitter)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setFontFamily("Monospace")

        palette = self.textEdit.palette()
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor("black"))
        self.textEdit.setPalette(palette)

        palette = self.textEdit.palette()
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Text, QtGui.QColor("white"))
        self.textEdit.setPalette(palette)

        
                
        self.plainTextEdit = QtGui.QTextEdit(self.splitter)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit.setFontFamily("Monospace")

        palette = self.plainTextEdit.palette()
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor("black"))
        self.plainTextEdit.setPalette(palette)

        palette = self.plainTextEdit.palette()
        palette.setColor(QtGui.QPalette.Active, QtGui.QPalette.Text, QtGui.QColor("lightGreen"))
        self.plainTextEdit.setPalette(palette)

        self.verticalLayout.addWidget(self.splitter)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.plainTextEdit.setReadOnly(True)

        QtCore.QObject.connect(self.pushButton_3,QtCore.SIGNAL("clicked()"),self.save_clicked)
        QtCore.QObject.connect(self.pushButton_2,QtCore.SIGNAL("clicked()"),self.open_clicked)
        QtCore.QObject.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.run_clicked)

        QtCore.QMetaObject.connectSlotsByName(rayide)

    def open_clicked(self):
        self.file_path = QtGui.QFileDialog.getOpenFileName(filter='Arquivos Portugol (*.por)', caption='Abrir Arquivo Portugol')
        if self.file_path[-4:] == '.por':
            file_por = open(self.file_path, 'r')
            code_text = file_por.read()
            file_por.close()
            self.textEdit.setText(code_text)

    def run_clicked(self):
        result = ''
        if self.file_path != "" and os.path.isfile(self.file_path):
            self.save_clicked()
            result = os.popen("python3.5 run.py "+self.file_path).read()
            if result == '':
                result = 'Nenhum erro encontrado.'
            self.plainTextEdit.setPlainText(result)

    def save_clicked(self):
        result = ''
        if self.file_path != "" and os.path.isfile(self.file_path):
            file_por = open(self.file_path, 'w')
            file_por.write(self.textEdit.toPlainText())
            file_por.close()
        else:
            self.file_path = QtGui.QFileDialog.getSaveFileName(filter='Arquivos Portugol (*.por)', caption='Salvar Arquivo Portugol')
            print(name)
            if self.file_path:
                file_por = open(self.file_path,'w')
                text = self.textEdit.toPlainText()
                file_por.write(text)
                file_por.close()
            else:
                return

    def retranslateUi(self, rayide):
        rayide.setWindowTitle(_translate("RayIDE", "RayIDE", None))

