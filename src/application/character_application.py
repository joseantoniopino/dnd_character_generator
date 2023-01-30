from src.domain.character import Character
from src.application.interfaces.character_application_interface import CharacterApplicationInterface


class CharacterApplication(CharacterApplicationInterface):
    def __init__(self, character_repository, console_output_handler):
        self.character_repository = character_repository
        self.console_output_handler = console_output_handler

    def create_character(self, name, char_class, race, background, age):
        character = Character(name, char_class, race, background, age)
        self.character_repository.save(character)
        self.console_output_handler.handle(character)

    def run(self):
        name = input("Ingrese el nombre del personaje: ")
        char_class = input("Ingrese la clase del personaje: ")
        race = input("Ingrese la raza del personaje: ")
        background = input("Ingrese el background del personaje: ")
        age = int(input("Ingrese la edad del personaje: "))
        self.create_character(name, char_class, race, background, age)
