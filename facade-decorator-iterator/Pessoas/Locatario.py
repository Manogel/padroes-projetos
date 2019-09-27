from Pessoas.Pessoa import Pessoa
from Interfaces.GetCep import GetCep
import json
import requests


class Locatario(Pessoa, GetCep):
    def __init__(self):
        Pessoa.__init__(self)
        self.telefone = None
        self.email = None
        self.cnpj = None
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

    def setCnpj(self, cnpj):
        self.cnpj = cnpj
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
      Bairro: {self.bairro}
      Endereço: {self.endereco}
      Nº Casa/Apartamento: {self.num_casa}
    
    CONTATO:
      Telefone: {self.telefone}
      Email: {self.email}

    DADOS EMPRESARIAIS:
      CNPJ: {self.cnpj}"""
        print(text)
        pass
