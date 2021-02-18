# Constante
PREGUNTA_PESO = "Cuanto pesas en kg? : "
PREGUNTA_ESTATURA = "Cuanto mides en metros? : "
MENSAJE_BIENVENIDA = "Hola como estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu IMC es ..."
MENSAJE_BAJO_PESO = "Estas pero delgado! !"
MENSAJE_NORMAL = "Estas en forma"
MENSAJE_SOBRE_PESO = "Ten cuidado estas en sobre peso"
MENSAJE_OBESO = "Cuidado estas obeso tu salud corre riesgo"

# Entrada codigo
print (MENSAJE_BIENVENIDA)
peso = float (input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
isBajoPeso = imc < 18.5
isNormal = imc >= 18.5 and imc < 25
isSobrePeso = imc >= 25 and imc < 30
resultado = ""
if (isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isNormal):
    resultado = MENSAJE_NORMAL
elif (isSobrePeso):
    resultado = MENSAJE_SOBRE_PESO
else:
    resultado = MENSAJE_OBESO

print (MENSAJE_DESPEDIDA, imc)
print (resultado)
