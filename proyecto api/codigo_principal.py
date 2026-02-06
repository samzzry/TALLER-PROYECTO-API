from  Base_datos import base_datos
from Empleado_modelo import Empleado_modelo
obj_bd_Empleado_lista = base_datos()
# creo el objeto empleado que voy a agregar
obj_empleado = Empleado_modelo("Juan", "Perez", "123456789", "987654321")
obj_empleado2 = Empleado_modelo("Maria", "Gomez", "987654321", "123456789")
lista_nuevos_modelos = [obj_empleado, obj_empleado2]
obj_bd_Empleado_lista.agregar_empleado(obj_empleado) # guardar un obj
obj_bd_Empleado_lista.agregar_empleado(obj_empleado2)
#lista
obj_bd_Empleado_lista.imprimir_info()
