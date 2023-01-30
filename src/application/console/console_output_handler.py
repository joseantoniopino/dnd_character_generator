from src.application.interfaces.output_interface import OutputHandlerInterface


class ConsoleOutputHandler(OutputHandlerInterface):
    def handle(self, data):
        print(data)
