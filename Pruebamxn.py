import math

class Matriz:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matriz = []

    def generar_matriz(self):
        self.matriz = [[(i * self.n) + j + 1 for j in range(self.n)] for i in range(self.m)]

    def run_matriz(self):
        valores = []
        for j in range(self.n):
            if j % 2 == 0:  # Columnas impares (considerando 0-based index)
                for i in range(self.m - 1, -1, -1):  # Mover hacia arriba
                    valores.append(self.matriz[i][j])
            else:  # Columnas pares
                for i in range(self.m):  # Mover hacia abajo
                    valores.append(self.matriz[i][j])
        return valores

class Resultados:
    @staticmethod
    def son_primos(numero):
        if numero <= 1:
            return False
        for i in range(2, int(math.sqrt(numero)) + 1):
            if numero % i == 0:
                return False
        return True 

    @staticmethod
    def impares(valores):
        return len([x for x in valores if x % 2 != 0])

    @staticmethod
    def ordenar(valores):
        ascendente = sorted(valores)
        descendente = sorted(valores, reverse=True)
        return ascendente, descendente

def main():
    while True:
        try:
            m = int(input("Ingrese el número de filas: "))
            n = int(input("Ingrese el número de columnas: "))

            if m <= 0 or n <= 0:
                raise ValueError("Las dimensiones deben ser mayores que 0.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, ingrese números enteros positivos.")

    matriz = Matriz(m, n)
    matriz.generar_matriz()
    valores = matriz.run_matriz()
    
    print("Valores en su recorrido:", valores)

    primos = [numero for numero in valores if Resultados.son_primos(numero)]
    print("Números primos:", primos)

    impares = Resultados.impares(valores)
    print("Cantidad de números impares:", impares)

    ascendente, descendente = Resultados.ordenar(valores)
    print("Números ordenados de menor a mayor:", ascendente)
    print("Números ordenados de mayor a menor:", descendente)

if __name__ == "__main__":
    main()
