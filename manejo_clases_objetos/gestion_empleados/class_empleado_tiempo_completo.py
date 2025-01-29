from class_empleado import Empleado


class EmpleadoTiempoCompleto(Empleado):

    def __init__(self, nombre, apellido, salario_base, bono_anual):
        super().__init__(nombre, apellido, salario_base)
        self.bono_anual = bono_anual

    def calcular_salario(self):
        return self.salario_base + self.bono_anual
    
    