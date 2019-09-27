# -*- coding: utf-8 -*-
from Imoveis.Galpao import Galpao
from Imoveis.Residencia import Residencia
from Contratos.Venda import Venda
from Contratos.Aluguel import Aluguel
from Pessoas.Locador import Locador
from Pessoas.Locatario import Locatario
from Contratos.GerirContratos import GerirContratos


class Facade():
    def __init__(self):
        self.Imovel = None
        self.Locatario = None
        pass

    def newImovel(self, tipo):
        if(tipo.upper == 'GALPAO'):
            self.Imovel = Galpao()
            self.Imovel.setDataLocalization('68925153', '781')
            self.Imovel.setImovelInformation(
                float(2.999), "Area de lazer", float(59.76), float(80.89))
            self.Imovel.setPropritetario(self.linkLocatario())
        else:
            self.Imovel = Residencia(tipo)
            self.Imovel.setDataLocalization('68925153', '781')
            self.Imovel.setImovelInformation(
                float(2999), "Area de lazer", float(59.76), float(80.89), 1, 2, 3, 4)
            self.Imovel.setPropritetario(self.linkLocatario())
        return self.Imovel

    def linkLocatario(self):
        isExists = False
        if(isExists):
            # Find locatario e return to self.locatario
            print('Find locatario e return to self.locatario')
        else:
            self.newLocatario()
        return self.Locatario

    def newLocatario(self):
        self.Locatario = Locatario()
        self.Locatario.setCnpj("42443232324")
        self.Locatario.setDataLocalization('68925153', '781')
        self.Locatario.setUserInformation('Gustavo', '30-10-2000', '03951567260',
                                          'Argentino', '96991934171', 'Gustavo@gmail.com')
        return self.Locatario
