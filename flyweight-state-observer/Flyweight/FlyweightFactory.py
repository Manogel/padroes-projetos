# -*- encoding: UTF-8 -*-
from Product import Item

class ProductFactory(object):

    def __init__(self):
        self.list_product = dict()

    def make(self, nome, valor):

        if (nome, valor) not in self.list_product:
            print('Criou um novo')
            self.list_product[(nome, valor)] = Item(nome, valor)

        return self.list_product[(nome, valor)]

""" 
class TeaShop(object):

    def __init__(self, product_factory):
        self.__orders = dict()
        self.__product_factory = product_factory

    def take_order(self, tea_type, table):

        if table not in self.__orders:
            self.__orders[table] = list()

        self.__orders[table].append(self.__tea_maker.make(tea_type))

    def serve(self):
        for table, orders in self.__orders.iteritems():
            print(f'Serving tea to table {table}')

if __name__ == u'__main__':
  """