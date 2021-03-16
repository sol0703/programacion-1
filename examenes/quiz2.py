# preguntas
preguntaNumero = '''Buenos dias, por favor ingrese alguna de estas opciones
    1. Hacer conversion de grados celsius a kelvin 
    2. Mostrar como esta el estado de la temperatura del paciente
    3. Mostrar la temperatuta maxima, minima y cada cuanto tomaba un dato 
    4. Salir del programa
'''
preguntaConversionTemperatura = ''' Ingrese la opcion de su interes
    C- Mostrar la temperatura en grados celsius
    F- Mostrar la temperatura en grados fahrenheit
    K- Mostrar la temperatura en kelvin
'''
# mensajes

mensajeCelsius = 'La lista original esta en grados celsius, no es necesario mostrar la conversion'
mensajeFahrenheit = 'Mostrar lista en grados fahrenheit'
mensajeKelvin = 'Mostrar la lista en kelvin'
mensajeTemperaturaMaxima = 'La temperatura maxima es -->'
mensajeTemperaturaMinima = 'La temperatura minima es -->'
mensajeCadaCuanto = 'Los datos se tomaron cada {} horas'
mensajeDespedida = 'Feliz dia'
# mensajes error
mensajeErrorNumero = 'Solo se encuentran las opciones 1, 2, 3 y 4 '
mensajeErrorConversion = 'Solo se encuentran las opciones C, F y K'

temperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

# Conversion punto 1
listaFahrenheit = []
for elemento in temperaturaCorporal:
    conversor = round ((elemento-32)/0.00023,2)
    listaFahrenheit.append(conversor)
listaKelvin = []
for elemento in temperaturaCorporal:
    conversor = round (elemento+273.15,2)
    listaKelvin.append(conversor)

# estado de la temperatura punto 2
ListaEstadoTemperatura = []
for elemento in temperaturaCorporal:
    estadoTemperatura = ''
    if (elemento < 36):
        estadoTemperatura = 'hipotermia'
    elif (elemento >= 37.6):
        estadoTemperatura = 'fiebre'
    elif (elemento >= 36 and elemento < 37.6):
        estadoTemperatura = 'temperatura normal'
    ListaEstadoTemperatura.append(estadoTemperatura)

opcionEscogida = int (input(preguntaNumero))
while (opcionEscogida !=4):
    #----- opcion 1 -----
    if (opcionEscogida == 1):
        opcionTemperatura = input (preguntaConversionTemperatura)
        if (opcionTemperatura == 'C'):
            print (mensajeCelsius)
            print (temperaturaCorporal)
        elif (opcionTemperatura == 'F'):
            print ( mensajeFahrenheit)
            print (listaFahrenheit)
        elif (opcionTemperatura == 'K'):
            print (mensajeKelvin)
            print (listaKelvin)
        else:
            print (mensajeErrorConversion)
    #----- opcion 2 -----
    elif (opcionEscogida == 2):
        print (ListaEstadoTemperatura)
    #----- opcion 3 -----
    elif (opcionEscogida == 3):
        print (mensajeTemperaturaMaxima, max(temperaturaCorporal))
        print (mensajeTemperaturaMinima, min(temperaturaCorporal))
        print (mensajeCadaCuanto, 24/len(temperaturaCorporal))
    #----- opcion 4 -----
    else:
        print (mensajeErrorNumero)
    
    opcionEscogida = int (input(preguntaNumero))

print (mensajeDespedida)