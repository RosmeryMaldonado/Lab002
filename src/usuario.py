class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_edad(self):
        if self.edad >=18 :
            return True
        return False

    def actualizar_edad(self, nueva_edad):
        pass