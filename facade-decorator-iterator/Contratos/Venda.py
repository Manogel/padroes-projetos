from Contratos.Contrato import Contrato
import copy
from Interfaces.Command import Command


class Venda(Contrato, Command):
    def __init__(self, imovel, locador, locatario):
        Contrato.__init__(self, "Venda")
        self.Imovel = imovel
        self.Locador = locador
        self.Locatario = locatario
        self.valor = 0
        self.num_parcelas = 1
        self.valor_entrada = None
        pass

    def imprimirImovelContrato(self):
        self.Imovel.getInformation()
        pass

    def imprimirContrato(self):
        termo = f"""O VENDEDOR, {self.Locador.getNome()} no CPF {self.Locador.getCPF()},  na qualidade de legítimo proprietário do(a) {self.Imovel.getTipoImovel()}, 
situado à {self.Imovel.getEndereco()}, {self.Imovel.getNumero()} no CEP {self.Imovel.getCEP()}, resolve vendê-lo(a) ao COMPRADOR, 
{self.Locatario.getNome()} no CPF {self.Locatario.getCPF()}, pelo valor de R$ {self.Imovel.getValor()}.
    """
        print(termo)
        return termo

    def setParcelas(self, nParcelas):
        self.num_parcelas = nParcelas
        pass

    def getParcelas(self):
        return self.num_parcelas

    def setValor(self, valor):
        self.valor = valor
        pass

    def getValor(self):
        return self.valor

    def setValorEntrada(self, valor):
        self.valor = valor
        pass

    def getValorEntrada(self):
        return self.valor

    def clonar(self):
        return copy.copy(self)
