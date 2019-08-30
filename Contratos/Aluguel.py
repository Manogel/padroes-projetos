# -*- coding: utf-8 -*-
from Contratos.FactoryContract import FactoryContract
from Imoveis.Residencia import Residencia 
from Imoveis.Galpao import Galpao
from Pessoas.Locador import Locador
from Pessoas.Locatario import Locatario
from Interfaces.TermoContrato import TermoContrato

class Aluguel(FactoryContract, TermoContrato):
  def montaLocador(self, nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, comprovante_renda = None):
    return Locador(nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, comprovante_renda)
  
  def montaLocatario(self, nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, cnpj = None):
    return Locatario(nome, data_nasc, cpf, nacionalidade, cep, num_casa, telefone, email, cnpj)

  def montaImovel(self, proprietario, tipo, valor, descricao, cep, num_casa,  area_const, area_terr, n_suites, n_quartos, n_banheiros, n_garagem):
    return Residencia(proprietario, tipo, valor, descricao, cep, num_casa,  area_const, area_terr, n_suites, n_quartos, n_banheiros, n_garagem)

  def montaTermo(self, Imovel, Locador, Locatario):
    termo = f"""
LOCADOR: {Locador.getNome()}, portador da cédula de CPF nº {Locador.getCPF()}.

LOCATÁRIO: {Locatario.getNome()}, portador da cédula de CPF nº {Locatario.getCPF()}.

CLÁUSULA: O objeto deste contrato de locação é o imóvel residencial, 
situado à {Imovel.getEndereco()}, {Imovel.getNumero()}, {Imovel.getBairro()}, {Imovel.getCEP()}, {Imovel.getCidade()} - {Imovel.getEstado()}."""
    return termo











""" from Contratos.Contrato import Contrato

class Aluguel(Contrato):
  def __init__(self, imovel, locador, locatario, inicio, fim, obs, valor, temp = 5):
    super(Aluguel, self).__init__("Aluguel", imovel, locador, locatario, inicio, fim, obs)
    self.termo_contrato = None
    self.valor = valor
    self.tempo_locacao = temp
    pass
  
  def imprimirContrato(self):
    self.termo = f""
LOCADOR: {self.Locador.getNome()}, portador da cédula de CPF nº {self.Locador.getCPF()}.

LOCATÁRIO: {self.Locatario.getNome()}, portador da cédula de CPF nº {self.Locatario.getCPF()}.

CLÁUSULA PRIMEIRA: O objeto deste contrato de locação é o imóvel residencial, situado à {self.Imovel.getEndereco()}, {self.Imovel.getNumero()}, {self.Imovel.getBairro()}, {self.Imovel.getCep()}, {self.Imovel.getCidade()} - {self.Imovel.getEstado()}.

CLÁUSULA SEGUNDA: O prazo da locação é de {self.tempo_locacao} meses, iniciando-se em {self.data_inicio} com término em {self.data_fim}, independentemente e aviso, notificação ou interpelação judicial ou mesmo extrajudicial.

CLÁUSULA TERCEIRA: O aluguel mensal, deverá ser pago até o dia 10 (dez) do mês subseqüente ao vencido, no local indicado pelo LOCADOR, é de R$ {self.valor/self.tempo_locacao} (Valor) mensais, reajustados anualmente, de conformidade com a variação do IGP-M apurada no ano anterior, e na sua falta, por outro índice criado pelo Governo Federal e, ainda, em sua substituição, pela Fundação Getúlio Vargas, reajustamento este sempre incidente e calculado sobre o último aluguel pago no último mês do ano anterior.

CLÁUSULA QUARTA: O LOCATÁRIO será responsável por todos os tributos incidentes sobre o imóvel bem como despesas ordinárias de condomínio, e quaisquer outras despesas que recaírem sobre o imóvel, arcando tambem com as despesas provenientes de sua utilização seja elas, ligação e consumo de luz, força, água e gás que serão pagas diretamente às empresas concessionárias dos referidos serviços.

CLÁUSULA QUINTA: Em caso de mora no pagamento do aluguel, será aplicada multa de 2% (dois por cento) sobre o valor devido e juros mensais de 1% (um por cento) do montante devido.

CLÁUSULA SEXTA: Fica ao LOCATÁRIO, a responsabilidade em zelar pela conservação, limpeza do imóvel, efetuando as reformas necessárias para sua manutenção sendo que os gastos e pagamentos decorrentes da mesma, correrão por conta do mesmo. O LOCATÁRIO está obrigado a devolver o imóvel em perfeitas condições de limpeza, conservação e pintura, quando finda ou rescindida esta avença, conforme constante no termo de vistoria em anexo. O LOCATÁRIO não poderá realizar obras que alterem ou modifiquem a estrutura do imóvel locado, sem prévia autorização por escrito da LOCADORA. Caso este consinta na realização das obras, estas ficarão desde logo, incorporadas ao imóvel, sem que assista ao LOCATÁRIO qualquer indenização pelas obras ou retenção por benfeitorias. As benfeitorias removíveis poderão ser retiradas, desde que não desfigurem o imóvel locado.

PARÁGRAFO ÚNICO: O LOCATÁRIO declara receber o imóvel em perfeito estado de conservação e perfeito funcionamento devendo observar o que consta no termo de vistoria.

CLÁUSULA SÉTIMA: O LOCATÁRIO declara, que o imóvel ora locado, destina-se única e exclusivamente para o seu uso residencial e de sua família.

PARÁGRAFO ÚNICO: O LOCATÁRIO, obriga por si e sua família, a cumprir e a fazer cumprir integralmente as disposições legais sobre o Condomínio, a sua Convenção e o seu Regulamento Interno.

CLÁUSULA OITAVA: O LOCATÁRIO não poderá sublocar, transferir ou ceder o imóvel, sendo nulo de pleno direito qualquer ato praticado com este fim sem o consentimento prévio e por escrito do LOCADOR.

CLÁUSULA NONA: Em caso de sinistro parcial ou total do prédio, que impossibilite a habitação o imóvel locado, o presente contrato estará rescindido, independentemente de aviso ou interpelação judicial ou extrajudicial; no caso de incêndio parcial, obrigando a obras de reconstrução, o presente contrato terá suspensa a sua vigência e reduzida a renda do imóvel durante o período da reconstrução à metade do que na época for o aluguel, e sendo após a reconstrução devolvido o LOCATÁRIO pelo prazo restante do contrato, que ficará prorrogado pelo mesmo tempo de duração das obras de reconstrução.

CLÁUSULA DÉCIMA : Em caso de desapropriação total ou parcial do imóvel locado, ficará rescindido de pleno direito o presente contrato de locação, independente de quaisquer indenizações de ambas as partes ou contratantes.

CLÁUSULA DÉCIMA PRIMEIRA: Falecendo o FIADOR, o LOCATÁRIO, em 30 (trinta) dias, dar substituto idôneo que possa garantir o valor locativo e encargos do referido imóvel, ou prestar seguro fiança de empresa idônea.

CLÁUSULA DÉCIMA SEGUNDA: No caso de alienação do imóvel, obriga-se o LOCADOR, dar preferência ao LOCATÁRIO, e se o mesmo não utilizar-se dessa prerrogativa, o LOCADOR deverá constar da respectiva escritura pública, a existência do presente contrato, para que o adquirente o respeite nos termos da legislação vigente.

CLÁUSULA DÉCIMA TERCEIRA: O FIADOR e principal pagador do LOCATÁRIO, responde solidariamente por todos os pagamentos descritos neste contrato bem como, não só até o final de seu prazo, como mesmo depois, até a efetiva entrega das chaves ao LOCADOR e termo de vistoria do imóvel.

CLÁUSULA DÉCIMA QUARTA: È facultado ao LOCADOR vistoriar, por si ou seus procuradores, sempre que achar conveniente, para a certeza do cumprimento das obrigações assumidas neste contrato.

CLÁUSULA DÉCIMA QUINTA: A infração de qualquer das cláusulas do presente contrato, sujeita o infrator à multa de duas vezes o valor do aluguel, tomando-se por base, o último aluguel vencido.

CLÁUSULA DÉCIMA SEXTA: As partes contratantes obrigam-se por si, herdeiros e/ou sucessores, elegendo o Foro da Cidade do (colocar o fórum do município), para a propositura de qualquer ação.

E, por assim estarem justos e contratados, mandaram extrair o presente instrumento em três (03) vias, para um só efeito, assinando-as, juntamente com as testemunhas, a tudo presentes.
    "

    print(f'{self.termo[0:900]} [...]')
    pass """
