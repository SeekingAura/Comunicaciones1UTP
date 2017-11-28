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
recognizer = FileRecognizer(djv)#creando objeto archivo reconocedor del dejavu con la config dada
def reconocer
def menu():
	os.system("clear")
	print "Reconocedor de voz -- Menu principal"
	print "diga 'Escribir' para escribir una sola palabra"
	print "diga 'Ejecutar' para ejecutar lo escrito"
	print "diga 'Borrar' para borrar el texto actual"
	print "diga 'Cerrar' para Salir del programa"
	os.system('read -s -n 1 -p "Presione cualquier tecla para iniciar la detección de voz"')
	secs = 5
	print "reconociendo del microfno durante %d segundos" % (secs)
	sound = djv.recognize(MicrophoneRecognizer, seconds=secs)
	if sound is None:
		print "No se ha reconocido nada del microfono"
		return None
	else:
		print "Del microfono de los %d segundos se a reconocido: %s\n" % (secs, song)

class compilarVoz(object):
	def __init__:
		self.texto=""
		self.seconds=5
		self.soundMicrofone=None
	def menu(self):
		os.system("clear")
		print "Reconocedor de voz -- Menu principal"
		print "diga 'Escribir' para escribir una sola palabra"
		print "diga 'Ejecutar' para ejecutar lo escrito"
		print "diga 'Borrar' para borrar el texto actual"
		print "diga 'Cerrar' para Salir del programa"
		# comando para realizar pause en Linux o ubuntu
		comando=self.tomarVoz()
		return comando

	def determinarComando(self):
		

	def tomarVoz(self):
		os.system('read -s -n 1 -p "Presione cualquier tecla para iniciar la detección de voz por microfono"')
		secs = 5
		print "reconociendo del microfono durante %d segundos" % (self.seconds)
		sound = djv.recognize(MicrophoneRecognizer, seconds=self.seconds)
		if sound is None:
			print "No se ha reconocido nada del microfono"
			return None
		else:
			print "Del microfono de los %d segundos se a reconocido: %s\n" % (secs, song)

if __name__ == '__main__':


	# Fingerprint a todos los archivos que hay en una carpeta (banco de conocimiento)
	djv.fingerprint_directory("mp3", [".mp3"])

	# Or recognize audio from your microphone for `secs` seconds
	secs = 5
	print "reconociendo del microfno durante %d segundos" % (secs)
	song = djv.recognize(MicrophoneRecognizer, seconds=secs)

	if song is None:
		print "No se ha reconocido nada del microfono"
	else:
		print "Del microfono de los %d segundos se a reconocido: %s\n" % (secs, song)

	# Or use a recognizer without the shortcut, in anyway you would like

	song = recognizer.recognize_file("mp3/si-1.mp3")
	print "Del archivo, se ha reconocido: %s\n" % song
