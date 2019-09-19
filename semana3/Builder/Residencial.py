from Builder.ImovelBuilder import ImovelBuilder
import json
import requests

class ResidencialBuilder(ImovelBuilder):
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
    self.imovel.area_construida = 2000
    self.imovel.area_terreno = 2200
    pass
 
     
  def buildDadosImovel(self):
    self.imovel.tipo = "Apartamento"
    self.imovel.descricao = "Lugar muito legal"
    pass
 
     
  def buildValor(self):
    self.imovel.valor = 250000
    pass


