# Mensaje
MENSAJE_SALUDAR  =  'Bienvenido !! Te apoyare ahorrando '
MESANJE_AHORRO  =  'LLEVAS AHORRADO ...'
PREGUNTAR_VALOR_CPU  =  '¿Cuanto vale el pc que quieres? : '
PREGUNTA_CUANTO_TIENE  =  '¿Cuánto llevas ahorrado? : '

# Entrada al codigo
print (MENSAJE_SALUDAR)
valor = float (input(PREGUNTAR_VALOR_CPU))
ahorrado = float (input(PREGUNTA_CUANTO_TIENE))

while (valor < ahorrado):
    print (MESANJE_AHORRO, ahorrado, 'te falta ...', valor - ahorrado)
    ahorrado = ahorrado + 1000

print (valor == ahorrado)
