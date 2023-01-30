from abc import ABC, abstractmethod


class OutputHandler(ABC):
    @abstractmethod
    def handle(self, data):
        pass
