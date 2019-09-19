# -*- coding: utf-8 -*-
from Memento import Memento
import math

class Game(object):
  def __init__(self, perguntas):
    self.pontos = 0
    self.perguntas = perguntas
    self.memento = []
    self.startGame()
    
    pass

  def setState(self, item, x):
    # print(f'ORIGINATOR: Mudando o estado para {self.state}')
    if (x == item[1]):
      self.memento.append(self.saveState())
      self.pontos = self.pontos + 1
      print('Acertou!!!!!')
    else:
      self.memento.append(self.saveState())
      if (self.pontos - 1 >= 0):
        self.pontos = self.pontos - 1
      print('Errou!!!!!')
  
  def saveState(self):
    # print(f'ORIGINATOR: Salvando estado')
    return Memento(self.pontos)
  

  def restoreState(self):
    self.pontos = self.memento[-2].getStateSaved()
    # print('Restaurando estado!')
    pass

  def startGame(self):
    print('INICIANDO GAME....')
    print('''Use as seguintes informações: ''')
    print('0 para não')
    print('1 para sim')
    print("-=========-")
    
    self.memento.append(self.saveState())
    for i, item in enumerate(self.perguntas):
      print(f'Fase {i+1}')
      print(f'Seu nivel {self.pontos}')
      print(f'\n{item[0]}')
      x = int(input("Sua Resposta: "))
      self.setState(item, x)
      print("-==================-\n")
    print('JOGO FINALIZADO')
    print(f'Você atingiu o nivel {self.pontos}')
    if (self.pontos == len(self.perguntas)):
      print("Parabéns você zerou o jogo!")
    elif(self.pontos < math.ceil(len(self.perguntas)/2) ):
      print("Parabéns você precisa melhorar!")
    else:
      print("Mais um pouco e você zerava o jogo!")

    pass

  

  