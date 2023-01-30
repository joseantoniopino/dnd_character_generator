
from src.application.character_application import CharacterApplication
from src.application.character_creator import CharacterCreator
from src.application.console_output_handler import ConsoleOutputHandler
from src.infrastructure.character_repository import MySQLCharacterRepository
from src.infrastructure.database import MySQLDatabase


def main():
    # Conectarse a la base de datos
    connection = MySQLDatabase().connect()
    repository = MySQLCharacterRepository(connection)
    output_handler = ConsoleOutputHandler()
    character_creator = CharacterCreator(repository)
    application = CharacterApplication(character_creator, output_handler)
    application.run()

    # Cerrar la conexión
    connection.close()


if __name__ == "__main__":
    main()
