# -*- coding: utf-8 -*-
from abc import ABCMeta
class Pessoa(object):
  __metaclass__ = ABCMeta
  def __init__(self, nome, data_nasc, cpf, nacionalidade, cep, num_casa):
    self.nome = nome
    self.data_nasc = data_nasc
    self.cpf = cpf
    self.nacionalidade = nacionalidade
    self.cep = cep
    self.num_casa = num_casa
    self.bairro = None
    self.endereco = None
    self.estado = None
    self.cidade = None
  pass

  def dadosPessoa(self):
    pass

  def getNome(self):
    return self.nome
  
  def getCPF(self):
    return self.cpf

  def getContato(self):
    pass
  