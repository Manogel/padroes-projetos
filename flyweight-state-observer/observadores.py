# -*- encoding: UTF-8 -*-

def imprime(nota_fiscal):
    print (f'Imprimindo nota fiscal {nota_fiscal.cnpj}')

def envia_email(nota_fiscal):
    print (f'Enviando nota fiscal {nota_fiscal.cnpj} para o email do cliente')

def salvar(nota_fiscal):
    print (f'Salvando nota fiscal {nota_fiscal.cnpj} no sistema')