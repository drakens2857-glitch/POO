class Estudiante:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.promedio = 0.0
        self.materias = []
        self.activo = True
        self.creditos = 0

    def agregar_materia(self, materia):
        self.materias.append(materia)
        print(f"Materia '{materia}' agregada a {self.nombre}")

    def mostrar_info(self):
        print(f"\n=== INFORMACIÓN DEL ESTUDIANTE ===")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Promedio: {self.promedio}")
        print(f"Materias: {self.materias}")
        print(f"Activo: {self.activo}")
        print(f"Créditos: {self.creditos}")


print("=== CREANDO ESTUDIANTES PERSONALIZADOS ===")
estudiante1 = Estudiante("Ana García", 20)
estudiante2 = Estudiante("Carlos López", 22)
estudiante3 = Estudiante("María Rodríguez", 19)

estudiante1.mostrar_info()
estudiante2.mostrar_info()
estudiante3.mostrar_info()

print("\n=== PERSONALIZANDO ESTUDIANTES ===")
estudiante1.promedio = 8.5
estudiante1.creditos = 45
estudiante1.agregar_materia("Matemáticas")
estudiante1.agregar_materia("Física")

estudiante2.promedio = 9.2
estudiante2.creditos = 60
estudiante2.agregar_materia("Programación")
estudiante2.agregar_materia("Base de Datos")

estudiante3.promedio = 7.8
estudiante3.creditos = 30
estudiante3.agregar_materia("Historia")

print("\n=== INFORMACIÓN ACTUALIZADA ===")
estudiante1.mostrar_info()
estudiante2.mostrar_info()
estudiante3.mostrar_info()

print("\n=== INDEPENDENCIA DE OBJETOS ===")
print(f"¿Son el mismo estudiante? {estudiante1 is estudiante2}")
print(f"Estudiante 1 tiene {len(estudiante1.materias)} materias")
print(f"Estudiante 2 tiene {len(estudiante2.materias)} materias")
