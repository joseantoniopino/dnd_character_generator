from abc import ABC

from src.infrastructure.interfaces.characters.character_repository_interface import CharacterRepositoryInterface


class MySQLCharacterRepository(CharacterRepositoryInterface, ABC):
    def __init__(self, connection):
        self.connection = connection

    def save_character(self, character):
        cursor = self.connection.cursor()
        sql = "INSERT INTO characters (name, class, race, background, age) VALUES (%s, %s, %s, %s, %s)"
        values = (character.name, character.char_class, character.race, character.background, character.age)
        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()

    def get_character(self, character_id):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM characters WHERE id = %s"
        cursor.execute(sql, character_id)
        result = cursor.fetchone()
        cursor.close()
        return result
