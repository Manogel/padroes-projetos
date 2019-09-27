# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def imprimirImovelContrato(self):
        pass
    pass
