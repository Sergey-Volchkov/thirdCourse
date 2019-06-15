# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kis2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStyledItemDelegate

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1169, 843)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 951, 721))
        self.widget.setObjectName("widget")
        self.createTableWidget()
        self.resetColumn()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1000, 30, 111, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)

        self.acceptButton = QtWidgets.QPushButton(self.frame)
        self.acceptButton.setObjectName("acceptButton")
        self.verticalLayout.addWidget(self.acceptButton)

        self.calculateButton = QtWidgets.QPushButton(self.frame)
        self.calculateButton.setObjectName("calculateButton")
        self.verticalLayout.addWidget(self.calculateButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1169, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Размерность NxN:"))
        self.acceptButton.setText(_translate("MainWindow", "Применить"))
        self.calculateButton.setText(_translate("MainWindow", "Рассчитать"))

    def createTableWidget(self):
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 951, 721))
        self.tableWidget.setObjectName("tableWidget")
    def resetColumn(self,n=2):
        self.tableWidget.setColumnCount(n)
        self.tableWidget.setRowCount(n)
        self.tableWidget.resizeColumnsToContents()
