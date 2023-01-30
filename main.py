
from src.application.character_application import CharacterApplication
from src.application.console_output_handler import ConsoleOutputHandler
from src.infrastructure.character_repository import MySQLCharacterRepository
from src.infrastructure.database import MySQLDatabase


def main():
    # Conectarse a la base de datos
    connection = MySQLDatabase().connect()

    repository = MySQLCharacterRepository(connection)
    output_handler = ConsoleOutputHandler()
    application = CharacterApplication(repository, output_handler)

    application.run()

    # Cerrar la conexión
    connection.close()


if __name__ == "__main__":
    main()
