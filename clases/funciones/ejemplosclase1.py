guardar = print ('hola')
print (guardar)

guardar = round(14.2534897,2)
print (guardar)

def linedesign (cantidad,simbolo):
    print (simbolo*cantidad)
    return None

linedesign(30,'#')
linedesign(10,'*')
linedesign(100,'°')

# Muestra la lista 
def mostrarLista(listaEntrada):
    for elemento in listaEntrada:
        print (elemento)
    return None
lista = [213,32,23123,321,321,233,1232,23]
lista2 = [564654,645,64543.2565,547,57865]
linedesign(30,'°')
mostrarLista(lista)
linedesign(30,'*')
mostrarLista(lista2)

# Sumar dos numeros
def sumar (a = 0,b = 0):
    suma = a + b
    return suma
linedesign(30,'*')
resultado = sumar()
print (resultado)
print (sumar(12,14))

# Restar dos numeros
def restar (a = 0,b = 0):
    resta = a - b
    return resta

# Multiplicar dos numeros
def multiplicar (a = 0,b = 0):
    multiplica = a * b
    return multiplica

# Dividir dos numeros
def dividir (a = 0,b = 1):
    dividi = a / b
    return dividi

# Potenciar dos numeros 
def potenciar (base = 0,exponente = 0):
    potencia = base ** exponente
    return potencia

# Funciones dependientes de otras
def calcular (operacion, numeroA, numeroB):
    print (operacion(numeroA,numeroB))


baseIngresada = int (input('Ingrese una base entera :'))
exponenteIngresada = int (input('Ingrese una exponente entero :'))

print (restar(83,87))
print (multiplicar(83,87))
print (dividir(83,87))
print (dividir())
print (potenciar(5,6))

calcular (multiplicar,63,67)