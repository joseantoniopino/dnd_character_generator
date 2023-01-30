from src.domain.character import Character


class CharacterCreator:
    def __init__(self, character_repository):
        self.character_repository = character_repository

    def create_character(self, name, char_class, race, background, age):
        character = Character(name, char_class, race, background, age)
        self.character_repository.save_character(character)
        return character
