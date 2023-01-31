from src.application.characters.character_creator import CharacterCreator
from src.application.characters.console.character_command_line_application import CharacterCommandLineApplication
from src.application.console.console_output_handler import ConsoleOutputHandler
from src.infrastructure.characters.mysql_character_repository import MySQLCharacterRepository
from src.infrastructure.database import MySQLDatabase


class ApplicationBootstrapper:
    def __init__(self):
        self.connection = MySQLDatabase().connect()
        self.repository = MySQLCharacterRepository(self.connection)
        self.output_handler = ConsoleOutputHandler()
        self.character_creator = CharacterCreator(self.repository)

    def get_character_command_line_application(self):
        return CharacterCommandLineApplication(self.character_creator, self.repository, self.output_handler)

    def close_connection(self):
        self.connection.close()
