# -*- encoding: UTF-8 -*-
from Checkout.State import State

class In_approval(State):

    def aplica_desconto_extra(self, orcamento, desc):
        orcamento.adiciona_desconto_extra(orcamento.valor * desc)

    def aprova(self, orcamento):
        orcamento.estado_atual = Approval()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reject()

    def finaliza(self, orcamento):
        raise Exception("Orcamentos em aprovacao nao pode ser finalizado")


class Approval(State):

    def aplica_desconto_extra(self, orcamento, desc):
        orcamento.adiciona_desconto_extra(orcamento.valor * desc)

    def aprova(self, orcamento):
        raise Exception("Orcamentos aprovado nao pode ser aprovado novamente")

    def reprova(self, orcamento):
        raise Exception("Orcamentos aprovado nao pode ser reprovado")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finished()


class Reject(State):

    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orcamentos reprovados nao recebem desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orcamentos aprovado nao pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamentos aprovado nao pode ser reprovado novamente")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finished()


class Finished(State):

    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orcamentos finalizados nao recebem desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orcamentos finalizado nao pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamentos finalizado nao pode ser reprovado")

    def finaliza(self, orcamento):
        raise Exception("Orcamentos finalizado nao pode ser finalizado novamente")

