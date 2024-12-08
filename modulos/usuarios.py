class Usuario:
    def __init__(self, nombre, usuario, contrasena, telefono, cedula, rol):
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.telefono = telefono
        self.cedula = cedula
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Usuario: {self.usuario}"
    
    def mostrar_informacion(self):
        return (f"Nombre: {self.nombre}\n"
                f"Usuario: {self.usuario}\n"
                f"Contraseña: {self.contrasena}\n"
                f"Teléfono: {self.telefono}\n"
                f"Cédula: {self.cedula}")

    def cambiar_contrasena(self, nueva_contrasena):
        if len(nueva_contrasena) < 4:
            return "La nueva contraseña debe tener al menos 4 caracteres."
        self.contrasena = nueva_contrasena
        return "Contraseña actualizada con éxito."

    def actualizar_telefono(self, nuevo_telefono):
        if not nuevo_telefono.isdigit() or len(nuevo_telefono) != 9:
            return "El número de teléfono debe contener 9 dígitos."
        self.telefono = nuevo_telefono
        return f"Número de teléfono actualizado a: {self.telefono}"

class Empleado(Usuario):
    def __init__(self, nombre, usuario, contrasena, telefono, cedula, num_funcionario):
        super().__init__(nombre, usuario, contrasena, telefono, cedula, "Empleado")
        self.num_funcionario = num_funcionario

    def mostrar_num_funcionario(self):
        return f"Numero de funcionario: {self.num_funcionario}"
    
class Cliente(Usuario):
    def __init__(self, nombre, usuario, contrasena, telefono, cedula, puntos=0):
        super().__init__(nombre, usuario, contrasena, telefono, cedula, "Cliente")
        self.puntos = puntos

    def acumular_puntos(self, cantidad):
        self.puntos += cantidad
        return f"Puntos acumulados: {self.puntos}"
class Administrador(Usuario):
    def __init__(self, nombre, usuario, contrasena, telefono, cedula, permisos=[]):
        super().__init__(nombre, usuario, contrasena, telefono, cedula, "Administrador")
        self.permisos = permisos

    def agregar_permiso(self, permiso):
        if permiso not in self.permisos:
            self.permisos.append(permiso)
        return f"Permisos actuales: {', '.join(self.permisos)}"
