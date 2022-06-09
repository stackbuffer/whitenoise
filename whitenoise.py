import wavio
import numpy as np
from pydub import AudioSegment
from pydub.playback import play


class WhiteNoise:
	def __init__(self, samples, samplerate, filename):
		self.samples = samples
		self.samplerate = samplerate
		self.filename = filename


	def generate(self):
		x = []
		l = []

		x.append(np.random.random(size = self.samples))

		for i in x:
			for j in i:
				l.append(j)

		l = np.array(l)

		wavio.write(self.filename, l, self.samplerate, sampwidth=2)


	def playNoise(self):
		song = AudioSegment.from_wav(self.filename)
		play(song)



noise = WhiteNoise(300000, 44100, "noise.wav")
noise.generate()
noise.playNoise()
