# -*- coding: utf-8 -*-
from abc import ABCMeta


class Pessoa(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.nome = None
        self.data_nasc = None
        self.cpf = None
        self.nacionalidade = None
        self.cep = None
        self.num_casa = None
        self.bairro = None
        self.endereco = None
        self.estado = None
        self.cidade = None
    pass

    def setDataLocalization(self):
        pass

    def setUserInformation(self):
        pass

    def dadosPessoa(self):
        pass

    def getNome(self):
        return self.nome

    def getCPF(self):
        return self.cpf

    def getContato(self):
        pass
