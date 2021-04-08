# Punto 1
# Sumar dos numeros
def sumar (a = 0,b = 0,c = 0):
    suma = a + b + c
    return suma

# Restar dos numeros
def restar (a = 0,b = 0,c = 0):
    resta = a - b - c
    return resta

# Multiplicar dos numeros
def multiplicar (a = 0,b = 0,c = 0):
    multiplica = a * b * c
    return multiplica

# Dividir dos numeros
def dividir (a = 0,b = 1,c = 1):
    dividi = a / b / c
    return dividi

# Potenciar dos numeros 
def potenciar (base = 0,exponente = 0,exponente2 = 0):
    potencia = base ** exponente ** exponente2
    return potencia

print (sumar(23,2,76))
print (restar(12,54,3))
print (multiplicar(3,5,10))
print (dividir(100,3,7))
print (potenciar(3,5,2))

# Punto 2
def mostrarLista (lista):
    for elemento in lista :
        print (elemento)

numero1 = [1,2,3,4,5]
numero2 = [6,7,8,9,10]
numero3 = [11,12,13,14,15]
mostrarLista(numero1)
mostrarLista(numero2)
mostrarLista(numero3)

# Punto 3
def area (base = 0,altura = 0):
    Triangulo = (base*altura)/2
    return Triangulo

def calcular (operacion,numeroA,numeroB):
    print (operacion(numeroA,numeroB))
baseIngresada = int (input('Ingrese el numero entero de la base del triangulo : '))
alturaIngresada = int (input('Ingrese el numero entero de la altura del triangulo :'))
print (area(baseIngresada,alturaIngresada))

# Punto 4
numeroEntero = [123,53,983,2,634,87,10,432,5]
def informaList (lista):
    mayor = max (lista)
    menor = min (lista)
    acumulador = 0
    for elemento in lista :
        acumulador += elemento
    sizeList =   len (lista)
    promedio = acumulador / sizeList
    print (f'el número mayor en la lista es el {mayor}, el menor {menor} y el promedio {promedio}')
informaList (numeroEntero)

# Punto 5
