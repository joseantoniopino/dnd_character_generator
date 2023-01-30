from src.application.interface import OutputHandler


class ConsoleOutputHandler(OutputHandler):
    def handle(self, data):
        print(data)
