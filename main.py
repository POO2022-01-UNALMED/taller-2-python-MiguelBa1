class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "amarillo", "verde", "negro", "blanco"]:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro
        
    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        return len(list(filter(lambda x: x != None, self.asientos)))

    def verificarIntegridad(self):
        valido = True
        for asiento in self.asientos:
            if asiento != None:
                if asiento.registro != self.registro:
                    valido = False

        if self.motor.registro != self.registro:
            valido = False
        
        return "Auto original" if valido else "Las piezas no son originales" 