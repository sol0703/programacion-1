#Estos son booleans que son variables que solo vale
# verdadero o falso
pruebaV = True
pruebaF = False
print (pruebaV)
print (pruebaF)
pruebaV = pruebaF
print (pruebaV)
edad = 19
estatura = 1.63
peso = 65
NOMBRE = "Sara Osorno"
# mirar si la persona es mayor de 18 años
print ("#"*15,"Mayor Edad", "#"*15)
isMayorEdad = edad >= 18
print (isMayorEdad)
# calcular si la estatura  era menor de la del promedio
print ("#"*15, "Bajo la Estatura promedio", "#"*15)
isMayorEstatura = estatura < 1.70
print (isMayorEstatura)
# Calculando si el peso es diferente de 84
print ("#"*15, "Peso diferente 65",  "#"*15)
isPesoDiferente = peso != 65
print (isPesoDiferente)
# vamos a ver si un apellido esta en el nombre completo
apellido = "Osorno"
isApellido = apellido in NOMBRE
print ("#"*15, "Eata el apellido en el nombre?", "#"*15)
print (isApellido)