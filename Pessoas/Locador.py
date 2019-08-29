# -*- coding: utf-8 -*-
from Pessoas.Pessoa import Pessoa
from Interfaces.GetCep import GetCep
import json
import requests

class Locador(Pessoa, GetCep):
  def __init__(self, nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, comprovante_renda = None):
    Pessoa.__init__(self,nome, data_nasc, cpf, nacionalidade, cep, num_casa)
    self.comprovante_renda = comprovante_renda
    self.telefone = telefone
    self.email = email
    self.getCep()
    pass

  
  def getCep(self):
    response = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
    response = json.loads(response.content)
    self.bairro = response["bairro"]
    self.endereco = response["logradouro"]
    self.estado = response["uf"]
    self.cidade = response["localidade"]
    pass

  def dadosPessoa(self):
    text = f"""
    DADOS PESSOAIS:
      Nome: {self.nome}
      Data de nascimento: {self.data_nasc}
      CPF: {self.cpf}
      nacionalidade: {self.nacionalidade}
    
    LOCALIDADE:
      CEP: {self.cep}
      Estado: {self.estado}
      Cidade: {self.cidade}
      Endereço: {self.endereco}
      Bairro: {self.bairro}
      Nº Casa/Apartamento: {self.num_casa}
    
    CONTATO:
      Telefone: {self.telefone}
      Email: {self.email}

    RENDA MENSAL:
      Valor: {self.comprovante_renda}"""
    print(text)
    pass

  def getContato(self):
    return f'{self.telefone} / {self.email}'