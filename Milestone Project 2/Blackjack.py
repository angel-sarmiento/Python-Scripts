#from IPython.display import clear_output
#import math
#import sys
import random


suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def aceChange(self):                        #method to change the ace from a value of 1 or 11
        if self.rank == 14 and self.value == 11:
            self.value = 1
        elif self.rank == 14 and self.value == 1:
            self.value = 11
    
    def __str__(self):
        if self.rank < 11:
            return f"{self.rank} of {self.suit}"
        elif self.rank == 11:
            return f"Jack of {self.suit}"
        elif self.rank == 12:
            return f"Queen of {self.suit}"
        elif self.rank == 13:
            return f"King of {self.suit}"
        elif self.rank == 14:
            return f"Ace of {self.suit}"


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)
    
    def __len__(self):
        return len(self.deck)

    

class Hand():

    def __init__(self):
        self.hand = []

    def draw(self,deck):
        selection = random.randint(0,len(deck)-1)
        print(deck.deck[selection])
        self.hand.append(deck.deck[selection])  
        del(deck.deck[selection])  
    

dick = Deck()
dick.shuffle()

lefthand = Hand()
lefthand.draw(dick)
lefthand.draw(dick)

