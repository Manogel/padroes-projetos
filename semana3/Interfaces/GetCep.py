# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class GetCep(ABC):
  @abstractmethod
  def getCep(self):
    pass
  pass