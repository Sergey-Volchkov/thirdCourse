from munkres import Munkres, print_matrix, make_cost_matrix, DISALLOWED
import sys
from PyQt5 import QtWidgets
from kis2 import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.acceptButton.clicked.connect(self.recreateTableWidget)
        self.ui.calculateButton.clicked.connect(self.calculate)
    def recreateTableWidget(self):
        self.ui.resetColumn(n=int(self.ui.spinBox.text()))
    def calculate(self):
        matrix = []
        for _ in range(self.ui.tableWidget.rowCount()):
            matrix.append([])
            for i in range(self.ui.tableWidget.columnCount()):
                try:
                    matrix[_].append(int(self.ui.tableWidget.item(_,i).text()))
                except:
                    matrix[_].append(DISALLOWED)

        #cost_matrix = make_cost_matrix(matrix, lambda cost: (sys.maxsize - cost) if
         #                                     (cost != DISALLOWED) else DISALLOWED)
        m = Munkres()
        indexes = m.compute(matrix)
        #print_matrix(matrix, msg='Highest profit through this matrix:')
        self.total = 0
        self.buf = []
        for self.row, self.column in indexes:
            self.value = matrix[self.row][self.column]
            self.total += self.value
            self.buf.append(str(str(self.row +1)+ ' ' +str(self.column+ 1) + ' -> ' +str(self.value)))
        self.buf.append('Сумма значений= ' + str(self.total))
        self.showdialog()
    def showdialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Ответ представлен в формате '№ строки','№ столбца','значение'")
        msg.setInformativeText('\n'.join(self.buf))
        msg.setWindowTitle("Ответ")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
