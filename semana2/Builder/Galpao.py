from Builder.ImovelBuilder import ImovelBuilder
import json
import requests

class GalpaoBuilder(ImovelBuilder):
  def buildProprietario(self, dono):
    #Processamento
    self.imovel.proprietario = dono
    pass

  def buildLocalizacao(self):
    self.imovel.cep = "68925153"
    response = requests.get(f"https://viacep.com.br/ws/68925153/json/")
    response = json.loads(response.content)
    self.imovel.bairro = response["bairro"]
    self.imovel.endereco = response["logradouro"]
    self.imovel.estado = response["uf"]
    self.imovel.cidade = response["localidade"]
    self.imovel.num_casa = "781"
    pass
 
     
  def buildTerreno(self):
    self.imovel.area_construida = 340
    self.imovel.area_terreno = 360
    pass
 
     
  def buildDadosImovel(self):
    self.imovel.tipo = "Galpão"
    self.imovel.descricao = "Ambiente totalmente ventilado"
    pass
 
     
  def buildValor(self):
    self.imovel.valor = 170000
    pass
