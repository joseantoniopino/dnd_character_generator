class MainMenu:
    def __init__(self):
        self.options = [
            ("Personaje", self.character_menu),
            ("Raza", self.race_menu),
            ("Trasfondo", self.background_menu),
            ("Clase", self.class_menu),
            # Añade más opciones aquí si es necesario
        ]

    def display(self):
        print("Main Menu:")
        for i, (option, _) in enumerate(self.options):
            print(f"{i + 1}. {option}")
        print("\n0. Exit")

    def run(self):
        while True:
            self.display()
            choice = self.get_user_choice()
            if choice == 0:
                break
            self.options[choice - 1][1]()

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 0 <= choice <= len(self.options):
                    return choice
                print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid choice. Please try again.")

    def character_menu(self):
        pass
        # Llama a la clase correspondiente al CRUD de Personaje

    def race_menu(self):
        pass
        # Llama a la clase correspondiente al CRUD de Raza

    def background_menu(self):
        pass
        # Llama a la clase correspondiente al CRUD de Trasfondo

    def class_menu(self):
        pass
        # Llama a la clase correspondiente al CRUD de Clase
