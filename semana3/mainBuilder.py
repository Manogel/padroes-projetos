from Builder.ImobiliariaDirector import ImobiliariaDirector
from Builder.Residencial import ResidencialBuilder
from Builder.Galpao import GalpaoBuilder
from Pessoas.Locador import Locador


DonoImovel = Locador('Manoel',  '30-10-1999', '03951567260', 'Brasileiro', '68925153', '781', '96991934171', 'manoelgomes53@gmail.com')

imobiliaria = ImobiliariaDirector(GalpaoBuilder())

imobiliaria.construct(DonoImovel)

meuImovel = imobiliaria.getImovel()

text = f"""
    DADOS DO LOCADOR:
      Nome: {meuImovel.proprietario.getNome()}
      CPF: {meuImovel.proprietario.getCPF()}
      Contato: {meuImovel.proprietario.getContato()}
    
    SOBRE O IMOVEL:
      Tipo: {meuImovel.tipo}
      Área do terreno: {meuImovel.area_terreno}
      Área construida: {meuImovel.area_construida}
      Descrição do local: {meuImovel.descricao}
    
    LOCALIDADE:
      CEP: {meuImovel.cep}
      Estado: {meuImovel.estado}
      Cidade: {meuImovel.cidade}
      Endereço: {meuImovel.endereco}
      Bairro: {meuImovel.bairro}
      Nº Casa/Apartamento: {meuImovel.num_casa}
    
    VALOR DO IMOVEL: {meuImovel.valor} """

print(text)

