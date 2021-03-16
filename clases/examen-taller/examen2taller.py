# ----- preguntas -----
preguntaNumero = ''' Ingrese alguna de estas opciones
    1. Hacer conversion de pesos a dolares o Euros
    2. Agregar un valor a la lista de pesos
    3. Mostrar valor mas alto, mas bajo y promedio
    4. Eliminar elemento de la lista
    5. Salir
'''
preguntaMoneda = '''
    C- Mostrar original en pesos colombiano
    D- Mostrar en dolares
    E- Mostrar en euro
'''
preguntarNumero = 'Ingrese un valor COP:'
preguntaBorrarCoordenada = 'Ingrese la posicion que desea borrar:'
#----- mensajes -----
mensajePesos = 'Mostrando lista original'
mensajeDolares = 'Mostrando lista en dolares'
mensajeEuros = 'Mostrar lista en euros'
mensajeMayor = 'El mayor numero ingresado es -->'
mensajeMenor = 'El menor numero ingreado es -->'
mensajePromedio = 'El promedio es -->'
mensajeDespedida = 'Que tengas un feliz dia'
#----- error -----
mensajeErrorEntrada = 'valor ingresado no valido'

listaPesos = [20000,30000,4000,2500,1000,7600]

# Conversion punto 1
listaEuros = []
for elemento in listaPesos:
    conversor = round (elemento*0.00023,2)
    listaEuros.append(conversor)
listaDolares = []
for elemento in listaPesos:
    conversor = round (elemento*0.00028,2)
    listaDolares.append(conversor)

opcionEscogida = int (input(preguntaNumero))
while (opcionEscogida !=5):
    #----- opcion 1 -----
    if (opcionEscogida == 1):
        opcionMoneda = input (preguntaMoneda)
        if (opcionMoneda == 'C'):
            print (mensajePesos)
            print (listaPesos)
        elif (opcionMoneda == 'D'):
            print ( mensajeDolares)
            print (listaDolares)
        elif (opcionMoneda == 'E'):
            print (mensajeEuros)
            print (listaEuros)
        else:
            print (mensajeErrorEntrada)
    #----- opcion 2 -----
    elif (opcionEscogida == 2):
        valorIngresado = float (input(preguntarNumero))
        listaPesos.append(valorIngresado)
        print (listaPesos)
    #----- opcion 3 -----
    elif (opcionEscogida == 3):
        print (mensajeMayor, max(listaPesos))
        print (mensajeMenor, min(listaPesos))
        print (mensajePromedio, sum(listaPesos)/len(listaPesos))
    #----- opcion 4 -----
    elif (opcionEscogida == 4):
        print (listaPesos)
        posicion = int (input(preguntaBorrarCoordenada)) - 1
        listaPesos.pop(posicion)
        print (listaPesos)
    #----- opcion no valida -----
    else:
        print (mensajeErrorEntrada)
    
    opcionEscogida = int (input(preguntaNumero))

print (mensajeDespedida)