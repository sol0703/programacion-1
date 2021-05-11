# punto 1
print ('Punto 1 --- Grafico de barras')

import matplotlib.pyplot as plt

snacks = []
precios = []
for i in range (5):
    Snacks = input ("Agregue tu snack favorito: ")
    Precios = input ("Agregue el precio de tu snack favorito: ")
    precio.append (Precios)
    snacks.append (Snacks)
    print (f"Realice este proceso {4-i} veces")

snacks = (snacks)
precios = (precios)
plt.bar (snacks, precios, width = 0.6, color = 'c')
##
plt.title ('Snacks favoritos')
plt.xlabel ('Snacks')
plt.ylabel ('Precios')
plt.savefig ('Grafico anacks.png')
plt.show ()

# punto 2
print ('Punto 2 --- Grafico de torta')

Ciudades = []
Poblacion = []

for i in range (5):
    ciudad = input ("Agregue una de tus ciudades favoritas: ")
    poblacion = input ("Agregue el numero de la poblacio de la ciudad escogida: ")
    Ciudades.append (ciudad)
    Poblacion.append (poblacion)
    print (f"Realice este proceso {4-i} veces")

print (Ciudades)
print (Poblacion)
maximo = Poblacion.index (max (Poblacion))
pieExplode = [0,0,0,0,0]

pieExplode [maximo] = 0.1

plt.pie(Poblacion, labels = Ciudades,
        explode = pieExplode)
plt.title ("Ciudades favoritas en el mundo")
plt.savefig ('Grafico ciudades favoritas.png')
plt.show ()

# punto 3
print ('Punto 3 --- Grafico curvas')

print ('ecg = Un electrocardiograma es un examen que registra la actividad eléctrica del corazón.')
print ('ppg = Es una técnica de pletismografía en la cual se utiliza un haz de luz para determinar el volumen de un órgano')

import pandas as pd

ppgData = pd.read_csv ('ppg.csv', encoding = 'UT8', header = 0, delimiter = ';').to_dict ()
muestras = list (ppgData ['muestra'].values ())
valores = list (ppgData ['valor'].values ())
plt.plot (muestras, valores)
plt.xlabel ('Tiempo (ms)')
plt.ylabel ('Voltaje (mV)')
plt.title ('Fotopletismografia')
plt.savefig ('Grafico ppg.png')
##
ecgData = pd.read_csv ('ecg.csv', encoding = 'UT8', header = 0, delimiter = ';').to_dict ()
muestra1 = list (ecgData ['muestra'].values ())
voltaje = list (ecgData ['valor'].values ())
plt.plot (muestra1, voltaje)
plt.xlabel ('Tiempo (ms)')
plt.ylabel ('Voltaje (mV)')
plt.title ('Electrocardiograma')
plt.savefig ('Grafico ecg.png')
plt.show ()