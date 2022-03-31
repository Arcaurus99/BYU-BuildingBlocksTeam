
def squareArea(lado):
    area_cuadrado = lado ** 2
    print(f"The area of the square is {area_cuadrado}")

def suma(a : int, b : int):
    resultado = a + b
    print(resultado)

if __name__ == '__main__':
    # entrada_lado = int(input('Insert value of the side: '))
    # squareArea(entrada_lado)

    valor_A = int(input('Ingresa el valor A: '))
    valor_B = int(input('Ingresa el valor B: '))
    suma(valor_A, valor_B)
