# Entradas
MENSAJE_SALUDO = 'Bienvenido a este programa, juguemos'
PREGUNTAR_NUMERO  =  'En este juego debes acertar un numero entero que va desde el 1-10, la idea es que lo puedes intentar las veces que quieras ... Muchos exitos, ingresa tu numero:'
PREGUNTA_FALLIDA  =  '¡Aaaah! Fallaste, ingrese otro numero: '
MENSAJE_GANASTE  =  'Felicidades ganaste !!'
MENSAJE_PERDISTE  =  'Perdiste, vuelve a intentarlo !!'

# Entrada al codigo
NumeroOculto = 7
vidas = 5
print (MENSAJE_SALUDO)
NumeroIngresado = int (input (PREGUNTA_FALLIDA))
if (NumeroIngresado != NumeroOculto):
    vidas -=1
while (NumeroOculto != NumeroIngresado and vidas >0):
    NumeroIngresado = int (input (PREGUNTA_FALLIDA))
    vidas -=1

if (vidas >=0 and NumeroOculto == NumeroIngresado):
    print (MENSAJE_GANASTE)
    print (vidas)
else:
    print (MENSAJE_PERDISTE, 'El numero era el', NumeroOculto)