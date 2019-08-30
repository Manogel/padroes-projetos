# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
class TermoContrato(ABC):
  @abstractmethod
  def montaTermo(self):
    pass
  pass