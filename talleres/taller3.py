# Ejercicio 1
print ("ejecicio1")
# Constantes
MENSAJE_SALUDO = "Hola profe, espero que este bien"
PREGUNTA_NUMERO_1 = "Ingrese un numero A: "
PREGUNTA_NUMERO_2 = "Ingrese un numero B: "
MENSAJE_MAYOR =  "El numero A es mayor que el numero B"
MENSAJE_IGUAL = "A y B son iguales"
MENSAJE_MAYOR_2 = "El numero B es mayor que el numero A"

# Entrada de codigo
print (MENSAJE_SALUDO)
NumeroA = int (input (PREGUNTA_NUMERO_1))
NumeroB = int (input (PREGUNTA_NUMERO_2))
isMayor = NumeroA > NumeroB
isIguales = NumeroA == NumeroB
if (isMayor):
    print (MENSAJE_MAYOR)
elif (isIguales):
    print (MENSAJE_IGUAL)
else:
    print (MENSAJE_MAYOR_2)

# Ejercicio 2
print ("ejercicio2")
# Constantes
MENSAJE_EDAD = "Cuantos años tienes? :"
MENSAJE_MENOR_EDAD = "Eres aun un pollito"
MENSAJE_JOVEN = "Eres persona joven"
MENSAJE_ADULTO = "Eres una persona ya adulta"
MENSAJE_ADULTO_MAYOR = "Eres un adulto mayor"

# Entrada de codigo
Edad = int (input (MENSAJE_EDAD))
isMenorEdad = Edad < 18
isJoven = Edad >= 18 and Edad <= 25
isAdulto = Edad >= 25 and Edad <= 60
isAdultoMayor = Edad > 60
if (isMenorEdad):
    print (MENSAJE_MENOR_EDAD)
elif (isJoven):
    print (MENSAJE_JOVEN)
elif (isAdulto):
    print (MENSAJE_ADULTO)
else:
    print (MENSAJE_ADULTO_MAYOR)

# Ejercicio 3
print ("ejercico3")
# Contantes
PREGUNTA_AÑO_ACTUAL = "Ingrese año actual, pliiisss: "
PREGUNTA_CUALQUIER_AÑO = "Ingrese el año que usted quiera, pliiiiisss: "

# Entrada codigo
AñoActual = int (input (PREGUNTA_AÑO_ACTUAL))
CualquierAño = int (input (PREGUNTA_CUALQUIER_AÑO))
isAñoMayor = CualquierAño > AñoActual
isAñoMayor2 = AñoActual > CualquierAño
if (isAñoMayor):
    resta = CualquierAño - AñoActual
    print (f"Faltan {resta} años para llegar")
elif (isAñoMayor2):
    resta2 = AñoActual - CualquierAño
    print (f"Han pasado {resta2} años")
else:
    print ("Los años son iguales")

# Ejercicio 4
print ("ejercicio4")
# Constantes
preguntaMedida = 'ingrese una medida en centimetros : '
preguntaUnidad = ''' ingrese en que unidades desea transformar :
    K - Kilometros
    M - Metros 
    mm -milimetros
'''
mensajeError = 'Entrada no válida'

# Entrada de codigo
medida = float(input(preguntaMedida))
unidad = input(preguntaUnidad)
metros = medida / 100
kilometros = medida / 100000
milimetros = medida *10
if (unidad == 'K'):
    print (kilometros)
elif (unidad == 'M'):
    print (metros)
elif (unidad == 'mm'):
    print (milimetros)
else:
    print (mensajeError)

print ("FIN")