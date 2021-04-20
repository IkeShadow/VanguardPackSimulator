#!/usr/bin/python3
import random


class OGSets:

	# sets in classic series / Will be Updated over time
	sets = ["BT01-EN", "BT02-EN", "BT03-EN"]

	# Create rarity arrays of set
	def __init__(self):
		self.common = []
		self.rare = []
		self.do_rare = []
		self.tri_rare = []

	# Adds card to correct rarity array
	def add_card(self, rarity, cardname):
		if rarity == "C":
			self.common.append(cardname)
		if rarity == "R":
			self.rare.append(cardname)
		if rarity == "RR":
			self.do_rare.append(cardname)
		if rarity == "RRR":
			self.tri_rare.append(cardname)

	# Shuffles the rarity listings
	def shuffle(self):
		random.shuffle(self.common)
		random.shuffle(self.rare)
		random.shuffle(self.do_rare)
		random.shuffle(self.tri_rare)

	# Returns a pack of a given set
	def create_pack(self):
		self.shuffle()
		pack = []
		for i in range(0, 4):
			pack.append(self.common[i] + "; C")
		rarity = random.randint(0, 89)
		if rarity in range(80, 90):
			pack.append(self.tri_rare[0] + "; RRR")
		elif rarity in range(65, 80):
			pack.append(self.do_rare[0] + "; RR")
		else:
			pack.append(self.rare[0] + "; R")
		return pack

	def pull_card(self, rarity):
		self.shuffle()
		if rarity == "Common":
			return self.common[0]
		elif rarity == "R":
			return self.rare[0]
		elif rarity == "RR":
			return self.do_rare[0]
		elif rarity == "RRR":
			return self.tri_rare[0]