from src.application.bootstrapper.application_bootstrapper import ApplicationBootstrapper


def main():
    bootstrapper = ApplicationBootstrapper()
    application = bootstrapper.get_character_command_line_application()
    application.run()

    bootstrapper.close_connection()


if __name__ == "__main__":
    main()
