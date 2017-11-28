import warnings
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

if __name__ == '__main__':
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

	# Fingerprint all the mp3's in the directory we give it
	djv.fingerprint_directory("mp3", [".mp3"])

	# Recognize audio from a file
	song = djv.recognize(FileRecognizer, "mp3/si-0.mp3")
	print "Del archivo se ha reconocido: %s\n" % song

	# Or recognize audio from your microphone for `secs` seconds
	secs = 5
	song = djv.recognize(MicrophoneRecognizer, seconds=secs)
	if song is None:
		print "No se ha reconocido nada del microfono"
	else:
		print "Del microfono de los %d segundos se a reconocido: %s\n" % (secs, song)

	# Or use a recognizer without the shortcut, in anyway you would like
	recognizer = FileRecognizer(djv)#creando objeto archivo reconocedor del dejavu con la config dada
	song = recognizer.recognize_file("mp3/si-1.mp3")
	print "De la otra forma, se ha reconocido: %s\n" % song
