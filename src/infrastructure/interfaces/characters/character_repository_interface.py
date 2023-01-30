from abc import ABC, abstractmethod

from src.domain.characters.character import Character


class CharacterRepositoryInterface(ABC):
    @abstractmethod
    def save_character(self, character: Character) -> None:
        pass

    @abstractmethod
    def get_character(self, character_id: int) -> Character:
        pass
