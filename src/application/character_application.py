
class CharacterApplication:
    def __init__(self, character_creator, console_output_handler):
        self.character_creator = character_creator
        self.console_output_handler = console_output_handler

    def run(self):
        name = input("Ingrese el nombre del personaje: ")
        char_class = input("Ingrese la clase del personaje: ")
        race = input("Ingrese la raza del personaje: ")
        background = input("Ingrese el background del personaje: ")
        age = int(input("Ingrese la edad del personaje: "))
        character = self.character_creator.create_character(name, char_class, race, background, age)
        self.console_output_handler.handle(character)
