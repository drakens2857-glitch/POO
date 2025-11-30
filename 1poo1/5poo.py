class Perro:

    def __init__(self):
        self.nombre = "Firulais"
        self.energia = 100

    def ladrar(self):
        if self.energia >= 5:
            print(f"{self.nombre} dice: ¡Guau! (Energía: {self.energia})")
            self.energia -= 5
        else:
            print(f"{self.nombre} está demasiado cansado para ladrar... (Energía: {self.energia})")


print("=== CREANDO UN PERRO ===")
mi_perro = Perro()

print(f"Nombre del perro: {mi_perro.nombre}")
print(f"Energía inicial: {mi_perro.energia}\n")

print("=== EL PERRO EMPIEZA A LADRAR ===")
mi_perro.ladrar()
print(f"Energía después del primer ladrido: {mi_perro.energia}\n")

mi_perro.ladrar()
print(f"Energía después del segundo ladrido: {mi_perro.energia}\n")

print("=== CAMBIANDO EL NOMBRE DEL PERRO ===")
mi_perro.nombre = "Max"
print(f"Nuevo nombre del perro: {mi_perro.nombre}")
mi_perro.ladrar()
print(f"Energía: {mi_perro.energia}\n")

print("=== EL PERRO SE CANSA ===")
for _ in range(15):
    mi_perro.ladrar()
