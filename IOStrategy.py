# -*-coding utf-8-*-
from abc import abstractmethod, ABC


class IOStrategy(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, notes):
        pass
