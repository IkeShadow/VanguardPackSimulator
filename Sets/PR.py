import random


class PRSets:
    #List of promo sets, highly subject to change
    sets = ["PR1", "SPR1", "PR2", "SPR2"]

    def __init__(self):
        self.pack = []

    def add_card(self, cardname):
        self.pack.append(cardname)

    def shuffle(self):
        random.shuffle(self.pack)

    def create_pack(self):
        self.shuffle()
        pack = self.pack[0]

        return pack
