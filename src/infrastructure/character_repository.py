# character_repository.py

class CharacterRepository:
    def save(self, character):
        raise NotImplementedError


class MySQLCharacterRepository(CharacterRepository):
    def __init__(self, connection):
        self.connection = connection

    def save(self, character):
        cursor = self.connection.cursor()
        sql = "INSERT INTO characters (name, class, race, background, age) VALUES (%s, %s, %s, %s, %s)"
        values = (character.name, character.char_class, character.race, character.background, character.age)
        cursor.execute(sql, values)
        self.connection.commit()
        cursor.close()
