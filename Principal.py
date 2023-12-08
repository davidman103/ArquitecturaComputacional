from porteo import Animal
from _thread import start_new_thread
from machine import Pin, SoftI2C
import utime

i2c = SoftI2C(scl=Pin(22),sda=Pin(21))

from ola import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c)  
###################################################################################3


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

ListaAnimales = [] #Variable global

for i in range(0, 20, 1): #Recordar
    animal = Animal("A_{}".format(i))
    ListaAnimales.append(animal) #Creamos una lista Vacia llamada Animales, en donde guardaremos la informacion de los animales creados
print(ListaAnimales)

def main():
    ObjetoEstatico = Animal(1) #Es un objeto estatico, valgase la redundancia 

    #Ya se crearon los animales(objetos), ahora se puede empezar con la implementacion de la lógica 

    while len(ListaAnimales) > 2: #Mientras haya más de un individio, siga ejecutandose
       Nacidos = []
       ListaPosiciones = []
       
       utime.sleep_ms(100)
       for i in range(len(ListaAnimales)):
          NuevaPosicion = ((ListaAnimales[i]).CambiarPosicion())
          ListaPosiciones.append(NuevaPosicion)

########################################################################################33
       
       resultados = encontrar_elementos_repetidos(ListaPosiciones)  #En esta parte del codigo llamamos a la funcion "encontrar_elementos_repetidos", que indica los elementos que poseen una misma posicion

       if resultados: #Se ejecuta la busqueda de coindicencias 
            for elemento, posiciones in resultados.items():
               print(f"Elemento: {elemento} - Posiciones: {posiciones}")
               #Posicion_VariableTemporal = posiciones #Guardamos la posicion de los elementos coincidentes en una variable
               ObjetoEstatico.Coincidencia(ListaAnimales, posiciones, Nacidos) #llamamos al metodo que ejecuta toda la logica 
               
               if len(Nacidos) > 0: #Para el caso que se haya ejecutado un apareamiento exitoso, crearemos un contenedor con este elemento 
#Nota para Deivy del futuro: Agregar el apareamiento para depredadores xd, olvide que también deberian hacerlo lol
                  # SE DEBE MOSTRAR EL NUEVO NACIDO
                  Nacidos = []
               continue
       else:
            print("No se encontraron elementos repetidos en la lista.")
        
       
HistoricoPresa = 0
HistoricoDepre = 0

def OLED():
    #Posterior a la inicializacion d ela conexion por i2c de la pantalla se prodece a ejecutar el metodo grafico 
 while len(ListaAnimales) > 2:
     
    for i in ListaAnimales:
        oled.pixel((i.get_posicion())[0], (i.get_posicion())[1], 1)
        
    Presas = []
    Depredadores = []
    for i in range(len(ListaAnimales)):
           if ListaAnimales[i].get_tipo() == 'Presa':
               Presas.append(1)
           else:
               Depredadores.append(1)  

    HistoricoPresa = len(Presas)
    HistoricoDepre = len(Depredadores)

    oled.text("P:{}".format(HistoricoPresa), 65, 25)
    oled.text("D:{}".format(HistoricoDepre), 65, 35)
    oled.show()
    utime.sleep_ms(100)
    oled.fill(0)
    oled.show()

    #Debido a que toda la logica del codigo se encuentra en otra función y se ejecuta en otro hilo de nuestro procesador, trabajaremos con una lista global de elementos



   
if __name__ == "__main__":
   start_new_thread(main,()) #Ejecutamos la tarea main en un hilo aparte
   start_new_thread(OLED,())
  
  
  
  

   input("Ingrese una letra para terminar :" )
   