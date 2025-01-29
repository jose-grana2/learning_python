from class_empleado_tiempo_completo import EmpleadoTiempoCompleto
from class_empleado_tiempo_parcial import EmpleadoTiempoParcial

#ejemplo tiempo completo
empleado_tiempo_completo = EmpleadoTiempoCompleto('Juan', 'Marín', 70000, 400)
print('Salario total del empleado a tiempo completo:', empleado_tiempo_completo.calcular_salario())

empleado_tiempo_parcial = EmpleadoTiempoParcial('Juan', 'Marín', 50, 40)
print('Salario total del empleado a tiempo parcial:', empleado_tiempo_parcial.calcular_salario())


