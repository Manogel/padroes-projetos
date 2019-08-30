from abc import ABCMeta, abstractmethod

class FactoryContract(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def montaLocador(self):
    pass
  
  @abstractmethod
  def montaLocatario(self):
    pass

  @abstractmethod
  def montaImovel(self):
    pass

