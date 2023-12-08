
import random


########################################################
def encontrar_elementos_repetidos(lista_de_listas):
    elementos_repetidos = {}
    
    for i, elemento in enumerate(lista_de_listas):
        elemento_tupla = tuple(elemento)
        if elemento_tupla in elementos_repetidos:
            elementos_repetidos[elemento_tupla].append(i)
        else:
            elementos_repetidos[elemento_tupla] = [i]
    
    elementos_repetidos = {k: v for k, v in elementos_repetidos.items() if len(v) > 1}
    
    return elementos_repetidos

class Animal: 

    def __init__(self, nombre):
        self.nombre = nombre
        self.posicion = [random.randrange(0,64,1), random.randrange(0,64,1)]
        probabilidad = random.random()
        if self.nombre == "PresaNacida":  #Dependiendo del valor de nombre en la clase, se asigna a la variable tipo dentro de la clase su correspondiente tipo
            
            #Esta solucion ni me parece dle todo correcta
            self.tipo = 'Presa'
            
        self.tipo = 'Presa' if random.random() > 0.3 else 'Depredador'


    def get_tipo(self): #Este metodo solo retorna el tipo de animal
        return self.tipo
    
    def get_posicion(self): #Este metodo solo retorna la posicion
        return self.posicion
    
    def CambiarPosicion(self): #En este metodo, se plantean las 9 posibilidades de movimiento para un objeto con 9 casillas circundantes tomando en cuenta las limitantes del espacio
        
     for i in range(0,9):
        Eleccion = random.randrange(0,9,1)
        if Eleccion == 8:  #En esta posibilidad se mantiene la misma posicion 
             return self.posicion
        elif Eleccion == 0:
             if (self.posicion[0]-2) >= 0 and (self.posicion[1]-2) >= 0:
                  self.posicion = [self.posicion[0]-2, self.posicion[1]-2]
                  return self.posicion 
             continue
        elif Eleccion == 1:
             if (self.posicion[1]-2) >= 0:
                  self.posicion = [self.posicion[0], self.posicion[1]-2]     
                  return self.posicion
             continue
        elif Eleccion == 2: 
             if (self.posicion[1]-2) >= 0 and (self.posicion[0] + 2) <= 64:
                  self.posicion = [self.posicion[0] + 2, self.posicion[1]-2]
                  return self.posicion
             continue
        elif Eleccion == 3:
             if (self.posicion[0] + 2) < 64:
                  self.posicion = [self.posicion[0]+2, self.posicion[1]]
                  return self.posicion  
             continue   
        elif Eleccion == 4:
             if (self.posicion[0] + 2) < 64 and (self.posicion[1] + 2) < 64:
                  self.posicion = [self.posicion[0]+2, self.posicion[1]+2]
                  return self.posicion   
             continue  
        elif Eleccion == 6:
             if (self.posicion[0] - 2) > 0 and (self.posicion[1] + 2) <64:
                  self.posicion = [self.posicion[0]-2, self.posicion[1]+2]
                  return self.posicion     
             continue
        elif Eleccion == 5:
             if (self.posicion[1] + 2) < 64:
                  self.posicion = [self.posicion[0], self.posicion[1]+2]
                  return self.posicion    
             continue 
        elif Eleccion == 7:
             if (self.posicion[0] - 2) > 0:
                  self.posicion = [self.posicion[0]-2, self.posicion[1]]
                  return self.posicion    
             continue 
        
    def Muerte(self, lista_de_animales_existentes):  
            lista_de_animales_existentes.remove(self)
             #Esta posiblemente no es la mejor solucion   #################Revisarrrrrrrrr
            
            #Fue la mejor solucion, list comprenjeisions no fueron mejores
     
    def MuerteDepredador(self, Animal2, lista_de_animales_existentes, posicionI, posicionJ):
            probabilidad = random.random() # Cada animal tiene un 40% de probabilidades de morir
            if probabilidad < 0.5:
                    self.Muerte(lista_de_animales_existentes)
            elif probabilidad >= 0.5:
                    Animal2.Muerte(lista_de_animales_existentes)
            
        
    def MuertePresa(self, lista_de_animales_existentes): #por agregar- > Contenedor: El contenedor asociado a la presa)
        probabilidad = random.random()
        if probabilidad > 0.2: #La presa tiene el 60% de probabilidades de morir
            self.Muerte(lista_de_animales_existentes)

    def Apareamiento(self, lista_de_animales, Nacidos):
        probabilidad = random.random()
        if probabilidad > 0.8:
            animalNacido = Animal("PresaNacida")
            lista_de_animales.append(animalNacido)
            Nacidos.append(animalNacido)

    def Coincidencia(self, lista_de_animales_existentes, lista_posiciones, Nacidos): #Nota, esto solo es valido para dos elementos prsentes simultaneamente en la misma posicion
     posicionI = lista_posiciones[0]
     posicionJ = lista_posiciones[1]

     Animal1 = lista_de_animales_existentes[posicionI] #Guardamos los animales asociados a las posiciones de la lista_posiciones
     Animal2 = lista_de_animales_existentes[posicionJ]
     

     tipo1 = Animal1.get_tipo() #Consultamos su tipo
     tipo2 = Animal2.get_tipo()
     print(tipo1, tipo2)
    
     
            #logica
     if tipo1 == tipo2:
                
                if tipo1 == 'Depredador':
                  print("Se ejecuto el caso donde son iguales y depredadores:", tipo1, tipo2)
                  #si los dos elementos son iguales, y si uno es depredador
                  Animal1.MuerteDepredador(Animal2, lista_de_animales_existentes, posicionI, posicionJ)
                  return None
                else: 
                  print("Se ejecuto el caso donde son iguales y presas: ", tipo1, tipo2)
                  #llamamos al metodo apareamiento
                  Animal1.Apareamiento(lista_de_animales_existentes, Nacidos)
                  return None
            
     elif tipo1 != tipo2:
                #Si son diferentes, alguno de los dos debe ser depredador
                if tipo1 == 'Depredador':
                
                    Animal2.Muerte(lista_de_animales_existentes)
                    return None
                else:
                 
                    Animal1.Muerte(lista_de_animales_existentes)
                    return None
            

            #Hay un problemilla en la logica de coincidencia 
#Nota futura: Agregar un item con la cantidad de animales vivos
# Agregar una entrada para la creacion de animales
##################################################################################
print("Se inicio el codigo....")
