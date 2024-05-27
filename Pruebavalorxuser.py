import math


class Matriz: # esta clase maneja la manipulacion y creacion de la matriz

    def __init__(self, m,n): # constructor de la clase y inicia las dimensiones
        self.m=m # filas 
        self.n=n # columnas 
        self.matriz=[]  # creo una lista vacia para almacenar los valores de m y n

    def read_matriz(self):
        # leer los valores de la matriz de la dimension M x N 
        print("ingrese los valores de la matriz:")
        for i in range (self.m):        
            fila=[] 
            for j in range( self.n):    
                while True:
                    try:
                        valor=int(input(f"valor para posicion ({i},{j}): "))
                        fila.append(valor)
                        break
                    except  ValueError:
                        print("Entrada Invalida. por favor, ingrese un numero entero")
            self.matriz.append(fila)
            
    def run_matriz(self):
        valores = []
        for j in range(self.n):
            if j % 2 != 0:  # Columnas pares
                for i in range(self.m):
                    valores.append(self.matriz[i][j])
                if j + 1 < self.n:  # Mover hacia la derecha si es posible
                    valores.append(self.matriz[self.m - 1][j + 1])
            else:  # Columnas impares
                for i in range(self.m - 1, -1, -1):  # Mover hacia arriba
                    valores.append(self.matriz[i][j])
                if j + 1 < self.n:  # Mover hacia la derecha si es posible
                    valores.append(self.matriz[0][j + 1])
        return valores
class Resultados:
    @staticmethod
    def son_primos(numero):
        # aca miramos si es un numero es primo 
        if numero <= 1:
            return False
        for i in range (2, int(math.sqrt(numero))+1):
            if numero % i == 0:
                return False                
        return True 

    @staticmethod
    def impares(valores):
        # contamos la cantidad de impares
        return len([x for x in valores if x % 2 != 0])

    @staticmethod
    def ordenar (valores):
        # ordenamos los valores de menor a mayor y mayor a menor 
        menor=sorted(valores)
        mayor= sorted(valores, reverse=True)

        return menor,mayor
def main():
    while True:
        try:
            m=int(input(" ingrese el numero de filas: "))
            n=int(input("ingrese el numero de columnas: "))

            if m<= 0  or n <=0:
                raise  ValueError ("las dimensiones deben ser mayor que 0 ")
            break

        except ValueError  as e:
            print(f"entrada invalida: {e}. por ingrese un numero positivo")

        # llamamos nuestras clases y metodos
    matriz= Matriz(m,n)
    matriz.read_matriz()
    valores= matriz.run_matriz()
    
    print("valores de su recorrido: ", valores)

    primos = [numero for numero in valores if Resultados.son_primos(numero)]
    print("Números primos:", primos)

    impares = Resultados.impares(valores)

    print("cantidad de numeros impares: ", impares)
    menor, mayor = Resultados.ordenar(valores)

    print("Numeros ordenados ascendente a descendente", menor)
    print("Numeros ordenados descendente a ascendente", mayor)

if __name__ == "__main__":
    main()     