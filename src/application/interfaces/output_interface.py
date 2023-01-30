from abc import ABC, abstractmethod


class OutputHandlerInterface(ABC):
    @abstractmethod
    def handle(self, data):
        pass
