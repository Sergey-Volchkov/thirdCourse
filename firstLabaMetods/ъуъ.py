from PyQt5 import QtWidgets
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
# sys.path.insert(0, 'C:\Program Files\MySQL\MySQL Server 8.0\lib')
# sys.path.insert(0, 'C:\Program Files\MySQL\Connector C++ 8.0\lib64')
# sys.path.insert(0, 'C:\Program Files\MySQL\MySQL Router 8.0\lib')
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation
from PyQt5.QtCore import *
from PyQt5.QtSql import QSqlTableModel
import pymysql.cursors


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.refreshButton.clicked.connect(self.btnClicked)

    # def btnClicked(self):
    #     self.ui.label.setText("Вы нажали на кнопку!")
    #     # Если не использовать, то часть текста исчезнет.
    #     self.ui.label.adjustSize()

    def btnClicked(self):
        try:
            self.ui.sqlRelationalTable.setSort(7, Qt.AscendingOrder)  # Qt.DescendingOrder сортировка в обратном порядке
            self.max_ = 'max'
            self.min_ = 'min'

            # self.query.exec("""SELECT seller.`id`,seller.`price_rub` from seller ORDER BY seller.`price_rub` ASC""")

            # Шаблон для максимальный-лучший рейтинга
            # self.max_price = self.maxmin(max_,'seller.`price_rub`')
            # print(self.max_price)
            # self.price_rating_per_one = self.max_price / 100 * float(self.ui.priceSpinBox.text().replace(',', '.'))
            # print(self.price_rating_per_one)
            # self.query.exec("""SELECT seller.`id`,seller.`price_rub` from seller """)
            # while self.query.next():
            #     print(self.query.value(0), round(int(self.query.value(1)) / self.price_rating_per_one,2))

            # Шаблон для минимальный-лучший рейтинга
            # self.min_price = self.maxmin(min_,'seller.`price_rub`')
            # print(self.min_price)
            # self.price_rating_per_one = self.min_price*float(self.ui.priceSpinBox.text().replace(',','.'))
            # print(self.price_rating_per_one)
            # self.query.exec("""SELECT seller.`id`,seller.`price_rub` from seller """)
            # while self.query.next():
            #     print(self.query.value(0),round(self.price_rating_per_one/int(self.query.value(1))*100, 2))

            self.criterion_dict = {}
            self.final_rating = {}

            self.query = QSqlQuery()
            self.query.exec("""SELECT seller.`id` from seller""")
            while self.query.next():
                self.criterion_dict[(self.query.value(0))] = {}

            self.min_rating('price_rub', self.ui.priceSpinBox)
            self.max_rating('yearsOnTheMarket', self.ui.yearsSpinBox)
            self.max_rating('rating', self.ui.reviewSpinBox)
            self.min_rating('delivery_days', self.ui.deliveryTimeSpinBox)
            # print(self.criterion_dict)
            for key, item in self.criterion_dict.items():
                i = 0
                for k, _ in item.items():
                    print(k, _)
                    i += _
                self.final_rating[key] = round(i, 2)
            print(self.final_rating)

            self.query = QSqlQuery()
            # self.query.exec("""CREATE TEMPORARY TABLE rating_table(`id` INT NOT NULL,`rating` float,PRIMARY KEY (`id`))""")
            print(self.query.exec("""CREATE TEMPORARY TABLE if not exists final_table as (Select * from seller)"""))
            print(self.query.exec("""ALTER TABLE `final_table` ADD COLUMN `final_rating` FLOAT(11)"""))
            for key, item in self.final_rating.items():
                # self.query.exec("""insert into rating_table(`id`,`rating`) value({0},{1})""".format(key,item))\
                print(item / 4, key)
                print(
                    self.query.exec("""update final_table set final_rating={0} where id = {1}""".format(item / 4, key)))
            self.ui.sqlRelationalTable.submitAll()
            self.ui.sqlRelationalTable.setTable('final_table')
            self.ui.setNameColumn()
            self.ui.sqlRelationalTable.setHeaderData(8, Qt.Horizontal, "Рейтинг")

            self.ui.sqlRelationalTable.select()
        except Exception as e:
            print(e)

    def maxmin(self, value, column):
        self.query = QSqlQuery()
        self.query.exec("""SELECT seller.`id`,{0}({1}) from seller""".format(value, column))
        while self.query.next():
            return float(self.query.value(1))

    def min_rating(self, criterion, spinBox):
        self.min_criterion = self.maxmin(self.min_, 'seller.`{0}`'.format(criterion))
        self.criterion_rating_per_one = self.min_criterion * float(spinBox.text().replace(',', '.'))
        self.query.exec("""SELECT seller.`id`,seller.`{}` from seller""".format(criterion))
        while self.query.next():
            try:
                self.criterion_rating = round(self.criterion_rating_per_one / int(self.query.value(1)) * 100, 2)
            except:
                self.criterion_rating = 0
            self.criterion_dict[self.query.value(0)][criterion] = self.criterion_rating
        return self.criterion_dict

    def max_rating(self, criterion, spinBox):
        self.max_criterion = self.maxmin(self.max_, 'seller.`{0}`'.format(criterion))
        self.criterion_rating_per_one = self.max_criterion / 100 * float(spinBox.text().replace(',', '.'))
        self.query.exec("""SELECT seller.`id`,seller.`{}` from seller""".format(criterion))
        while self.query.next():
            try:
                self.criterion_rating = round(int(self.query.value(1)) / self.criterion_rating_per_one, 2)
            except: self.criterion_rating = 0
            self.criterion_dict[self.query.value(0)][criterion] = self.criterion_rating

        return self.criterion_dict


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
