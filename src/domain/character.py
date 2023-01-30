class Character:
    def __init__(self, name: str, race: str, char_class: str, background: str, age: int):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.background = background
        self.age = age

    # TODO: reemplazar por método para imprimir en pdf
    def __str__(self):
        return f"Nombre: {self.name}\nRaza: {self.race}\nClase: {self.char_class}\nTrasfondo: {self.background}\nEdad: {self.age}"
