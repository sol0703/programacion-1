# Punto 1
print ('Punto 1')
class Persona ():
    def __init__ (self, nombreEntrada, edadEntrada, idEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEntrada
    def hablar (self, mensaje):
        print (f'Hola mi nombre es {self.nombre} y tengo un mensaje que decir...', mensaje)
    def caminar (self, pasos):
        for i in range (pasos):
            print (f'Hola mi nombre es {self.nombre} y he caminado {i+1} pasos')

persona1 = Persona ('Sara', 20, 1000538076)
persona1.hablar ('Ojala te encuentres bien')
persona1.caminar (5)

# Punto 2
print ('Punto 2')
class Doctor (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, especialidadEntrada):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.especialidad = especialidadEntrada
    def mostrarAtributos (self):
        print (f'Buenas tardes, soy el doctor y mi nombre es {self.nombre}, tengo {self.edad} años, me especialice en {self.especialidad} y mi identificacion es {self.id}')
    def enfermedadTratada (self, enfermedad):
        print (f'Pol tal razon yo {self.nombre} procedo a tratar la {enfermedad}')

doctor1 = Doctor ('Juan Manuel', 32, 43263548, 'Oftamologia')
doctor1.mostrarAtributos ()
doctor1.enfermedadTratada ('Miopia')

# Punto 3
print ('Punto 3')
class Nutricionista (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, universidadEgresado):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.universidad = universidadEgresado
    def mostrarAtributos (self):
        print (f'Buenas tardes soy la nutricionista y mi nombre es {self.nombre}, tengo {self.edad} años, mi identificacion es {self.id} y soy egresada de la universidad {self.universidad}')
    def imcPaciente (self, peso, altura):
        return round (peso/(altura**2))

nutricionista1 = Nutricionista ('Sandra', 24, 43000341, 'UdeA')
nutricionista1.mostrarAtributos ()
print (nutricionista1.imcPaciente (70, 1.63))

# Punto 4
print ('Punto 4')
class Abogado (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, especialidadEntrada, universidadEgresado):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.especialidad = especialidadEntrada
        self.universidad = universidadEgresado
    def mostrarAtributos (self):
        print (f'Buenas tardes soy el abogado {self.nombre}, tengo {self.edad} años, me identifico con el numero {self.id}, me especialice en {self.especialidad} y soy egresado de la universidad {self.universidad}')
    def casoRepresentado (self, nombre, caso):
        print (f'Y yo como el abogado {self.nombre} procedo a representar al cliente {nombre} en el caso de {caso}')

abogado1 = Abogado ('Juan Carlos', 45, 70433543, 'derecho laboral y seguridad social', 'CES')
abogado1.mostrarAtributos ()
abogado1.casoRepresentado ('Julian', 'invasion de pago de salud y pension a sus empreados')
