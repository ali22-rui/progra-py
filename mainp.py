from persona import *

a1= Persona("Gael" , "abcde@gmail.com")
a2= Persona("Toño" , "1234@gmail.com")
a3= Persona("Sebas" , "chono@gmail.com")
a4= Persona("Lia" , "mep@gmail.com")

a1.register()
a2.register()

Persona.personas_registradas()
