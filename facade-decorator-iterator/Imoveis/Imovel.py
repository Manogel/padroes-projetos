# -*- coding: utf-8 -*-
from Interfaces.GetCep import GetCep
from abc import ABCMeta


class Imovel(object):
    __metaclass__ = ABCMeta

    def __init__(self, tipo):
        self.proprietario = None
        self.tipo = tipo
        self.cep = None
        self.num_casa = None
        self.valor = None
        self.descricao = None
        self.area_terreno = None
        self.area_construida = None
        self.endereco = None
        self.bairro = None
        self.cidade = None
        self.estado = None
        pass

    def editInformation(self):
        pass

    def setDataLocalization(self):
        pass

    def setImovelInformation(self):
        pass

    def getInformation(self):
        pass

    def getTipoImovel(self):
        return self.tipo

    def getValor(self):
        return self.valor

    def getCEP(self):
        return self.cep

    def getEndereco(self):
        return self.endereco

    def getBairro(self):
        return self.bairro

    def getCidade(self):
        return self.cidade

    def getEstado(self):
        return self.estado

    def getNumero(self):
        return self.num_casa

    def setPropritetario(self, proprietario):
        self.proprietario = proprietario
        pass

    def getPropritetario(self):
        return self.proprietario
