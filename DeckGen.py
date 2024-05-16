from BaseObjects import Card
from IDgenerator import GEN_HASH_CARD
from random import shuffle

def DECK_GENERATOR(nDecks: int = 1, jokers: bool = False, aValueDict = None):

    # deck to be returned
    deck = []

    # faces and suits
    faces = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    # creates `nDecks` decks.
    for deck_number in range(1, nDecks+1):

        # iterates through suits and faces.
        for suit in suits:
            for face in faces:

                # generates a unique ID for each card.
                hash_id = GEN_HASH_CARD(face, suit, deck_number)

                # instatiates a card object.
                thisCard = Card(face, suit)
                if aValueDict:
                    thisCard.set_value(aValueDict)
                
                # sets the unique ID for the card.
                thisCard.set_ID(hash_id)
                deck.append(thisCard)

        # if jokers are to be included, add them to the deck.
        if jokers == True:
            hash_id = GEN_HASH_CARD("Joker", "Red", deck_number)
            deck.append(Card("Joker", "Red", aValueDict))
            hash_id = GEN_HASH_CARD("Joker", "Black", deck_number)
            deck.append(Card("Joker", "Black", aValueDict))
    
    return deck

