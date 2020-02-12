import sys
import design_main
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from amteo_parser import Parser
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from matplotlib import pyplot as plt
from datetime import date as Date
#Гистологические кассеты
class Example(QtWidgets.QMainWindow, design_main.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scenario_list = []
        self.search_prodName_pushButton.clicked.connect(self.search)
        self.contracts_listWidget.itemClicked.connect(self.item_clicked)
        self.save_pushButton.clicked.connect(self.save_the_data)
        self.units_listWidget.itemChanged.connect(self.unit_item_checked)
        self.save_pushButton.setEnabled(False)
        self.progressBar.setTextVisible(False)
        self.price_from_lineEdit.textChanged.connect(lambda x: self.price_range_changed('from',x))
        self.price_to_lineEdit.textChanged.connect(lambda x: self.price_range_changed('to',x))
        self.statusBar().showMessage('Ready')
        self.setWindowTitle('Makroskak_v1.0')    
        self.show()

    def search(self):
        self.progressBar.setTextVisible(True)
        name = self.search_prodName_lineEdit.text()
        date_from = self.from_dateEdit.date().toPyDate().strftime('%d.%m.%Y')
        date_to = self.to_dateEdit.date().toPyDate().strftime('%d.%m.%Y')
        time_period = f'{date_from}-{date_to}'

        scn = Scenario(time_period, name)
        self.scenario_list.append(scn)
        self.scenario_list[-1].parser.progress.connect(self.progressBar.setValue)
        self.scenario_list[-1].parser.done.connect(
            lambda: self.contracts_listWidget.addItem(self.scenario_list[-1].shortcut)
        )
        self.scenario_list[-1].parser.done.connect(
            lambda: self.progressBar.setTextVisible(False)
        )
        self.scenario_list[-1].parser.error.connect(self.error_dialog)

    def error_dialog(self,msg):
        w = QtWidgets.QErrorMessage()
        w.showMessage(msg)
        w.exec_()

    def save_the_data(self):
        item = self.contracts_listWidget.selectedItems()[0]
        for i in self.scenario_list:
            if i.shortcut == item.text():
                columns = list(i.list_of_contracts[0].keys())
                df = pd.DataFrame(columns=columns)
                for i in i.list_of_contracts:
                    df = df.append(i,ignore_index=True)
                df.to_excel(f'{i.shortcut}.xlsx')
                break
        
    def item_clicked(self, item):
        self.save_pushButton.setEnabled(True)
        for scn in self.scenario_list:
            if scn.shortcut == item.text():
                self.summary_textBrowser.setText(scn.summary())
                self.plotter = Plotter(scn)
                self.update_list_of_units(scn.units)
                self.year_price_qlabel.setPixmap(QPixmap(self.plotter.update()))
                break

    def update_list_of_units(self,units):
        self.units_listWidget.clear()
        for unit in units:
            QListWidgetItem(unit,self.units_listWidget).setCheckState(2)

    def price_range_changed(self,sender,val):
        # if val == '':
        #     val = 0
        try:
            if sender == 'from':
                self.plotter.scenario.min_price = int(val)
            if sender == 'to':
                self.plotter.scenario.max_price = int(val)
        except:
            pass
        self.year_price_qlabel.setPixmap(QPixmap(self.plotter.update()))

    def unit_item_checked(self,item):
        checked_items = []
        for i in range(self.units_listWidget.count()):
            if self.units_listWidget.item(i).checkState() == 2:
                checked_items.append(self.units_listWidget.item(i).text())
        self.plotter.not_units = checked_items
        self.year_price_qlabel.setPixmap(QPixmap(self.plotter.update()))

class Plotter:
    
    def __init__(self,scenario):
        self.scenario = scenario
        self.not_units = self.scenario.units
        self.update()

    def update(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.grid()

        for unit in self.scenario.units:
            X = []
            Y = []
            if unit in self.not_units:
                for contract in self.scenario.list_of_contracts:
                    if contract['Единица измерения'] == unit:
                        price = float(contract['Цена'])
                        if price < self.scenario.max_price and price > self.scenario.min_price:
                            Y.append(price)
                            a = [int(i) for i in contract['date'].split('-')]
                            date = Date(a[0],a[1],a[2])
                            X.append(date)
                ax.scatter(X,Y,label=unit) 
        ax.legend()
        plt.ylabel('Руб.')
        plt.xticks(rotation=45)
        plt.savefig('loc_.jpg',bbox_inches='tight')
        return 'loc_.jpg'        

from time import sleep
class Scenario:
    def __init__(self,time_period, name):
        self.time_period = time_period
        self.name = name
        self.shortcut = f'{self.name} - {self.time_period}'
        self.list_of_contracts = []
        self.parser = Parser(time_period, name)
        self.parser.done.connect(self.get_other_data)
        self.parser.start()            

    def get_other_data(self):
        self.list_of_contracts = self.parser.list_of_contracts
        self.units = self.parser.units()
        self.max_price = max([i['Цена'] for i in self.parser.list_of_contracts])
        self.min_price = min([i['Цена'] for i in self.parser.list_of_contracts])

    def summary(self):
        summary = ''
        summary += f'Продукт: {self.name}\n'
        summary += f'Период: {self.time_period}\n'
        summary += f'Количество контрактов: {len(self.list_of_contracts)}\n'
        summary += f'Средняя цена: {0}\n'
        summary += f'Ед. изм.: {self.units}\n'
        return summary


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()