"""Tarea: Implementar un sistema de Gestion de empleados, 
Clase base: empleado. Atributos privados: Nombre y ID
Clases derivadas: 
    empleado regular. Atributos privados: salario anual
    gerente.  Atributos privados: salario anual y bono
    trabajador por hora. Atributos privados:tarifa por hora y horas trabajadas
Metodos: registrar horas de trabajo y calcular pago

Nosotros definimos que metodos usar para cada tipo de empleado
Crear insrtancias de cada tipo y mostrar el calculo del pago"""


from abc import ABC, abstractmethod #Para crear clases y metodos abstractos
#import math #modulo para operar operaciones matematicas

class Empleado(ABC):
    def __init__(self, nombre, ID, salario_mensual = 0):
        self.nombre = nombre
        self.ID = ID
        self.salario_mensual = salario_mensual
        
    def GetSalario(self):
      return self.salario_mensual
    
    @abstractmethod
    def calcular_pago(self):
        pass

    @abstractmethod
    def calcular_salario_anual(self):
        pass


    
class Empleado_regular(Empleado):
   def __init__(self, nombre, ID, salario_mensual):
       super(). __init__(nombre, ID, salario_mensual)
              
       
   def calcular_pago(self):
        return self.calcular_salario_anual()

   def calcular_salario_anual(self):
        salario_anual = super().GetSalario() * 12
        return salario_anual
    
    
class Gerente(Empleado):
   def __init__(self, nombre, ID, salario_mensual, bono):
       super(). __init__(nombre, ID, salario_mensual)
       self.bono = bono
       
   def calcular_pago(self):
        return self.calcular_salario_anual()
      
   def calcular_salario_anual(self):
        salario_anual = (self.GetSalario() * 12) + self.bono
        return salario_anual
    
    
class Trabajador_hora(Empleado):
   def __init__(self, nombre, ID, tarifa_hora, horas_trabajadas):
       super(). __init__(nombre, ID)
       self.tarifa_hora = tarifa_hora
       self.horas_trabajadas = horas_trabajadas
       
   def calcular_salario_mensual(self):
      salario_diario = self.tarifa_hora * self.horas_trabajadas
      salario_mensual = salario_diario * 30
      return salario_mensual
      
   def calcular_pago(self):
        return self.calcular_salario_anual()
      
   def calcular_salario_anual(self):
        salario_anual = self.calcular_salario_mensual() * 12
        return salario_anual
    

empleadoRegular = Empleado_regular("Jose", "152625", 1)
gerente = Gerente ("Sonia", "763272", 5000000, 300000)
trabajadorHora = Trabajador_hora("Lucia", "347834", 10000, 8)

print(f"El pago del empleado regular es: {empleadoRegular.calcular_pago():.2f}") 
print(f"El pago del gerente es: {gerente.calcular_pago():.2f}")
print(f"El area del trabajador por hora es: {trabajadorHora.calcular_pago():.2f}")

