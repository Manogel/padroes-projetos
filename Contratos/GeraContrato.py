# -*- coding: utf-8 -*-
from Contratos.Aluguel import Aluguel
from Contratos.Venda import Venda
from Contratos.Contrato import Contrato


class GeraContrato():
    @staticmethod
    def montaContrato(tipo, inicio, fim, obs, valor_entrada = 0, num_parcelas = 0):
      contratoFactory = None
      if (tipo.upper() == "Venda".upper()):
        contratoFactory = Venda()
      elif (tipo.upper() == "Aluguel".upper()):
        contratoFactory = Aluguel()
      else:
        return None
      contrato = Contrato(tipo, inicio, fim, obs, valor_entrada, num_parcelas)
      contrato.setLocador(contratoFactory.montaLocador('Manoel',  '30-10-1999', '03951567260', 'Brasileiro', '68925153', '781', '96991934171', 'manoelgomes53@gmail.com'))
      contrato.setLocatario(contratoFactory.montaLocatario('Gustavo',  '30-10-1996', '03951567260', 'Brasileiro', '68903770', '781', '96991934171', 'manoelgomes53@gmail.com', "42443232324"))
      contrato.setImovel(contratoFactory.montaImovel(contrato.getLocador(), "Apartamento", float(2999), "Area de lazer", '68925153', '781', float(59.76), float(80.89), 1, 2, 3, 4))
      contrato.setTermo(contratoFactory.montaTermo(contrato.getImovel(), contrato.getLocador(), contrato.getLocatario()))
      
      return contrato



""" class Contrato(object):
  def __init__(self, tipo, imovel, locador, locatario, inicio, fim, obs):
    self.tipo = tipo
    self.Imovel = imovel
    self.Locador = locador
    self.Locatario = locatario
    self.data_inicio = inicio
    self.data_fim = fim
    self.observacoes = obs
    pass

  def imprimirContrato(self):
    pass
   """