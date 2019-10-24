from automata import *
from Audio_con_Archivo import *
from gif import *
from tkinter import *
import speech_recognition as sr 


def validar():
    automata = Automata(entrada.get(), ventana, lienzo)
    if(automata.estado != "rechazado"):
      automata.validar(esfera, flecha, flecha3, flecha4, borde, esfera2, esfera3, flecha2, apuntador)

def borrar():
    lienzo.delete("all")
    imagen_esfera = lienzo.create_image(150, 100, anchor=NE, image=esfera)
    flecha_esfera = lienzo.create_image(180, 70, anchor=NE, image=flecha)
    flecha_esfera12 = lienzo.create_image(84, 140, anchor=NE, image=flecha3)
    flecha_esfera122 = lienzo.create_image(260, 140, anchor=NE, image=flecha3)
    borde_esfera = lienzo.create_image(513, 87, anchor=NE, image=borde)
    imagen_esfera2 = lienzo.create_image(325, 100, anchor=NE, image=esfera)
    flecha_esfera2 = lienzo.create_image(355, 70, anchor=NE, image=flecha)
    flecha_esfera22 = lienzo.create_image(435, 140, anchor=NE, image=flecha3)
    imagen_esfera3 = lienzo.create_image(500, 100, anchor=NE, image=esfera2)

def fasd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak: ")
        audio = r.listen(source)
        try:
            x= r.recognize_google(audio, language='es-ES')
            #print("transcription: " + x)
            entrada.insert(0, x)
        except sr.UnknownValueError:
            print("Audio unintelligible")
        except sr.RequestError as e:
            print("Cannot obtain results; {0}".format(e))

ventana = Tk()
ventana.title("Automata")
ventana.geometry("700x500")
ventana.config(bg="black")

"""texto = Label (ventana, text="palabra")
texto.grid(column=2, row=2, columnspan=1)"""

entrada = Entry(ventana, width=15, bg="pink")
entrada.grid(column=2, row=2)

boton = Button(ventana, text="validar", bg="pink", command=validar)
boton.grid(column=4, row=2)

boton = Button(ventana, text="limpiar", bg="pink", command=borrar)
boton.grid(column=7, row=2)

boton_escuchar = Button(ventana, text="grabar", bg="pink", command=lambda:fasd())
boton_escuchar.grid(column=6, row=2)

lienzo = Canvas(ventana, width=700, height=350, bg="black",  bd=0, highlightthickness=0, relief='ridge')
lienzo.grid(column=2, row=1, columnspan=17)

"""anim = MyLabel(lienzo, 'assets/aceptacion.gif')
anim.config(bg="black")
anim.place(x=100, y=150)"""

esfera = PhotoImage(file = "assets/imagen1.png")
esfera2 = PhotoImage(file = "assets/imagen2.png")
esfera3 = PhotoImage(file = "assets/imagen2.png")
flecha = PhotoImage(file = "assets/flecha2.png")
flecha2 = PhotoImage(file = "assets/flecha_iluminada2.png")
flecha3 = PhotoImage(file = "assets/imagen_recta1.png")
flecha4 = PhotoImage(file = "assets/flecha_rectailu1.png")
borde = PhotoImage(file = "assets/borde2.png")
apuntador = PhotoImage(file = "assets/apuntador.png")

imagen_esfera = lienzo.create_image(150, 100, anchor=NE, image=esfera)
flecha_esfera = lienzo.create_image(180, 70, anchor=NE, image=flecha)
flecha_esfera12 = lienzo.create_image(84, 140, anchor=NE, image=flecha3)
flecha_esfera122 = lienzo.create_image(260, 140, anchor=NE, image=flecha3)
borde_esfera = lienzo.create_image(513, 87, anchor=NE, image=borde)
imagen_esfera2 = lienzo.create_image(325, 100, anchor=NE, image=esfera)
flecha_esfera2 = lienzo.create_image(355, 70, anchor=NE, image=flecha)
flecha_esfera22 = lienzo.create_image(435, 140, anchor=NE, image=flecha3)
imagen_esfera3 = lienzo.create_image(500, 100, anchor=NE, image=esfera2)
mainloop()
