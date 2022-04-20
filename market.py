from agent import Agent
import numpy as np
import matplotlib.pyplot as plt

class Market(object):
	"""
	Market class
	"""

	def __init__(self, pop, c_pct=0.5):
		""" 
		Class initializes with 

		`p`: population of agent's interacting in market
		`c_pct`: proportion of consumers in the market
		"""
		self.pop = pop
		self.agents_ = [Agent(i, np.random.choice([1, 2], p = [1 - c_pct, c_pct])) for i in range(self.pop)]

	def random_q(self, q=5):
		""" 
		function loops through each consumer. For each consumer there will be 5 producers selected randomly. \\
		Each producer will make an offer - establish and present an asking price . Then, the consumer will sort \\
		through all asking prices and select the lowest that must also be below its maximum willingness to pay. 
		"""

		# create a list for resulting prices
		PR = []

		# create lists separating consumers and producers
		C = [a for a in self.agents_ if a.role == 2]
		P = [a for a in self.agents_ if a.role == 1]
		# loop through all consumers
		for a in C:
			# select q producers randomly
			p_q = np.random.choice(P, q, replace=False)
			# create a dictionary containing pairs of producers and their offering prices
			prices_dict = {}
			for p in p_q:
				prices_dict[p] = p.set_askingPriceStrat()
			# update prev_price for producers such that they'll remember their price in the inmidiate last interaction
			for item, pr in prices_dict.items():
				item.prev_price = pr


			# print(prices_dict.values())


			# sort through the prices in the produces, prices pairs and select the lowest
			offer_best = sorted(prices_dict.items(), key = lambda item: item[1])[0]
			# get lowest price
			pr_best = offer_best[1]
			# get producer offering lowest price
			p_best = offer_best[0]


			# print(pr_best)

			if pr_best < a.w2p:
				# include this price as it was materialized during a successful transaction
				PR.append(pr_best)
				# signal to the agent that transaction was a success
				p_best.success = True


		for p in P:
			p.success = False


		return PR


	def info_complete(self):
		""" 
		function loops through each consumer. The consumer has access to the full list of prices. \\
		The consumer then sorts the list of prices and calls up the producer with the lowest price and,  \\
		if and only if the producer has not yet sold the good before, the consumer makes a bid. Then, \\
		the producer accepts to sell if the bid is greater then his minimun willing to accept.
		"""

		pass

	def plot_pricesCDF(self, vect):
		# number of data points
		n = len(vect)
		# sort through the data
		x = np.sort(vect)
		# get relative frequency for each point in the data
		y = np.arange(1, n+1)/n

		fig, axes = plt.subplots()

		axes = plt.plot(x, y)

		return axes
