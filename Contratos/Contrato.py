class Contrato(object):
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
  