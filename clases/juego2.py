
import random
# Entradas
MENSAJE_SALUDO = '''
    Bienvenido
        a este programa,
    !!!juguemos!!'''
PREGUNTAR_NUMERO  = '''
        En este juego debes acertar un numero entero 
        que va desde el 1-10, la idea es que 
        lo puedes intentar antes de que se te
        acaben las vidas...no existe vida 0 
        Muchos exitos, ingresa tu numero:
'''
PREGUNTA_DIFICULTAD = '''
    1- Facil
    2- Moderado
    3- Dificil
'''
PREGUNTA_FALLIDA  =  '¡Aaaah! Fallaste, ingrese otro numero: '
MENSAJE_GANASTE  =  'Felicidades ganaste !!'
MENSAJE_PERDISTE  =  'Perdiste, vuelve a intentarlo !!'

# Entrada al codigo
NumeroOculto = random.randint(1,10)
vidas = None

dificultad = int (input (PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad !=2 and dificultad !=3):
    print ('ingresa una opcion valida')
    dificultad = int (input (PREGUNTA_DIFICULTAD))

if (dificultad ==1):
    print ('Modo facil activado')
    vidas = 5
elif (dificultad == 2):
    print ('Modo moderado activado')
    vidas = 3
else:
    print ('Modo dificil activado, sssssss mucho cuidado')
    vidas = 1

NumeroIngresado = int (input(PREGUNTAR_NUMERO))
while (NumeroIngresado != NumeroOculto and vidas>1):
    vidas -=1
    NumeroIngresado = int (input (PREGUNTA_FALLIDA))
    print (f'te quedan {vidas} vidas')
    NumeroIngresado = int (input(PREGUNTA_FALLIDA))

if (vidas >=0 and NumeroIngresado == NumeroOculto):
    print (MENSAJE_GANASTE)
else:
    print (MENSAJE_PERDISTE, 'El numero era', NumeroOculto)