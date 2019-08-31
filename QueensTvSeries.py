class Soldier:
	def __init__(self, first,last,major="Private"):
		self.first = first
		self.last = last
		self.major = major
	def full(self):
		return "{} {}".format(self.first,self.last)
sol1 = Soldier("HayWhy", "Dooble")
sol2 = Soldier("Cane","Scholl","Leiutenant")
print(sol1.major)