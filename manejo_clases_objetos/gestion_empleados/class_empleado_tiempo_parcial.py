from class_empleado import Empleado

class EmpleadoTiempoParcial(Empleado):

    def __init__(self, nombre, apellido, salario_base, horas_trabajadas):
        super().__init__(nombre, apellido, salario_base)
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return (self.salario_base * self.horas_trabajadas * 4 * 12 )
        