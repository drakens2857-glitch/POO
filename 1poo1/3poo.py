class Vehiculo:

    pass

print("=== CREACIÓN DE OBJETOS ===")
auto1 = Vehiculo()
auto2 = Vehiculo()
auto3 = Vehiculo()
auto4 = Vehiculo()

print(f"Objeto auto1: {auto1}")
print(f"Objeto auto2: {auto2}")
print(f"Objeto auto3: {auto3}")
print(f"Objeto auto4: {auto4}\n")

print("=== IDENTIDAD Y TIPO ===")
print(f"ID de auto1: {id(auto1)}")
print(f"ID de auto2: {id(auto2)}")
print(f"ID de auto3: {id(auto3)}")
print(f"ID de auto4: {id(auto4)}\n")

print(f"Tipo de auto1: {type(auto1)}")
print(f"Tipo de auto2: {type(auto2)}\n")

print(f"¿Es auto1 una instancia de Vehiculo? {isinstance(auto1, Vehiculo)}")
print(f"¿Es 'cadena' una instancia de Vehiculo? {isinstance('cadena', Vehiculo)}\n")

print("=== COMPARACIÓN DE OBJETOS ===")
print(f"¿auto1 es auto2? {auto1 is auto2}")
print(f"¿auto1 es auto3? {auto1 is auto3}")
print(f"¿auto1 es auto1? {auto1 is auto1}\n")

print(f"¿auto1 == auto2? {auto1 == auto2}")
print(f"¿auto1 == auto1? {auto1 == auto1}\n")

otro_auto_1 = auto1
print(f"ID de otro_auto_1: {id(otro_auto_1)}")
print(f"¿auto1 es otro_auto_1? {auto1 is otro_auto_1}")
print(f"¿auto1 == otro_auto_1? {auto1 == otro_auto_1}\n")

print("Los IDs son únicos para cada objeto creado, incluso si provienen de la misma clase.")
print("Cada vez que se llama a Vehiculo() se crea un nuevo objeto en memoria.")
