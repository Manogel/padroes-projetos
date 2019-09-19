from Imoveis.Imovel import Imovel
from Interfaces.GetCep import GetCep
import json
import requests

class Galpao(Imovel, GetCep):
  def __init__(self, proprietario, valor, descricao, cep, num_casa, area_const, area_terr):
    super(Galpao, self).__init__(proprietario, "Galpao" , valor, descricao, cep, num_casa, area_const, area_terr)
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

  def getInformation(self):
    text = f"""
    DADOS DO LOCADOR:
      Nome: 
      CPF:
      Contato: 
    
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