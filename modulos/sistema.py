from .usuarios import Usuario, Cliente, Empleado, Administrador
import pickle
class Sistema:
    def __init__(self):
        self.bd = {}
    
    def __str__(self):
        return
    
    def registro(self, nombre, usuario, contrasena, telefono, cedula, rol, extra):
        if usuario in self.bd:
            return f"Error: El usuario '{usuario}' ya existe."
        
        if rol == "1":  # Empleado
            num_funcionario = extra
            nuevo_empleado = Empleado(nombre, usuario, contrasena, telefono, cedula, num_funcionario)
            self.bd[usuario] = nuevo_empleado
            return f"Empleado '{usuario}' registrado con éxito."
        
        elif rol == "2":  # Cliente
            puntos = int(extra)
            nuevo_cliente = Cliente(nombre, usuario, contrasena, telefono, cedula, puntos)
            self.bd[usuario] = nuevo_cliente
            return f"Cliente '{usuario}' registrado con éxito."
        
        elif rol == "3":  # Administrador
            permisos = extra.split(",")  # Permisos separados por coma
            nuevo_administrador = Administrador(nombre, usuario, contrasena, telefono, cedula, permisos)
            self.bd[usuario] = nuevo_administrador
            return f"Administrador '{usuario}' registrado con éxito."
        
        else:
            return "Error: Rol no válido."
    
    def mostrar_usuarios(self):
        if not self.bd:
            return "No hay usuarios registrados."
        usuarios_info = []
        for usuario in self.bd.values():
            rol = usuario.__class__.__name__
            usuarios_info.append(f"Rol: {rol} - {str(usuario)}")
        return "\n".join(usuarios_info)
    
    def login(self, usuario, contrasena):
        cliente = self.bd.get(usuario)
        if not cliente:
            return "Error: Usuario no encontrado."
        if cliente.contrasena != contrasena:
            return "Error: Contraseña incorrecta."
        return f"Bienvenido, {cliente.nombre}!"
    
    def guardar_usuarios(self, archivo="usuarios.txt"):
        try:
            with open(archivo, "wb") as file:
                pickle.dump(self.bd, file)
            return f"Usuarios guardados en {archivo}."
        except Exception as e:
            return f"Error al guardar los usuarios: {e}"
        
    def cargar_usuarios(self, archivo="usuarios.txt"):
        try:
            with open(archivo, "rb") as file:
                self.bd = pickle.load(file)
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado. Iniciando con una base de datos vacía.")
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")

