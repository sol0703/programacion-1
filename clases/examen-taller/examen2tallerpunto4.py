listaPesos = [20000,30000,4000,2500,1000,7600]
preguntaBorrarCoordenada = 'Ingrese la posicion que desea borrar:'
print (listaPesos)
posicion = int (input(preguntaBorrarCoordenada)) - 1
listaPesos.pop(posicion)
print (listaPesos)
