from Memento import Memento
from Game import Game


perguntas = [
  ["Pergunta 1", 0], ["Pergunta 2", 0], ["Pergunta 3", 0], ["Pergunta 3", 0], 
  ["Pergunta 4", 0], ["Pergunta 5", 0],["Pergunta 6", 0],["Pergunta 7", 0],
  ["Pergunta 8", 0],["Pergunta 9", 0], ["Pergunta 10", 0],["Pergunta 11", 0]
  ]

Game(perguntas)

""" originator = Originator()

originator.setState("Estado1")
originator.setState("Estado2")

savedState.append(originator.saveState())
originator.setState("Estado3")

savedState.append(originator.saveState())

originator.restoreState(savedState[1]) """