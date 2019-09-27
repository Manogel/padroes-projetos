# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Contrato(ABC):
    key = 0 
    def __init__(self, tipo):
        Contrato.key = Contrato.key + 1
        self.key = f"{Contrato.key}ADF{2*Contrato.key}"
        self.tipo = tipo
        self.Imovel = None
        self.Locador = None
        self.Locatario = None
        self.data_inicio = None
        self.data_fim = None
        self.observacoes = None
        self.termo_contrato = None
        pass

    def setInfo(self, inicio, fim, obs):
        self.data_inicio = inicio
        self.data_fim = fim
        self.observacoes = obs
        pass

    def getTipo(self):
        return self.tipo

    def imprimirContrato(self):
        pass

    def setImovel(self, imovel):
        self.Imovel = imovel
        return True

    def setLocador(self, locador):
        self.Locador = locador
        return True

    def setLocatario(self, locatario):
        self.Locatario = locatario
        return True

    def setTermo(self, termo):
        self.termo_contrato = termo
        return True

    def getImovel(self):
        return self.Imovel

    def getLocador(self):
        return self.Locador

    def getLocatario(self):
        return self.Locatario

    def clonar(self):
        pass
