class Persona:

    def __init__(self):
        self.nombre = "Sin nombre"
        self.edad = 0
        self.activo = True
        self.altura = 0.0
        self.hobbies = []

print("=== CREACIÓN DE PERSONA ===")
persona1 = Persona()

print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1.edad}")
print(f"Activo: {persona1.activo}")
print(f"Altura: {persona1.altura}")
print(f"Hobbies: {persona1.hobbies}")

print("\n=== MODIFICANDO ATRIBUTOS ===")
persona1.nombre = "Ana García"
persona1.edad = 25
persona1.altura = 1.65
persona1.hobbies = ["leer", "nadar", "programar"]

print(f"Nombre actualizado: {persona1.nombre}")
print(f"Edad actualizada: {persona1.edad}")
print(f"Altura actualizada: {persona1.altura}")
print(f"Hobbies actualizados: {persona1.hobbies}")

print("\n=== SEGUNDA PERSONA ===")
persona2 = Persona()
persona2.nombre = "Carlos López"
persona2.edad = 30
persona2.activo = False
persona2.altura = 1.80

print(f"Persona 2 - Nombre: {persona2.nombre}")
print(f"Persona 2 - Edad: {persona2.edad}")
print(f"Persona 2 - Activo: {persona2.activo}")
print(f"Persona 2 - Altura: {persona2.altura}")

print("\n=== INDEPENDENCIA DE OBJETOS ===")
print(f"¿Son la misma persona? {persona1 is persona2}")
print(f"Nombre persona1: {persona1.nombre}")
print(f"Nombre persona2: {persona2.nombre}")
