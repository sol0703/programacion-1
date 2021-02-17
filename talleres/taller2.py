# Constante
PREGUNTA_NOMBRE = "Como te llamas? : "
MENSAJE_SALUDO = "Un gusto conocerte "
ENUNCIADO = "Ayudanos a llenar el siguiente formato "
PREGUNTA_NUMEROA = "Ingrese un numero A "
PREGUNTA_NUMEROB = "Ingrese un numero B "

# Entrada al codigo
nombre = input (PREGUNTA_NOMBRE)
print (MENSAJE_SALUDO, nombre)
print (ENUNCIADO)
numeroA = int (input (PREGUNTA_NUMEROA))
numeroB = int (input (PREGUNTA_NUMEROB))
isNumeroMayor = numeroA > numeroB
print (isNumeroMayor)
isNumeroMayorIgual = numeroA >= numeroB
print (isNumeroMayorIgual)
isNumeroMenor = numeroA < numeroB
print (isNumeroMenor)
isNumeroDiferentes = numeroA != numeroB
print (isNumeroDiferentes)
isNumerosIguales = numeroA == numeroB
print (isNumerosIguales)

# Operaciones
sumar = numeroA + numeroB
print (f"la suma dio {sumar} exitosamente")
restar = numeroA - numeroB
print(f"la resta dio {restar} exitosamente")
multiplicar = numeroA * numeroB
print(f"la multiplicar dio {multiplicar} exitosamente")
dividir = numeroA / numeroB
print(f"la dividir dio {dividir} exitosamente")
exponente = numeroA ** numeroB
print(f"la exponente dio {exponente} exitosamente")