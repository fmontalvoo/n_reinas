import sys
from tablero import Tablero

if __name__ == "__main__":
    args = sys.argv
    n = int(args[1]) if len(args) > 1 else int(input('Ingresa cantidad de reinas: '))
    tablero = Tablero(ancho=800, alto=700, n=n)
    tablero.n_reinas.imprimir_tablero()
    tablero.ejecutar()