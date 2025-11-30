class Calculadora:

    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        print(f"Calculando {a} + {b}...")
        self.resultado = a + b
        return self.resultado

    def mostrar_resultado(self):
        print(f"El último resultado es: {self.resultado}")


print("=== INICIALIZANDO CALCULADORA ===")
mi_calculadora = Calculadora()
mi_calculadora.mostrar_resultado()

print("\n=== REALIZANDO SUMAS ===")
suma1 = mi_calculadora.sumar(10, 5)
print(f"Suma de 10 y 5: {suma1}")
mi_calculadora.mostrar_resultado()

suma2 = mi_calculadora.sumar(20, -7)
print(f"Suma de 20 y -7: {suma2}")
mi_calculadora.mostrar_resultado()

print("\n=== OTRAS OPERACIONES ===")
mi_calculadora.sumar(100, 25)
mi_calculadora.mostrar_resultado()
