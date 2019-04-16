# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertRowDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog, sqlRelationalTable):
        self.sqlRelationalTable = sqlRelationalTable
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 435)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 382, 326))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLabel(self.layoutWidget)
        self.name.setEnabled(True)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.nameEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setMinimumSize(QtCore.QSize(380, 30))
        self.nameEdit.setMaximumSize(QtCore.QSize(380, 30))
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout.addWidget(self.nameEdit)
        self.address = QtWidgets.QLabel(self.layoutWidget)
        self.address.setObjectName("address")
        self.verticalLayout.addWidget(self.address)
        self.addressEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressEdit.sizePolicy().hasHeightForWidth())
        self.addressEdit.setSizePolicy(sizePolicy)
        self.addressEdit.setMinimumSize(QtCore.QSize(380, 30))
        self.addressEdit.setMaximumSize(QtCore.QSize(380, 30))
        self.addressEdit.setObjectName("addressEdit")
        self.verticalLayout.addWidget(self.addressEdit)
        self.years = QtWidgets.QLabel(self.layoutWidget)
        self.years.setObjectName("years")
        self.verticalLayout.addWidget(self.years)
        self.yearsEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearsEdit.sizePolicy().hasHeightForWidth())
        self.yearsEdit.setSizePolicy(sizePolicy)
        self.yearsEdit.setMinimumSize(QtCore.QSize(380, 30))
        self.yearsEdit.setMaximumSize(QtCore.QSize(380, 30))
        self.yearsEdit.setObjectName("yearsEdit")
        self.verticalLayout.addWidget(self.yearsEdit)
        self.rating = QtWidgets.QLabel(self.layoutWidget)
        self.rating.setObjectName("rating")
        self.verticalLayout.addWidget(self.rating)
        self.ratingEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ratingEdit.sizePolicy().hasHeightForWidth())
        self.ratingEdit.setSizePolicy(sizePolicy)
        self.ratingEdit.setMinimumSize(QtCore.QSize(380, 30))
        self.ratingEdit.setMaximumSize(QtCore.QSize(380, 30))
        self.ratingEdit.setObjectName("ratingEdit")
        self.verticalLayout.addWidget(self.ratingEdit)
        self.price = QtWidgets.QLabel(self.layoutWidget)
        self.price.setObjectName("price")
        self.verticalLayout.addWidget(self.price)
        self.priceEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceEdit.sizePolicy().hasHeightForWidth())
        self.priceEdit.setSizePolicy(sizePolicy)
        self.priceEdit.setMinimumSize(QtCore.QSize(380, 30))
        self.priceEdit.setMaximumSize(QtCore.QSize(380, 30))
        self.priceEdit.setObjectName("priceEdit")
        self.verticalLayout.addWidget(self.priceEdit)
        self.delivery = QtWidgets.QLabel(self.layoutWidget)
        self.delivery.setObjectName("delivery")
        self.verticalLayout.addWidget(self.delivery)
        self.deliveryEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deliveryEdit.sizePolicy().hasHeightForWidth())
        self.deliveryEdit.setSizePolicy(sizePolicy)
        self.deliveryEdit.setMinimumSize(QtCore.QSize(380, 30))
        self.deliveryEdit.setMaximumSize(QtCore.QSize(380, 30))
        self.deliveryEdit.setObjectName("deliveryEdit")
        self.verticalLayout.addWidget(self.deliveryEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 380, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name.setText(_translate("Dialog", "Название компании"))
        self.address.setText(_translate("Dialog", "Адрес"))
        self.years.setText(_translate("Dialog", "Лет на рынке"))
        self.rating.setText(_translate("Dialog", "Рейтинг по отзывам"))
        self.price.setText(_translate("Dialog", "Цена"))
        self.delivery.setText(_translate("Dialog", "Доставка"))

    def accept(self):
        try:
            self.query = QSqlQuery()
            __check_digital = [self.nameEdit.toPlainText(), self.addressEdit.toPlainText(),
                               self.deliveryEdit.toPlainText().isdigit(), self.yearsEdit.toPlainText().isdigit(),
                               self.ratingEdit.toPlainText().isdigit(), self.priceEdit.toPlainText().isdigit()]
            if all(__check_digital):
                if int(self.deliveryEdit.toPlainText()) > 0 and int(self.yearsEdit.toPlainText()) > 0 and int(
                        self.ratingEdit.toPlainText()) > 0 and int(self.priceEdit.toPlainText()) > 0:
                    nameEdit = self.nameEdit.toPlainText()
                    addressEdit = self.addressEdit.toPlainText()
                    yearsEdit = int(self.yearsEdit.toPlainText())
                    ratingEdit = int(self.ratingEdit.toPlainText())
                    priceEdit = int(self.priceEdit.toPlainText())
                    deliveryEdit = int(self.deliveryEdit.toPlainText())
                    print(nameEdit,addressEdit,yearsEdit,ratingEdit,priceEdit,deliveryEdit)
                    print(self.query.exec_("""insert into `seller` (`name`,`address`,`delivery_days`,`rating`,`yearsOnTheMarket`,`product_id`,`price_rub`) \
                    values('{0}','{1}',{2},{3},{4},3, {5});""".format(nameEdit, addressEdit, deliveryEdit, ratingEdit,
                                                                  yearsEdit, priceEdit)))
                    print('Выполнили запрос в бд')
                    self.sqlRelationalTable.select()
            else:
                self.showdialog()
        except Exception as e:
            print(e)

    def showdialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Алярм!")
        msg.setInformativeText(
            "Кажется, вы ввели неверную информацию для одного или нескольких полей. Помните, что каждое поле должно быть заполнено подходящим типом данных!")
        msg.setWindowTitle("ВАРНИНГ!!!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # msg.buttonClicked.connect(QtWidgets.msgbtn)

        retval = msg.exec_()


class Form(QtWidgets.QDialog):
    def __init__(self, sqlRelationalTable, parent=None, ):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        self.uiD = Ui_Dialog()
        self.uiD.setupUi(self, sqlRelationalTable)
        print(self.accept())
        self.uiD.buttonBox.accepted.connect(self.uiD.accept)
        self.uiD.buttonBox.rejected.connect(self.close)
