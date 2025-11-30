class Estudiante:

    def __init__(self):

        self.nombre = ""
        self.edad = 0
        self.matricula = ""
        self.promedio = 0.0
        self.activo = True

estudiante1 = Estudiante()

estudiante1.nombre = "Carlos Méndez"
estudiante1.edad = 20
estudiante1.matricula = "EST-2024-001"
estudiante1.promedio = 8.5
estudiante1.activo = True

print("=" * 40)
print("INFORMACIÓN DEL ESTUDIANTE")
print("=" * 40)
print(f"Nombre: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad} años")
print(f"Matrícula: {estudiante1.matricula}")
print(f"Promedio: {estudiante1.promedio}")
print(f"Estado: {'Activo' if estudiante1.activo else 'Inactivo'}")
print("=" * 40)

print("\nActualizando información...")
estudiante1.promedio = 9.0
estudiante1.edad = 21

print(f"\nNuevo promedio: {estudiante1.promedio}")
print(f"Nueva edad: {estudiante1.edad} años")