import random


class Dice:
    def __init__(self, bottom_range, top_range):
        self.bottom_range = bottom_range
        self.top_range = top_range

    # returns a tuple of 2 dices
    def roll(self):
        dice1 = random.randint(self.bottom_range, self.top_range)
        dice2 = random.randint(self.bottom_range, self.top_range)
        return dice1, dice2
