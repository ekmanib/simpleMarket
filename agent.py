import numpy as np 

class Agent(object):
	""" 
	Agent class contain attributes and methods for basic agent in simple market model
	"""
	def __init__(self, id, role):
		"""
		Class initializes with following parameters

		`id`: agent's unique id
		`role`: 1 if agent is a producer or 2 if agent is a consumer
		`w2p`: consumer's willingness to pay
		`w2a`: producer's willinsness to accept
		`inc_strat`: increse in price strategy space
		"""
		self.id = id 
		self.role = role 
		self.w2p = self.set_WTP()
		self.w2a = self.set_WTA()
		self.prev_price = 0
		self.success = False

	def __str__(self):
		lines = []
		lines.append("----------------")
		lines.append("Player No." + str(self.id))
		if self.role == 1:
			lines.append("Producer's willingness to accept:\n\t"+ str(self.w2a))
		if self.role == 2:
			lines.append("Consumer's willingness to pay:\n\t" + str(self.w2p))
		lines.append("----------------")
		return '\n'.join(lines)


	def set_WTP(self):
		# function sets willing to pay parameter for consumer agent
		x = 0
		if self.role == 2:
			x = np.random.normal(10, 2.5)

		return x


	def set_WTA(self):
		# function sets willing to accept parameter for prodcuer agent
		x = 0
		if self.role == 1:
			x = np.random.normal(10, 2.5)
 
		return x

	def set_askingPriceStrat(self):
		# function sets the producer's asking price to be posted
		price = self.prev_price
		if self.success == False:
			if self.prev_price <= self.w2a:
				price = self.w2a
			elif self.prev_price > self.w2a:
				price = price * (0.99)
		elif self.success == True:
			price = price * (1.01)

		# print(self.prev_price, self.w2a, price)

		return price