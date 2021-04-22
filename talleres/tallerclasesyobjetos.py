# Punto 1
print ('Punto 1')
class Torta ():
    def __init__ (self, saborEntrada, alturaEntrada, formaEntrada):
        self.sabor = saborEntrada
        self.altura = alturaEntrada
        self.forma = formaEntrada 
    def mostrarAtributos (self):
        print (f''' Los atributos de la torta son:
        1- Su sabor es de {self.sabor}
        2- Posee una altura de {self.altura} cm
        3- Tiene una forma {self.forma}
        ''')

torta1 = Torta ('Vainilla y dulce de leche', 15, 'circular')
torta1.mostrarAtributos ()

# Punto 2
print ('Punto 2')
class Estudiante ():
    def __init__ (self, edadEntrada, nombreEntrada, idEntrada, carreraEntrada, semestreEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada
    def estudiar (self, materia, horasEstudiar, edad , identificacion):
        print (f'Buenas mi nombre es {self.nombre}, tengo {edad} años, me identifico con el numero de cc. {identificacion} y procedo a estudiar {materia} por {horasEstudiar} horas por semana')

estudiante1 = Estudiante (20, 'Sara', 1000538076, 'Ingenieria Biomedica', 3)
estudiante1.estudiar ('fisica', 4, 20, 1000538076)

# Punto 3
print ('Punto 3')
class Nutricionista ():
    def __init__ (self, edadEntrada, nombreEntrada, universidadEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.universidad = universidadEntrada
    def imcPaciente (self, peso, altura ):
        return round (peso/(altura**2))

nutricionista1 = Nutricionista (24, 'Sandra', 'UdeA')
print (nutricionista1.imcPaciente (70, 1.63))

#-----Punto 4-----#
print ('Punto 4')
class Canguro ():
    def __init__ (self, edadEntrada, idEntrada, nombreEntrada):
        self.edad = edadEntrada
        self.id = idEntrada
        self.nombre = nombreEntrada
    def saltar (self, saltos):
        for i in range (saltos):
            print (f'El canguro {self.nombre} ha dado {i+1} salto')

canguro1 = Canguro (9, 14701, 'Milo')
canguro1.saltar (5)

#-----Punto 5-----#
print ('Punto 5')
class Piano ():
    def __init__ (self, marcaEntrada, colorEntrada):
        self.marca = marcaEntrada
        self.color = colorEntrada
    def interpretar (self, cancion):
        print (f'Interpretacion de la cancion {cancion} en el piano')

piano1 = Piano ('Teclado Electronico Yamaha Ez-300 De 61 Teclas Con Adaptador', 'blanco')
piano1.interpretar ('Let it go')