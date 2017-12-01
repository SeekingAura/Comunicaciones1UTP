import warnings
warnings.filterwarnings("ignore")
import os
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

config = {
	"database": {
	"host": "127.0.0.1",
	"user": "root",
	"passwd": "seek1088",
	"db": "dejavu"
	}
}#estableciendo parametros de la base de datos
# create a Dejavu instance
djv = Dejavu(config)
#djv.recognize(FileRecognizer, "mp3/Sean-Fournier--Falling-For-You.mp3")


class compilarVoz(object):
	def __init__(self):
		self.texto=""
		self.seconds=5
		self.soundMicrofone=None
		# Fingerprint a todos los archivos que hay en una carpeta (banco de conocimiento)
		djv.fingerprint_directory("mp3", [".mp3"])
		djv.recognize(MicrophoneRecognizer, seconds=1)

	def programa(self):
		os.system("clear")
		print "Reconocedor de voz -- Menu principal"
		print "diga 'Escribir' para escribir una sola palabra"
		print "diga 'Ejecutar' para ejecutar lo escrito"
		print "diga 'Borrar' para borrar el texto actual"
		print "diga 'Cerrar' para Salir del programa"
		print "palabra actual %s" % (self.texto)
		# comando para realizar pause en Linux o ubuntu
		comando=self.tomarVoz()
		return comando

	def determinarComando(self, song):
		temp=""
		for i in song['song_name']:
			if i=="-":
				break
			else:
				temp+=i
		return temp


	def tomarVoz(self):
		raw_input("presione Enter para iniciar con el reconocimiento por el microfono")

		print "reconociendo del microfono durante %d segundos" % (self.seconds)
		sound = djv.recognize(MicrophoneRecognizer, seconds=self.seconds)
		if sound is None:
			print "No se ha reconocido nada del microfono"
			raw_input("presione Enter para continuar")
			return None
		else:
			print "Del microfono de los %d segundos se a reconocido: %s\n" % (self.seconds, sound)
			#print "Del microfono de los %d segundos se a reconocido: %s\n" % (self.seconds, self.determinarComando(sound))
			raw_input("presione Enter para continuar")
			return self.determinarComando(sound)

	def escribirPalabra(self):
		print "procesando para escribir palabra"
		value=self.tomarVoz()
		if value is not None:
			print "la palabra reconocida es %s" % (value)
			while(True):
				temp=raw_input("Desea agregarlo? s/n \n")
				if(temp=="s"):
					print "Agregado"
					self.texto+=value
					break
				elif(temp=="n"):
					print "Descartado"
					break
				else:
					print "el comando indicado es incorrecto"
		else:
			print "No se ha entendido lo indicado por microfono"

		while(True):
			temp=raw_input("Desea agregar mas? s/n \n")
			if(temp=="s"):
				self.escribirPalabra()
				break
			elif(temp=="n"):
				return
			else:
				print "el comando indicado es incorrecto"
if __name__ == '__main__':


	print("Creando objeto de reconocimiento")
	recognizeVoz=compilarVoz()
	raw_input("Todo listo presione enter para continuar")
	# Or recognize audio from your microphone for `secs` seconds
	salir=False
	while(not salir):
		value=recognizeVoz.programa()
		if value is not None:
			print "se ha recibido el comando %s" % (value)
			while(True):
				temp=raw_input("desea procesar? s/n \n")
				if(temp=="s"):
					if value=="cerrar":
						salir=True
						break
					elif value=="escribir":
						recognizeVoz.escribirPalabra()
						break
					elif value=="ejecutar":
						os.system(recognizeVoz.texto)
						raw_input("presione Enter para continuar")
						break
					elif value=="borrar":
						recognizeVoz.texto=""
						break
				elif(temp=="n"):
					break
				else:
					print "el comando indicado es incorrecto"
