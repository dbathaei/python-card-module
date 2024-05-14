from BaseObjects import Card
from IDgenerator import GEN_HASH_CARD
from random import shuffle

def DECK_GENERATOR(nDecks: int = 1, jokers: bool = False, aValueDict = None):
    deck = []
    faces = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    for deck_number in range(1, nDecks+1):
        for suit in suits:
            for face in faces:
                hash_id = GEN_HASH_CARD(face, suit, deck_number)
                thisCard = Card(face, suit)
                if aValueDict:
                    thisCard.set_value(aValueDict)
                thisCard.set_ID(hash_id)
                deck.append(thisCard)

        if jokers == True:
            for _ in range(2):
                if _ == 0:
                    jsuit = "Red"
                else:
                    jsuit = "Black"
                hash_id = GEN_HASH_CARD("Joker", jsuit, deck_number)
                deck.append(Card("Joker", jsuit, aValueDict))
    shuffle(deck)
    return deck

