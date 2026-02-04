from humanidad import *

humano1=Humano("Diana",19,"Femenino")
print(humano1.nombre)
print(humano1.edad)
print(humano1.genero)
humano1.caract()
humano1.saludo()

prog1=Programador("Jose", 20, "Masculino")
print(prog1.nombre)
print(prog1.edad)
print(prog1.genero)
prog1.caract()
prog1.saludo()
prog1.saludo2()

ing1=Ingeniero("David", 19, "Masculino","Ing gato")
print(ing1.nombre)
print(ing1.edad)
print(ing1.genero)
print(ing1.tipo)
ing1.saludo()
