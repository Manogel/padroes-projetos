


class Contrato(object):
  def __init__(self, tipo, inicio, fim, obs, valor_entrada = 0, num_parcelas = 0):
    self.tipo = tipo
    self.Imovel = None
    self.Locador = None
    self.Locatario = None
    self.data_inicio = inicio
    self.data_fim = fim
    self.observacoes = obs
    self.numParcelas = num_parcelas
    self.valorEntrada = valor_entrada
    self.termo_contrato = None
    pass

  def imprimirContrato(self):
    print(self.termo_contrato)
    return True
  
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
    