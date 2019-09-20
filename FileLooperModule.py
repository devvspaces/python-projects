class fileObject:
	def __init__(self,name):
		self.name=name
	def isDir(self):
		try:
			with open(self.name, "r") as f:
				pass
		except IsADirectoryError:
			return True
		return False