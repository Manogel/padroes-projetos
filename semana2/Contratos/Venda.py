from Contratos.Contrato import Contrato

class Venda(Contrato):
  def __init__(self, inicio, fim, obs = "Sem descricao"):
    Contrato.__init__(self, "Venda", inicio, fim, obs)
    self.valor = None
    self.num_parcelas = 1
    self.valor_entrada = None
    pass

  def imprimirContrato(self):
    termo = f"""O VENDEDOR, {self.Locador.getNome()} no CPF {self.Locador.getCPF()},  na qualidade de legítimo proprietário do(a) {self.Imovel.getTipoImovel()}, 
situado à {self.Imovel.getEndereco()}, {self.Imovel.getNumero()} no CEP {self.Imovel.getCEP()}, resolve vendê-lo(a) ao COMPRADOR, 
{self.Locatario.getNome()} no CPF {self.Locatario.getCPF()}, pelo valor de R$ {self.Imovel.getValor()}.
    """
    print(termo)
    return termo

  def setParcelas(self, nParcelas):
    self.num_parcelas = nParcelas
    pass

  def getParcelas(self, nParcelas):
    return self.num_parcelas

  def setValor(self, valor):
    self.valor = valor
    pass

  def getValor(self, valor):
    return self.valor

  def setValorEntrada(self, valor):
    self.valor = valor
    pass
  
  def getValorEntrada(self, valor):
    return self.valor
  
  
    