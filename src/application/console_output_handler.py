from src.application.interfaces.outputInterface import OutputHandlerInterface


class ConsoleOutputHandler(OutputHandlerInterface):
    def handle(self, data):
        print(data)
