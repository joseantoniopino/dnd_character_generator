def main():
    print("Bienvenido a la aplicación de personajes para Dungeons and Dragons")
    print("Por favor, seleccione una de las siguientes opciones:")
    print("1. Iniciar sesión")
    print("2. Registrarse")

    option = input("Opción: ")

    if option == "1":
        print("Iniciando sesión...")
    elif option == "2":
        print("Registrando usuario...")
    else:
        print("Opción inválida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()
