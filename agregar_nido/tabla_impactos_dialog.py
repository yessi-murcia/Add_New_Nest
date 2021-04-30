# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabla_impactos.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.tbl = QtWidgets.QTableWidget(Dialog)
        self.tbl.setGeometry(QtCore.QRect(10, 10, 371, 271))
        self.tbl.setAlternatingRowColors(True)
        self.tbl.setObjectName("tbl")
        self.tbl.setColumnCount(3)
        self.tbl.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tabla de Impactos"))
        item = self.tbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Proyecto"))
        item = self.tbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tipo"))
        item = self.tbl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Distancia"))

