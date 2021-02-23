# Quiz numero 1
# Constantes
MENSAJE_SALUDO = "Buenos dias, hoy vamos a analizar tu valor de trigliceridos y de homocisteina"
MENSAJE_1 = "Ingrese su valor respectivo de su exmanen de trigliceridos :"
MENSAJE_2 = "Ingrese el numero respectivo de su examen de homocisteina :"
MENSAJE_OPTIMO_TRIGLICERIDOS = "Su valor de trigliceridos esta optimo"
MENSAJE_SOBRE_EL_LIMITE_OPTICO_TRIGLICERIDOS = "Su valor de trigliceridos esta sobre el limite optico"
MENSAJE_ALTO_TRIGLICERIDOS = "Su valor de trigliceridos esta alto"
MENSAJE_MUY_ALTO_TRIGLICERIDOS = "Su valor de trigliceridos esta muy alto"
MENSAJE_OPTIMO_HOMOCISTEINA = "Su valor de homocisteina esta optimo"
MENSAJE_SOBRE_EL_LIMITE_OPTIMO_HOMOCISTEINA = "Su valor de homocisteina esta sobre el limite optimo"
MENSAJE_ALTO_HOMOCISTEINA = "Su valor de homocisteina esta alto"
MENSAJE_MUY_ALTO_HOMOCISTEINA = "Su valor de homocisteina esta muy alto"

# Entrada de codigo
print (MENSAJE_SALUDO)
triglicerido = int (input (MENSAJE_1))
homocisteina = int (input (MENSAJE_2))
isOptimoTrigliceridos = triglicerido < 150
isSobreElLimiteOptimoTrigliceridos = triglicerido >= 150 and triglicerido <= 199
isAltoTrigliceridos = triglicerido >= 200 and triglicerido <= 499 
isMuyAltoTrigliceridos = triglicerido < 500
isOptimoHomocisteina = homocisteina >= 2 and homocisteina < 15
isSobreElLimiteHomocisteina = homocisteina >= 15 and homocisteina < 30
isAltoHomocisteina = homocisteina >= 30 and homocisteina <= 100
isMuyAltoHomocisteina = homocisteina > 100

if (isOptimoTrigliceridos):
    print (MENSAJE_OPTIMO_TRIGLICERIDOS)
elif (isSobreElLimiteOptimoTrigliceridos):
    print (MENSAJE_SOBRE_EL_LIMITE_OPTICO_TRIGLICERIDOS)
elif (isAltoTrigliceridos):
    print (MENSAJE_ALTO_TRIGLICERIDOS)
else :
    print (MENSAJE_MUY_ALTO_TRIGLICERIDOS)

if (isOptimoHomocisteina):
    print (MENSAJE_OPTIMO_HOMOCISTEINA)
elif (isSobreElLimiteHomocisteina):
    print (MENSAJE_SOBRE_EL_LIMITE_OPTIMO_HOMOCISTEINA)
elif (isAltoHomocisteina):
    print (MENSAJE_ALTO_HOMOCISTEINA)
else :
    print (MENSAJE_MUY_ALTO_HOMOCISTEINA)