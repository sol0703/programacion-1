# Trabajamos Miguel Zuleta
# punto 1
# a
print('Punto a')
class ElementosDigitales ():
    def __init__ (self, nombre, creador, fechadepublicacion):
        self.nombre = nombre
        self.creador = creador
        self.fechadepublicacion = fechadepublicacion
    def mostrarAtributos (self,):
        print (f''' Los atributos de la pelicula son:
        1- Su creador es {self.nombre}
        2- El nombre de la compañia es {self.creador} 
        3- Su fecha de publicacion fue {self.fechadepublicacion}
        ''')

ElementosDigitales1 = ElementosDigitales('Julian', 'Marvel', '1 de Diciembre del 2119')
ElementosDigitales1.mostrarAtributos ()

# b
print('Punto b')
class Usuario ():
    def __init__ (self, nombre, edad, sexo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad
    def mostrarAtributos (self, cancion):
        print (f' Hola soy {self.nombre}, tengo {self.edad} años, soy {self.sexo} y soy de {self.nacionalidad} y estoy escuchando {cancion}' )


Usuario1 = Usuario('Sara', 20, 'Mujer', 'Colombiana')
Usuario1.mostrarAtributos ('Adios')

# c
print('Punto c')
class Pagina ():
    def __init__ (self, tipodecontenido, formato, fechadepublicacion):
        self.tipodecontenido = tipodecontenido
        self.formato = formato
        self.fechadepublicacion = fechadepublicacion
    def mostrarAtributos (self):
        print (f''' Los atributos de la pagina son:
        1- Su contenido es {self.tipodecontenido}
        2- El formato {self.formato} 
        3- Su fecha de publicacion es {self.fechadepublicacion}
        ''')

Pagina1 = Pagina('Musica', 'web', '2 de enero de 2001')
Pagina1.mostrarAtributos ()

# punto 2
# a
print ('punto 2')
class Cancion (ElementosDigitales):
    def _init_(self, nombre, creador, fechadepublicacion, Generomusical, Duracion):
        super().__init__(nombre, creador, fechadepublicacion)
        self.Generomusical = Generomusical
        self.Duracion = Duracion
    def mensaje (self, Nombre, Fechadecreacion):
        print (f'Cuando se crea una nueva cancion: {Nombre}, tambien se ve su fecha de creacion: {Fechadecreacion}')
    def veces (self, cancionnombre):
        for lista in range(cancionnombre):
            print (f'La cancion {cancionnombre} se a reproducido {lista+1} veces')

Cancion1 = Cancion('Estrellita', 'Maluma', '7 de marzo de 1999')
Cancion1.mensaje('Estrellita', '5 de abril de 1997')
Cancion1.veces (5)

# b
class Artista (Usuario):
    def _init_(self, nombre, edad, sexo, nacionalidad, Generomusical, numerocanciones, numerodealbum, ciudad):
        super().__init__(nombre, nombre, edad, sexo, nacionalidad)
        self.Generomusical = Generomusical
        self.numerocanciones = numerocanciones
        self.ciudad = ciudad
        self.numerodealbum = mumerodealbum
    def comunicado (self, numerodealbum, Generomusical, numerocanciones, ciudad):
        print (f'''Soy el artista {self.nombre} tengo {self.edad} años, soy genero {self.sexo}, soy de {self.nacionalidad}
        voy a lanzar mi album numero {numerodealbum} del gennero musical {Generomusical},
        donde cantare {numerocanciones} canciones.
        Preparete {ciudad} ALLA VOY !!!
        ''')

Artista1 = Artista('Paco', 70, 'Hombre', 'Peru')
Artista1.comunicado(1, 'tango', 7, 'DF')

# c
class Favoritos (Pagina):
    def __init__ (self, tipodecontenido, formato, fechadepublicacion, favoritoscomunidad, fechaactualizacion):
        Pagina.__init__(self, tipodecontenido, formato, fechadepublicacion)
        self.favoritoscomunidad = favoritoscomunidad
        self.fechaactualizacion = fechaactualizacion
    def agregarcancion (self, cancion, actualizacion):
        self.favoritoscomunidad.append(cancion)
        self.fechaactualizacion = actualizacion
    def mostrarlista (self, cancioneliminada):
        print (self.favoritoscomunidad)
        self.favoritoscomunidad.pop(cancioneliminada)

lista = ["let it go", "Adios", "Yellow"]
Yellow = Favoritos('cancion', 'web', 2002, 'lista', '4 de mayo de 2015')
Yellow.mostrarlista(2)
Yellow.agregarcancion('cancion nueva', 2015)
print (Yellow.favoritoscomunidad)

