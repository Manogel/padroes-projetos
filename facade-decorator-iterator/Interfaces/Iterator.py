# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
class Iterator(ABC):
  def remove(self):
    pass
  
  def nextt(self):
    pass
  
  def previous(self):
    pass
  
  def count(self):
    pass
  
  def key(self):
    pass
  
  def rewind(self):
    pass
