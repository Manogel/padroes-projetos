from Imoveis.Imovel import Imovel
from Interfaces.GetCep import GetCep
import json
import requests


class Galpao(Imovel, GetCep):
    def __init__(self):
        super(Galpao, self).__init__("Galpao")
        pass

    def setDataLocalization(self, cep, num_casa):
        self.cep = cep
        self.num_casa = num_casa
        self.getCep()
        pass

    def setImovelInformation(self, valor, descricao, area_const, area_terr):
        self.valor = valor
        self.descricao = descricao
        self.area_terreno = area_terr
        self.area_construida = area_const
        pass

    def getCep(self):
        response = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        response = json.loads(response.content)
        self.bairro = response["bairro"]
        self.endereco = response["logradouro"]
        self.estado = response["uf"]
        self.cidade = response["localidade"]
        pass

    def getInformation(self):
        text = f"""
    DADOS DO PROPRIETARIO:
      Nome: {self.proprietario.getNome()}
      CPF: {self.proprietario.getCPF()}
      Contato: {self.proprietario.getContato()} 
    
    SOBRE O IMOVEL:
      Tipo: {self.tipo }
      Área do terreno: {self.area_terreno}
      Área construida: {self.area_construida}
      Descrição do local: {self.descricao}
    
    LOCALIDADE:
      CEP: {self.cep}
      Estado: {self.estado}
      Cidade: {self.cidade}
      Endereço: {self.endereco}
      Bairro: {self.bairro}
      Nº Casa/Apartamento: {self.num_casa}
    
    VALOR DO IMOVEL: {self.valor} """
        print(text)
        pass
