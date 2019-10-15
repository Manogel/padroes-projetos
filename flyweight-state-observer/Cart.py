# -*- encoding: UTF-8 -*-
from Checkout.StateBuget import In_approval

class Cart(object):
    def __init__(self):
        self.__itens = []
        self.estado_atual = In_approval()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    def aplica_desconto_extra(self, desc):
        self.estado_atual.aplica_desconto_extra(self, desc)

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return self.__itens

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)