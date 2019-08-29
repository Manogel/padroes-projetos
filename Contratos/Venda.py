# -*- coding: utf-8 -*-
from Contratos.Contrato import Contrato
class Venda(Contrato):
  def __init__(self, imovel, locador, locatario, inicio, fim, obs, valor_entrada = None):
    super(Venda, self).__init__("Venda", imovel, locador, locatario, inicio, fim, obs)
    self.termo_contrato = None
    self.valor_entrada = valor_entrada
    pass
  
  def imprimirContrato(self):
    self.termo_contrato = f"""O VENDEDOR, {self.Locador.getNome()} no CPF {self.Locador.getCPF()},  na qualidade de legítimo proprietário do(a) {self.Imovel.getTipoImovel()}, 
resolve vendê-lo(a) ao COMPRADOR, {self.Locatario.getNome()} no CPF {self.Locatario.getCPF()}, pelo valor de R$ {self.Imovel.getValor()} , 
que deverá ser pago da seguinte forma: a título de sinal e primeiro pagamento R$ {self.valor_entrada}, nesta data, 
do qual o VENDEDOR dará plena quitação após a compensação ou cobrança respectiva, 
e o restante no ato da desocupação do imóvel e entrega das chaves, no valor de R$ {self.Imovel.getValor() - self.valor_entrada}.
    """
    print(self.termo_contrato)
    pass
