from tkinter import *
import speech_recognition as sr 


class Guardador:
	def __init__(self):
		self.raiz =Tk()
		self.frame = Frame(self.raiz)
		self.textBox = None

	def crear_ventana(self):
		self.raiz.title("programa ventanas")

		self.titulo_texto = StringVar()
		self.frame.config(height=500, width=900, padx=15, pady=15)

		self.label1 = Label(self.frame, text="Titulo:")
		self.label1.grid(row=1, column=1)

		self.entrada = Entry(self.frame, textvariable=self.titulo_texto, width=53)
		self.entrada.grid(row=1, column=2)

		self.label1 = Label(self.frame, text="texto:")
		self.label1.grid(row=3, column=1)

		self.textBox=Text(self.frame, height=15, width=40)
		self.textBox.grid(row=4, column=2)

		scroll = Scrollbar(self.frame, command = self.textBox.yview)
		scroll.grid(row=4, column=3, sticky="nsew")
		#scroll.pack(side=RIGHT, fill=Y)

		self.textBox.config( yscrollcommand=scroll.set)



		boton = Button(self.frame, text="Enviar", command=lambda:self.guardar(self.titulo_texto.get()))
		boton.place(x=100, y=288)
		boton2 = Button(self.frame, text="grabar", command=lambda:self.transcripcion())
		boton2.grid(row=5, column=2)

		self.frame.pack()
		self.raiz.mainloop()


	"""def guardar(self, titulo):

		nombreArchivo = titulo + '.txt'
		file = open(nombreArchivo,"w")
		infoArchivo = self.texto()
		file.write(infoArchivo)
		file.close()"""

	def transcripcion(self):

		r = sr.Recognizer()

		with sr.Microphone() as source:
			print("Speak: ")
			audio = r.listen(source)

		try:
			x= r.recognize_google(audio, language='es-ES')
			#print("transcription: " + x)
			entrada.insert(0, x + ' ')
		except sr.UnknownValueError:
			print("Audio unintelligible")
		except sr.RequestError as e:
			print("Cannot obtain results; {0}".format(e))

	def texto(self):
	    inputValue=self.textBox.get("1.0","end-1c")
	    return inputValue




"""guardador = Guardador()
guardador.crear_ventana()"""

    



