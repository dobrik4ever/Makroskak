import sys
import design_main
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
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
        self.save_pushButton.setEnabled(False)
        self.progressBar.setTextVisible(False)
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
        item_id = 0
        for i in self.scenario_list:
            if i.shortcut == item.text():
                self.summary_textBrowser.setText(i.summary())
                self.year_price_qlabel.setPixmap(
                    QPixmap(i.make_year_plot())
                    )
                break


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

    def make_year_plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.grid()

        for unit in self.units:
            X = []
            Y = []
            for contract in self.list_of_contracts:
                if contract['Единица измерения'] == unit:
                    a = [int(i) for i in contract['date'].split('-')]
                    date = Date(a[0],a[1],a[2])
                    X.append(date)
                    Y.append(float(contract['Цена']))  
            ax.scatter(X,Y,label=unit) 
        ax.legend()
        plt.ylabel('Руб.')
        plt.xticks(rotation=45)
        plt.savefig('loc_.jpg',bbox_inches='tight')
        return 'loc_.jpg'

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