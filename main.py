from modulos import Sistema, Usuario, Cliente, Empleado, Administrador
from os import system

def mostrar_titulo(): #Funcion para mostrar titulo del programa
            print("""
    ==============================================
        Gestor de usuarios - Cristian Gonzalez
    ==============================================
     (No olvidar exportar usuarios antes de salir)
    """)
            
def main():
    sistema = Sistema()
    sistema.cargar_usuarios()  # Cargar los usuarios desde el archivo al iniciar
    
    try:
        while True:
            system("cls")
            mostrar_titulo()
            print("1. Registro")
            print("2. Listar usuarios")
            print("3. Login")
            print("4. Exportar usuarios")
            print("5. Salir")
            
            opcion = input("Elige una opción: ")
            
            if opcion == "1":
                rol = input("1. Empleado | 2. Cliente | 3. Admin: ")
                nombre = input("Nombre: ")
                usuario = input("Usuario: ")
                while True:
                    contrasena = input("Contraseña (mayor a 4 caracteres): ")
                    if len(contrasena) <= 4:
                        print("La contraseña debe ser más larga.")
                    else:
                        break
                telefono = input("Teléfono: ")
                cedula = input("Cédula: ")
                
                if rol == "1":  # Empleado
                    num_funcionario = input("Número de funcionario (solo para empleados): ")
                    print(sistema.registro(nombre, usuario, contrasena, telefono, cedula, rol, num_funcionario))
                
                elif rol == "2":  # Cliente
                    puntos = input("Puntos del cliente: ")
                    print(sistema.registro(nombre, usuario, contrasena, telefono, cedula, rol, puntos))
                
                elif rol == "3":  # Administrador
                    permisos = input("Permisos del administrador (separados por coma): ")
                    print(sistema.registro(nombre, usuario, contrasena, telefono, cedula, rol, permisos))
                
                else:
                    print("Rol no válido.")
                
                enter = input("")
            
            elif opcion == "2":
                print("\nClientes registrados:")
                print(sistema.mostrar_usuarios())
                enter = input("")
            
            elif opcion == "3":
                usuario = input("Ingrese el nombre de usuario: ")
                contrasena = input("Ingrese la contraseña: ")
                print(sistema.login(usuario, contrasena))
                enter = input("")
            
            elif opcion == "4":
                archivo = "usuarios.txt"
                print(sistema.guardar_usuarios(archivo))
                enter = input("")
            
            elif opcion == "5":
                print("Saliendo del sistema. ¡Hasta luego!")
                enter = input("")
                break
            
            else:
                print("Opción no válida. Intente nuevamente.")
                enter = input("")
    except:
        print("\n\nSe interrumpio la ejecucion del programa...")

if __name__ == "__main__":
    main()


