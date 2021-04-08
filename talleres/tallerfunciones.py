# Punto 1
def mostrarLista (lista):
    for elemento in lista :
        print (elemento)

edades = [17,18,20,22,19]
nombres = ['Daniela','Santiago','Andrea','Isabella','Paula']
mostrarLista(edades)
mostrarLista(nombres)

# Punto 2
numeroEntero = [17,18,20,22,19]
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

# Punto 3
def saludar (cantidad = 0):
    print ('Buenos Dias '* cantidad)
saludar (7)

# Punto 4
numeroEntero = [17,18,20,22,19]
def ListaPar (lista):
    Par = []
    for elemento in lista:
        if elemento % 2 == 0 :
            Par.append (elemento)
    return Par

numeroPar = ListaPar (numeroEntero)
print (numeroPar)

# Punto 5
numeroEntero = [17,18,20,22,19]
def ListaMayor (lista):
    Mayor = []
    for elemento in lista:
        if elemento > 24 :
            Mayor.append (elemento)
    return Mayor

numeroMayor = ListaMayor(numeroEntero)
print (numeroMayor)

# Punto 6
def calcularIMC (peso, altura):
    return peso / (altura**2)
IMC = calcularIMC (69, 1.63)
print (IMC)

# Punto 7
def Adios ():
    print ("Ojala haya aprendido algo nuevo ")
Adios ()
print( 'Hasta la proxima')