class MiPrimeraClase:
    
    pass

print("=== VERIFICACIÓN DE LA CLASE ===")
print(f"Nombre de la clase: {MiPrimeraClase.__name__}")
print(f"Tipo de la clase: {type(MiPrimeraClase)}")
print(f"Documentación: {MiPrimeraClase.__doc__}")

mi_objeto = MiPrimeraClase()
print(f"\nObjeto creado: {mi_objeto}")
print(f"Tipo del objeto: {type(mi_objeto)}")
print(f"ID único del objeto: {id(mi_objeto)}")
print(f"¿Es instancia de MiPrimeraClase? {isinstance(mi_objeto, MiPrimeraClase)}")
