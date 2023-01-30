from abc import abstractmethod
from abc import ABCMeta


class CharacterApplicationInterface(metaclass=ABCMeta):
    @abstractmethod
    def create_character(self, name: str, char_class: str, race: str, background: str, age: int):
        pass

    @abstractmethod
    def run(self):
        pass
