# Sumar dos numeros
def sumar (a = 0,b = 0):
    '''
        devuelve la suma de dos numeros a y b
        por defecto a vala cero al igual que b
    '''
    suma = a + b
    return suma

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
