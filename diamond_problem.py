class Bilangan:
	def __init__(self, bilangan):
		self.bilangan = bilangan

class Genap(Bilangan):
	def __init__(self, bilangan):
		super().__init__(bilangan)

	def genap(self):
		if self.bilangan % 2 == 0:
			print("Bilangan Genap =")


class Ganjil(Bilangan):
	def __init__(self, bilangan):
		super().__init__(bilangan)

	def ganjil(self):
		if self.bilangan == 0:
			pass
		elif self.bilangan / int(self.bilangan) == 1:
			if self.bilangan % 2 != 0:
				print("Bilangan Ganjil =")



class Positif(Bilangan):
	def __init__(self, bilangan):
		super().__init__(bilangan)

	def positif(self):
		if self.bilangan >= 0:
			print("Bilangan Positif =")


class Negatif(Bilangan):
	def __init__(self, bilangan):
		super().__init__(bilangan)

	def negatif(self):
		if self.bilangan < 0:
			print("Bilangan Negatif =")



class Bulat(Bilangan):
	def __init__(self, bilangan):
		super().__init__(bilangan)

	def bulat(self):
		if self.bilangan == 0:
			print("Bilangan Bulat =")
		elif self.bilangan / int(self.bilangan) == 1:
			print("Bilangan Bulat =")



class Pecahan(Bilangan):
	def __init__(self, bilangan):
		super().__init__(bilangan)

	def pecahan(self):
		if self.bilangan == 0:
			pass
		elif self.bilangan / int(self.bilangan) != 1 :
			print("Bilangan Pecahan =")

class Prima(Genap, Ganjil, Positif, Negatif, Bulat, Pecahan):
	def __init__(self, bilangan):
		super().__init__(bilangan)

	def prima(self):
		if self.bilangan == 0:
			pass
		elif self.bilangan / int(self.bilangan) == 1:
			if self.bilangan > 1:
				for i in range (2, int(self.bilangan)):
					if (self.bilangan % i) == 0:
						break
				else:
					print("Bilangan Prima =")

objek = Prima(float(input()))
objek.prima()
objek.genap()
objek.ganjil()
objek.positif()
objek.negatif()
objek.bulat()
objek.pecahan()