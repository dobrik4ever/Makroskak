import bs4
import requests
import pandas as pd
import json
from PyQt5.QtCore import QThread, pyqtSignal

class Parser(QThread):

    progress = pyqtSignal(int)
    done = pyqtSignal()
    error = pyqtSignal(str)
    def __init__(self, time_period, product_name):
        QThread.__init__(self)
        self.product_name = product_name
        self.time_period = time_period
        self.list_of_contracts = []
        
    def run(self):
        product_name = self.product_name.replace(' ','+')
        self.url = f'http://openapi.clearspending.ru/restapi/v3/contracts/search/?daterange={self.time_period}&productsearch={product_name}&currentstage=EC&perpage=1'
        response = requests.get(self.url)
        try:
            data = response.json()
            number_of_contracts = int(data['contracts']['total'])
            pages = int(number_of_contracts/50)
            for page in range(1,pages+1):
                self.url = f'http://openapi.clearspending.ru/restapi/v3/contracts/search/?daterange={self.time_period}&productsearch={product_name}&currentstage=EC&page={page}'
                self.get(page)
                self.progress.emit((page/pages)*100)
            self.done.emit()
            self.progress.emit(0)
        except:
            self.error.emit('Нет контрактов!')
            pass

    def get(self,fname='response'):
        response = requests.get(self.url)
        if response.status_code == 200:
            pass
        elif response.status_code == 404:
            print('Not Found.')
            raise Exception('Internet otstoy u vas, soryyyan')

        data = response.json()

        with open(f'dump{fname}.json','w',encoding='utf-8') as file:
            json.dump(
                data,
                sort_keys=False,
                indent=4,
                ensure_ascii=False,
                separators=(',', ': '),
                fp=file
                )

        #Аттрибуты - дробление на участки данных
        self.contracts = [contract for contract in data['contracts']['data']]
        self.list_of_contracts += self.get_compressed_contracts()

    def get_compressed_contracts(self):
        contracts_data = []
        for contract in self.contracts:
            try:
                contracts_data.append(
                    self.__get_compressed_contract(contract)
                    )
            except:
                pass
        return contracts_data

    # def __get_simple_contract(self, contract):

    #     def product_from_list(List, element):
    #         print(List)
    #         print(element)
    #         for product in List:
    #             if element.lower() in product['name'].lower():
    #                 return product

    #     customer_name   = contract['customer']['fullName']
    #     date            = contract['signDate'].split('T')[0]
    
    #     product         = product_from_list(contract['products'], self.product_name)
    #     purchase_object = product['name']
    #     object_unit     = product['OKEI']['name']
    #     quantity        = product['quantity']
    #     price           = product['price']
        
    #     contractUrl     = contract['contractUrl']

    #     contract_data = {
    #         'Заказчик название' :   customer_name,
    #         'Объект закупки'    :   purchase_object,
    #         'Единица измерения' :   object_unit,
    #         'Количество'        :   quantity,
    #         'Цена'              :   price,
    #         'url'               :   contractUrl,
    #         'date'              :   date
    #     }
    #     return contract_data

    def __get_compressed_contract(self, contract):

        def product_from_list(List, element):
            for product in List:
                if element.lower() in product['name'].lower():
                    return product

        regnum          = contract['regNum']
        customer_name   = contract['customer']['fullName']
        customer_inn    = contract['customer']['inn']
        supplier_name   = contract['suppliers'][0]['organizationName']
        supplier_inn    = contract['suppliers'][0]['inn']
        date            = contract['signDate'].split('T')[0]
    
        product         = product_from_list(contract['products'], self.product_name)
        purchase_object = product['name']
        object_unit     = product['OKEI']['name']
        quantity        = product['quantity']
        price           = product['price']
        cost            = product['sum']
        
        contractUrl     = contract['contractUrl']

        contract_data = {
            'Номер закупки'     :   regnum,
            'Поставщик название':   supplier_name,
            'Поставщик инн'     :   supplier_inn,
            'Заказчик название' :   customer_name,
            'Заказчик инн'      :   customer_inn,
            'Объект закупки'    :   purchase_object,
            'Единица измерения' :   object_unit,
            'Количество'        :   quantity,
            'Цена'              :   price,
            'Стоимость'         :   cost,
            'url'               :   contractUrl,
            'date'              :   date
        }
        return contract_data

    def units(self):
        self.units = []
        for contract in self.list_of_contracts:
            self.units.append(contract['Единица измерения'])
        self.units = list(set(self.units))
        return self.units

    def find_product(self, product_name):
        for contract in self.contracts:
            print(f"ID: {contract['id']}")
            for ix, product in enumerate(contract['products']):
                if product_name in product['name']:
                   print('{}: - {}'.format(ix+1, product['name']))

    def package_types(self, product_name):
        package_types = 0
        for contract in self.contracts:
            for ix, product in enumerate(contract['products']):
                if product_name in product['name']:
                    try:
                        name = product['name']
                        price = product['price']
                        package = product['OKEI']['name']
                        summa = product['sum']
                        quantity = product['quantity']
                        if package not in package_types:
                            package_types.append(package)
                            print(name, price, package,  quantity, summa)
                    except:
                        pass
        return package_types