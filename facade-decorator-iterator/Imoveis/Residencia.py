from Imoveis.Imovel import Imovel
from Interfaces.GetCep import GetCep
import json
import requests


class Residencia(Imovel, GetCep):
    def __init__(self, tipo):
        super().__init__(tipo)
        self.num_suites = None
        self.num_quartos = None
        self.num_banheiros = None
        self.num_vagas_garagem = None
        pass

    def setDataLocalization(self, cep, num_casa):
        self.cep = cep
        self.num_casa = num_casa
        self.getCep()
        pass

    def setImovelInformation(self, valor, descricao, area_const, area_terr, n_suites, n_quartos, n_banheiros, n_garagem):
        self.valor = valor
        self.descricao = descricao
        self.area_terreno = area_terr
        self.area_construida = area_const
        self.num_suites = n_suites
        self.num_quartos = n_quartos
        self.num_banheiros = n_banheiros
        self.num_vagas_garagem = n_garagem
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
      Tipo: {self.tipo}
      Número de quartos: {self.num_quartos}
      Número de suites: {self.num_suites}
      Número de banheiros: {self.num_banheiros}
      Número de vagas na garagem: {self.num_vagas_garagem}
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
