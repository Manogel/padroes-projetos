# -*- coding: utf-8 -*-
from Contratos.FactoryContract import FactoryContract
from Imoveis.Residencia import Residencia 
from Imoveis.Galpao import Galpao
from Pessoas.Locador import Locador
from Pessoas.Locatario import Locatario
from Interfaces.TermoContrato import TermoContrato

class Venda(FactoryContract, TermoContrato):
  def montaLocador(self, nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, comprovante_renda = None):
    return Locador(nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, comprovante_renda)
  
  def montaLocatario(self, nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, cnpj = None):
    return Locatario(nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, cnpj)

  def montaImovel(self, proprietario, tipo, valor, descricao, cep, num_casa,  area_const, area_terr, n_suites, n_quartos, n_banheiros, n_garagem):
    return Residencia(proprietario, tipo, valor, descricao, cep, num_casa,  area_const, area_terr, n_suites, n_quartos, n_banheiros, n_garagem)

  def montaTermo(self, Imovel, Locador, Locatario):
    termo = f"""O VENDEDOR, {Locador.getNome()} no CPF {Locador.getCPF()},  na qualidade de legítimo proprietário do(a) {Imovel.getTipoImovel()}, 
situado à {Imovel.getEndereco()}, {Imovel.getNumero()} no CEP {Imovel.getCEP()}, resolve vendê-lo(a) ao COMPRADOR, 
{Locatario.getNome()} no CPF {Locatario.getCPF()}, pelo valor de R$ {Imovel.getValor()}.
    """
    return termo







""" class Venda(FactoryContract):
  def __init__(self, imovel, locador, locatario, inicio, fim, obs, valor_entrada = None):
    super(Venda, self).__init__("Venda", imovel, locador, locatario, inicio, fim, obs)
    self.termo_contrato = None
    self.valor_entrada = valor_entrada
    pass
  
  def imprimirContrato(self):
    self.termo_contrato = f""O VENDEDOR, {self.Locador.getNome()} no CPF {self.Locador.getCPF()},  na qualidade de legítimo proprietário do(a) {self.Imovel.getTipoImovel()}, 
resolve vendê-lo(a) ao COMPRADOR, {self.Locatario.getNome()} no CPF {self.Locatario.getCPF()}, pelo valor de R$ {self.Imovel.getValor()} , 
que deverá ser pago da seguinte forma: a título de sinal e primeiro pagamento R$ {self.valor_entrada}, nesta data, 
do qual o VENDEDOR dará plena quitação após a compensação ou cobrança respectiva, 
e o restante no ato da desocupação do imóvel e entrega das chaves, no valor de R$ {self.Imovel.getValor() - self.valor_entrada}.
    "
    print(self.termo_contrato)
    pass
 """

