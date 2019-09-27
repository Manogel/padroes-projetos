# -*- coding: utf-8 -*-
from Pessoas.Pessoa import Pessoa
from Interfaces.GetCep import GetCep
import json
import requests


class Locador(Pessoa, GetCep):
    def __init__(self):
        Pessoa.__init__(self)
        self.comprovante_renda = None
        self.telefone = None
        self.email = None
        pass

    def setDataLocalization(self, cep, num_casa):
        self.cep = cep
        self.num_casa = num_casa
        self.getCep()
        pass

    def setUserInformation(self, nome, data_nasc, cpf, nacionalidade, telefone, email):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.nacionalidade = nacionalidade
        self.telefone = telefone
        self.email = email
        pass

    def setComprovanteRenda(self, comprovante_renda):
        self.comprovante_renda = comprovante_renda
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
