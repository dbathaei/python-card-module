class Card:
    GEN_INDEX = {
        "Ace": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Joker": 14
    }

    def __init__(self, face, suit):
        self._face = face
        self._suit = suit
        self._value = self.get_value()
        self._special_attribute = False
        self._unique_ID = None
    
    def __str__(self) -> str:
        if self._face == "Joker":
            return "Joker"
        return f"{self._face} of {self._suit}"
    
    def __repr__(self) -> str:
        if self._face == "Joker":
            return "Joker"
        return f"{self._face} of {self._suit}"
    
    #-------------------
    # setters
    #-------------------

    def set_ID(self, ID):
        self._unique_ID = ID
    
    def set_value(self, valueDict: dict):
        self._value = valueDict[self._face]
    
    def set_value_direct(self, value: int):
        self._value = value
    
    #-------------------
    # getters
    #-------------------
    
    def face(self) -> str:
        return self._face
    
    def suit(self) -> str:
        return self._suit
    
    def value(self) -> int:
        return self._value
    
    def ID(self) -> int:
        return self._unique_ID
    
    def special(self) -> bool:
        return self._special_attribute

    def get_value(self) -> int:
        return int(self.GEN_INDEX[self._face])

class Player:
    def __init__(self, name, money = 0, DOB: int = 00000000, unique_ID = None):
        self._name = name
        self._money = money
        self._DOB = DOB # yyyymmdd
        self._hands = []
        self._unique_ID = unique_ID
        self._betting_strategy = None
        self._playing_strategy = None
    
    def __str__(self) -> str:
        return self._name
    
    def __repr__(self) -> str:
        return self._name
    
    #-------------------
    # setters
    #-------------------
    def set_hand(self, hand):
        self._hands.append(hand)
    
    def remove_hand(self, hand):
        self._hands.remove(hand)

    def set_ID(self, ID):
        self._unique_ID = ID
    
    def set_strategy(self, strategy, type):
        if type == "bet":
            self._betting_strategy = strategy
        elif type == "play":
            self._playing_strategy = strategy

    
    #-------------------
    # getters
    #-------------------
    def name(self) -> str:
        return self._name
    
    def money(self) -> float:
        return self._money
    
    def DOB(self) -> int:
        return self._DOB
    
    def bet_strategy(self, *args, **kwargs):
        return self._betting_strategy(*args, **kwargs)

    def player_strategy(self, *args, **kwargs):
        return self._playing_strategy(*args, **kwargs)
    
    #-------------------
    # cash mechanics
    #-------------------

    def get_chips(self, amount: float):
        self._money += amount

    def buys_in(self, amount: float, hand):
        self._money -= amount
        hand._total_cash += amount
    
    def cashes_out(self, hand):
        self._money += hand._total_cash
        hand._total_cash = 0


class Hand:
    def __init__(self, player = None, unique_ID = None):
        self._cards = []
        self._values = []
        self._value = 0
        self._special_attributes = {}
        self._total_cash = 0
        self._pot = 0
        self._lost = False
        self._won = False
        self._stop = True
        self._player = None
        self.set_player(player)
        self._unique_ID = unique_ID
        self._extra = False
        self._rounds = {}
        self._current_round = None
        self._action_number = 1
    
    def __str__(self) -> str:
        return f"{self._player}'s hand"
    
    def __repr__(self) -> str:
        return f"{self._player}'s hand"
    
    #-------------------
    # setters
    #-------------------

    def set_ID(self, ID):
        self._unique_ID = ID
    
    def set_player(self, player = None):
        if self._player:
            if self._player != player:
                self._player.remove_hand(self)

        if player == None:
            self._player = player
        else:
            self._player = player
            player.set_hand(self)


    def reset_hand(self):
        self._cards = []
        self._values = []
        self._value = 0
        self._special_attributes = {}
        self._lost = False
        self._won = False
        self._stop = True
        self._extra = False
        self._action_number = 1

    def set_sa(self, attribute: str, someValue = True):
        self._special_attributes[attribute] = someValue   
    
    #-------------------
    # getters
    #-------------------
    def get_action_number(self) -> int:
        return self._action_number
    
    def has_player(self) -> bool:
        return self._player != None
    
    def get_player(self):
        return self._player

    def is_playing(self) -> bool:
        return not self._stop
    
    # def get_special_attribute(self, attribute: str):
    #     return self._special_attributes[attribute]
    
    def get_cards(self):
        return self._cards
    
    def values(self):
        return self._values
    
    def value(self):
        return self._value
    
    def total_cash(self):
        return self._total_cash
    
    def pot(self):
        return self._pot

    def check_sa(self, attribute: str):
        return self._special_attributes.get(attribute, False)
    #-------------------
    # status
    #-------------------

    def is_extra(self):
        self._extra = True
    
    def stops(self):
        self._stop = True

    def starts(self):
        self._stop = False

    def wins(self):
        self._won = True
    
    def loses(self):
        self._lost = True


    #-------------------
    # card mechanics
    #-------------------

    def add_card(self, card: Card):
        self._cards.append(card)
        self._values.append(card.value())
        self.sum_values()
    
    def remove_card(self, card: Card):
        cIndex = self._cards.index(card)
        self._cards.remove(card)
        self._values.pop(cIndex)
        self.sum_values()

    #-------------------
    # cash mechanics
    #-------------------

    def load_cash(self, amount: float):
        if self._player.money() >= amount:
            self._player.buys_in(amount, self)
    
    def cash_out(self):
        self._player.cashes_out(self._total_cash)
    
    def bets(self, amount: float):
        if self.can_pay_bet(amount):
            self._total_cash -= amount
            self._pot += amount
        else:
            return f"{self._player} has insufficient funds."
    
    def gains(self, amount: float):
        self._pot += amount
    
    def pays(self, amount: float):
        self._pot -= amount
    
    def takes_pot(self):
        self._total_cash += self._pot
        self._pot = 0
    
    #-------------------
    # maint, methods, calcs
    #-------------------

    def sum_values(self):
        running_total = 0
        for value in self._values:
            running_total += value
        self._value = running_total
    
    def can_pay_bet(self, amount: float):
        if self._total_cash < amount:
            return False
        else:
            return True
        
    #-------------------
    # round mechanics
    #-------------------

    def start_round(self, round):
        round_name = f"round_{round.get_number()}"
        self._rounds.update({round_name: []})
        self._current_round = round
        round.set_hand(self)
        
    def record_action(self, action):
        print(f"Recording action: {action}")
        self._action_number += 1
        round_name = f"round_{self._current_round._number}"
        if round_name not in self._rounds:
            self._rounds[round_name] = []
        self._rounds[round_name].append(action)
        self._current_round.record_action(action)