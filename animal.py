class Animal():
    def __init__(self,nombre,color,patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas

    def sonido(self):
        print(f"sonido")
    

class Conejo(Animal):
    def sonido(self):
        print(f"Mi conejo se llama {self.nombre} es de color {self.color} y tiene {self.patas} patas ")
        print("sniff sniff")

        
class Ornitorrinco(Animal):
    def __init__(self,nombre,color,patas,pico):
        super().__init__(nombre,color,patas)
        self.pico=pico

    def sonido(self):
        print(f"Mi Ornitorinco se llama {self.nombre} es de color {self.color} y tiene {self.patas} patas y el tamaño de su pico es {self.pico} cm")
        print("Grrrrr")

class Dinosaurio(Animal):
    tipo="Dinosaurio"
    
    
    def sonido(self):
         print(f"Mi Dino se llama {self.nombre} es de color {self.color} y tiene {self.patas} patas, y su especie es {Dinosaurio.tipo}")
         print("ROAAR")


        
        
