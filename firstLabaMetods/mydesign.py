# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *
from insertRowDialog import Form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1133, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1133, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(980, 10, 140, 176))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.deliveryTimeSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.deliveryTimeSpinBox.setMaximum(1.0)
        self.deliveryTimeSpinBox.setSingleStep(0.01)
        self.deliveryTimeSpinBox.setProperty("value", 1.0)
        self.deliveryTimeSpinBox.setObjectName("deliveryTimeSpinBox")
        self.gridLayout.addWidget(self.deliveryTimeSpinBox, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.reviewSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.reviewSpinBox.setMaximum(1.0)
        self.reviewSpinBox.setSingleStep(0.01)
        self.reviewSpinBox.setProperty("value", 1.0)
        self.reviewSpinBox.setObjectName("reviewSpinBox")
        self.gridLayout.addWidget(self.reviewSpinBox, 5, 0, 1, 1)
        self.priceSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.priceSpinBox.setMaximum(1.0)
        self.priceSpinBox.setSingleStep(0.01)
        self.priceSpinBox.setProperty("value", 1.0)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.gridLayout.addWidget(self.priceSpinBox, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.yearsSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.yearsSpinBox.setMaximum(1.0)
        self.yearsSpinBox.setSingleStep(0.01)
        self.yearsSpinBox.setProperty("value", 1.0)
        self.yearsSpinBox.setObjectName("yearsSpinBox")
        self.gridLayout.addWidget(self.yearsSpinBox, 7, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 964, 533))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setDatabaseName("laba1")
        self.db.setUserName("root")
        self.db.setPassword("")
        self.db.open()
        self.sqlRelationalTable = QSqlRelationalTableModel(self.widget, db=self.db)
        self.sqlRelationalTable.setObjectName("sqlRelationalTable")
        self.sqlRelationalTable.setTable("seller")  # здесь выбираем таблицу для отображения
        # self.sqlRelationalTable.setFilter("") #пишем фильтр, аля  id =1
        self.sqlRelationalTable.setEditStrategy(
            QSqlTableModel.OnManualSubmit)  # применяем изменения только при использовании submitAll() или отменяем при revertAll()

        # self.sqlRelationalTable.removeColumn(0)

        self.setNameColumn()
        self.sqlRelationalTable.select()

        self.view = QtWidgets.QTableView()
        self.view.setSortingEnabled(True)
        self.view.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.view.setModel(self.sqlRelationalTable)
        self.view.setColumnWidth(1,200)
        # self.view.setColumnWidth(3,150)
        self.view.setColumnWidth(4,120)
        self.view.setColumnWidth(5,170)
        self.view.setColumnHidden(0, True)

        self.gridLayout_3.addWidget(self.view, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 3)

        self.refreshButton = QtWidgets.QPushButton(self.widget)
        self.refreshButton.setMinimumSize(QtCore.QSize(90, 0))
        self.refreshButton.setObjectName("refreshButton")
        self.gridLayout_2.addWidget(self.refreshButton, 1, 0, 1, 1)
        self.addButton = QtWidgets.QPushButton(self.widget)
        self.addButton.setMinimumSize(QtCore.QSize(90, 0))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.addRowButton)

        self.gridLayout_2.addWidget(self.addButton, 1, 1, 1, 1)
        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setMinimumSize(QtCore.QSize(90, 0))
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.deleteRowButton)

        self.gridLayout_2.addWidget(self.deleteButton, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа Аф"))
        self.label_4.setText(_translate("MainWindow", "Лет на рынке"))
        self.label.setText(_translate("MainWindow", "Цена"))
        self.label_2.setText(_translate("MainWindow", "Время доставки"))
        self.label_3.setText(_translate("MainWindow", "Отзывы"))
        self.refreshButton.setText(_translate("MainWindow", "Обновить"))
        self.addButton.setText(_translate("MainWindow", "Добавить"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))

    def addRowButton(self):
        try:
            form = Form(self.sqlRelationalTable)
            form.show()
            self.chosen_action = form.exec_()

            # Шаблон для совершения действия по слоту accepted от соответствущей клавиши в Dialog
            # print('vaffff')
            # if self.chosen_action == QtWidgets.QDialog.Accepted:
            #     print('VAF')
            #     form.acc()
        except Exception as e:
            print(e)

    def deleteRowButton(self):
            rows = set()
            for index in self.view.selectedIndexes():
                rows.add(index.row())
            for element in rows:
                self.sqlRelationalTable.removeRow(element)
            self.sqlRelationalTable.submitAll()
    def setNameColumn(self):
        self.sqlRelationalTable.setHeaderData(0, QtCore.Qt.Horizontal, 'ID')
        self.sqlRelationalTable.setHeaderData(1, QtCore.Qt.Horizontal, "Название")
        self.sqlRelationalTable.setHeaderData(2, QtCore.Qt.Horizontal, "Адрес")
        self.sqlRelationalTable.setHeaderData(3, QtCore.Qt.Horizontal, "Лет на рынке")
        self.sqlRelationalTable.setHeaderData(4, QtCore.Qt.Horizontal, "Рейтинг по отзывам")
        self.sqlRelationalTable.setHeaderData(5, QtCore.Qt.Horizontal, "Время доставки(дни)")
        self.sqlRelationalTable.setHeaderData(7, QtCore.Qt.Horizontal, "Цена")
        self.sqlRelationalTable.setRelation(6, QSqlRelation("product", 'id', 'name'))
        self.sqlRelationalTable.setHeaderData(6, QtCore.Qt.Horizontal, "Продукт")
    # Оставлю шаблон для контекстного меню
    # def openMenu(self, position):
    #     try:
    #         menu = QtWidgets.QMenu()
    #         addRow = QtWidgets.QAction('Добавить информацию', menu)
    #         removeRow = QtWidgets.QAction('Удалить информацию', menu)
    #         addRow.triggered.connect(self.addRow)
    #         menu.addAction(addRow)
    #         menu.addAction(removeRow)
    #         menu.exec_(self.view.viewport().mapToGlobal(position))
    #     except:
    #         self. warningDialog = QtWidgets.QDialog()

    # boxSource = QtWidgets.QVBoxLayout()
    # self.view.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    # self.view.customContextMenuRequested.connect(self.openMenu)
    # boxSource.addWidget(self.view)