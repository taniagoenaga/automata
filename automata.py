import time
from tkinter import *
from objeto import *
from clases import *
class Automata:

    def __init__(self, palabra, ventana, lienzo):
        if(len(palabra) % 2 == 0):
            self.estado = "rechazado"
            print("rechazado")
        else:
            self.palabra = palabra
            self.ventana = ventana
            self.estado_grafo = "inicial"
            self.lienzo = lienzo
            self.estado = "impar"
            self.pila = Pila(palabra, lienzo)
            print(self.palabra)

    def validar(self,esfera, flecha, flecha3, flecha4, borde, esfera2, esfera3, flecha2, apuntador):
        contador_palabra = 0
        if(self.estado != "rechazado"):
            x1=600
            y1=200
            x2=x1+50
            y2=y1+50
            for e in range(len(self.palabra)):
                if(self.estado != "rechazado"):
                    contador = 0
                    if(e == (len(self.palabra)/2)-0.5):
                        print(e)
                        self.estado_grafo = "mitad"
                        contador = 1
                        print(self.estado_grafo)
                        self.lienzo.create_image(150, 100, anchor=NE, image=esfera)
                        time.sleep(0.7)
                        self.lienzo.create_image(260, 140, anchor=NE, image=flecha4)
                        self.ventana.update()
                        time.sleep(0.7)
                        self.lienzo.create_image(260, 140, anchor=NE, image=flecha3)
                        self.ventana.update()
                    if(self.estado_grafo == "inicial"):
                        #self.lienzo.move(pointer, 50, 0)
                        self.pila.mostrar(x1, y1, x2, y2, e)
                        #vertical disminuye en x y horizontal disminuye y
                        y1-=50
                        y2-=50
                        time.sleep(0.7)
                        self.lienzo.create_image(150, 100, anchor=NE, image=esfera3)
                        self.lienzo.create_image(180, 70, anchor=NE, image=flecha)
                        self.ventana.update()
                        time.sleep(0.7)
                        self.lienzo.create_image(150, 100, anchor=NE, image=esfera)
                        self.lienzo.create_image(180, 70, anchor=NE, image=flecha2)
                        self.ventana.update()
                        time.sleep(0.7)
                        self.lienzo.create_image(180, 70, anchor=NE, image=flecha)
                        self.lienzo.create_image(150, 100, anchor=NE, image=esfera3)
                        self.ventana.update()
                    elif(self.estado_grafo == "mitad"):
                        #self.lienzo.move(pointer, 50, 0)
                        time.sleep(0.7)
                        self.lienzo.create_image(325, 100, anchor=NE, image=esfera3)
                        self.lienzo.create_image(355, 70, anchor=NE, image=flecha)
                        self.ventana.update()
                        time.sleep(0.7)
                        self.lienzo.create_image(325, 100, anchor=NE, image=esfera)
                        self.lienzo.create_image(355, 70, anchor=NE, image=flecha2)
                        self.ventana.update()
                        time.sleep(0.7)
                        self.lienzo.create_image(355, 70, anchor=NE, image=flecha)
                        self.lienzo.create_image(325, 100, anchor=NE, image=esfera3)
                        self.ventana.update()
                        if(contador == 1):
                            contador = 0
                        else:
                            if(self.palabra[e] == self.pila.pila[len(self.pila.pila)-1].letra):
                                contador_palabra+=1
                                self.lienzo.delete(self.pila.pila[len(self.pila.pila)-1].id)
                                self.lienzo.delete(self.pila.pila[len(self.pila.pila)-1].rectangulo)
                                self.pila.pila.pop(len(self.pila.pila)-1)
                            else:
                                self.estado == "rechazado"
                                self.lienzo.create_text(150,300,fill="green",font="Times 20 italic bold",text="palabra rechazada")
                                print("rechazado")
                    else:
                        print("esta palabra no es valida")
        if(contador_palabra == (len(self.palabra)/2)-0.5):
            time.sleep(0.7)
            self.lienzo.create_image(435, 140, anchor=NE, image=flecha4)
            self.lienzo.create_image(325, 100, anchor=NE, image=esfera)
            self.lienzo.update()
            time.sleep(0.7)
            self.lienzo.create_image(500, 100, anchor=NE, image=esfera3)
            self.lienzo.create_image(435, 140, anchor=NE, image=flecha3)
            self.lienzo.update()
            self.lienzo.create_text(150,300,fill="green",font="Times 20 italic bold",text="palabra aceptada")
            print("aceptado")
