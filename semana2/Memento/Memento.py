

class Memento(object):
  def __init__(self, state):
    self.state = state
    pass

  def getStateSaved(self):
    return self.state

    
  