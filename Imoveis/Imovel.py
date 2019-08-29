# -*- coding: utf-8 -*-
from Interfaces.GetCep import GetCep

class Imovel(object):
  def __init__(self, proprietario, tipo, valor, descricao, cep, num_casa, area_const, area_terr):
    self.proprietario = proprietario
    self.tipo = tipo
    self.valor = valor
    self.descricao = descricao
    self.cep = cep
    self.area_terreno = area_terr
    self.area_construida = area_const
    self.num_casa = num_casa
    self.endereco = None
    self.bairro = None
    self.endereco = None
    self.cidade = None
    self.estado = None
    pass

  def editInformation(self):
    pass

  def getInformation(self):
    pass

  def getTipoImovel(self):
    return self.tipo
  
  def getValor(self):
    return self.valor

  def getCep(self):
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
