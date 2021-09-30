class Timer():

	# Init Var
	chrono = 0

	def reset(self):
		self.chrono = 0

	def upTime(self):
		self.chrono += 1/60

	def getTime(self):
		return self.chrono