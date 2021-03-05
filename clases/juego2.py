
import random
# Entradas
MENSAJE_SALUDO = '''
    Bienvenido
        a este programa,
    !!!juguemos!!'''
MENSAJE_SEGUDO_NIVEL = 'Felicidades pasaste el primer nivel ahora ve por el ultimo!!'
MENSAJE_CALIENTE = 'Estas caliente'
MENSAJE_FRIO = 'Estas frio'
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
NueroOcultoDos = random.randint(1,10)
vidas = None

dificultad = int (input (PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad !=2 and dificultad !=3):
    print ('ingresa una opcion valida')
    dificultad = int (input (PREGUNTA_DIFICULTAD))

if (dificultad ==1):
    print ('Modo facil activado')
    vidas = 10
elif (dificultad == 2):
    print ('Modo moderado activado')
    vidas = 5
else:
    print ('Modo dificil activado, sssssss mucho cuidado')
    vidas = 2

NumeroIngresado = int (input(PREGUNTAR_NUMERO))
while (NumeroIngresado != NumeroOculto and vidas>1):
    if (NumeroIngresado > NumeroOculto):
        print (MENSAJE_CALIENTE)
    else:
        print (MENSAJE_FRIO)
    vidas -=1
    print (f'te quedan {vidas} vidas')
    NumeroIngresado = int (input(PREGUNTA_FALLIDA))
if (vidas >=0 and NumeroIngresado == NumeroOculto):
    print (MENSAJE_SEGUDO_NIVEL)
    NumeroIngresado = int (input(PREGUNTAR_NUMERO))
    while (NumeroIngresado != NueroOcultoDos and vidas>1):
        if (NumeroIngresado > NueroOcultoDos):
            print (MENSAJE_CALIENTE)
        else:
            print (MENSAJE_FRIO)
        vidas -=1
        print (f'te quedan {vidas} vidas')
        NumeroIngresado = int (input (PREGUNTA_FALLIDA))


if (vidas >=0 and NumeroIngresado == NueroOcultoDos ):
    print (MENSAJE_GANASTE)

else:
    print (MENSAJE_PERDISTE,
        'El numero era el',
        NumeroOculto,
        'El numero dos era el',
        NueroOcultoDos)