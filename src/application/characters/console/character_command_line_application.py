class CharacterCommandLineApplication:
    def __init__(self, character_creator, character_repository, console_output_handler):
        self.character_creator = character_creator
        self.character_repository = character_repository
        self.console_output_handler = console_output_handler

    def run(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Crear personaje")
            print("2. Ver personaje")
            print("3. Editar personaje")
            print("4. Listar personajes")
            print("5. Eliminar personaje")
            print("6. Salir")
            option = int(input("Opción: "))

            if option == 1:
                name = input("Ingrese el nombre del personaje: ")
                char_class = input("Ingrese la clase del personaje: ")
                race = input("Ingrese la raza del personaje: ")
                background = input("Ingrese el background del personaje: ")
                age = int(input("Ingrese la edad del personaje: "))
                character = self.character_creator.create_character(name, char_class, race, background, age)
                self.character_repository.save_character(character)
                print("Personaje creado correctamente.")
            elif option == 2:
                character_id = int(input("Ingrese el ID del personaje a ver: "))
                character = self.character_repository.get_character(character_id)
                self.console_output_handler.handle(character)
            elif option == 3:
                # Implementar la edición de personajes
                pass
            elif option == 4:
                # Implementar la lista de personajes
                pass
            elif option == 5:
                # Implementar la eliminación de personajes
                pass
            elif option == 6:
                break
