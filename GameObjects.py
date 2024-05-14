class Game:
    def __init__(self, name = None, unique_ID = None):
        self._name = name
        self._nPlayers = 0
        self._players = []
        self._deck_in_use = []
        self._deck_used = []
        self._hands = []
        self._bank = 0
        self._rounds = []
        self._roundcounter = 0
        self._unique_ID = unique_ID
        self._current_round = None
        self._actions = []
        self._check_func = None
        self._gameover = False
        self._action_identifier = None

    #-------------------
    # setters
    #-------------------
    def set_ID(self, ID):
        self._unique_ID = ID

    def set_recorder(self, recorder):
        self.Recorder = recorder

    def set_check_func(self, check_func: callable):
        self._check_func = check_func
    
    def set_action_identifier(self, identifier):
        self._action_identifier = identifier
    
    def game_starts(self):
        self._gameover = False

    def game_over(self):
        self._gameover = True
    
    def gameover(self):
        return self._gameover
    
    def get_roundnumber(self):
        return self._roundcounter
    
    #-------------------
    # player mechanics
    #-------------------

    def add_player(self, player: Player, hand = None):
        self._players.append(player)
        self._nPlayers += 1
        if hand:
            hand.set_player(player)
        elif len(self._hands) > 0:
            for hand in self._hands:
                if not hand.has_player():
                    hand.set_player(player)
                    return
        else:
            self._hands.append(Hand(player))
    
    def remove_player(self, player: Player, remove_hands: bool = False):
        self._players.remove(player)
        self._nPlayers -= 1
        hands_emptied = []
        for hand in self._hands:
            if hand.get_player() == player:
                hand.no_player()
                hands_emptied.append(hand)
        if remove_hands:
            self._hands -= hands_emptied

    #-------------------
    # deck mechanics
    #-------------------

    def import_deck(self, deck: list = [], valueDict: dict = None):
        self._deck_in_use += deck
        if valueDict:
            for card in deck:
                card.set_value(valueDict)
        
        from random import shuffle
        shuffle(self._deck_in_use)
    
    def empty_decks(self):
        deck_to_remove = self._deck_in_use + self._deck_used
        self._deck_in_use = []
        self._deck_used = []
        return deck_to_remove
    
    #-------------------
    # card mechanics
    #-------------------
    def deal_card(self, hand: Hand):
        if len(self._deck_in_use) == 0:
            self.recycle_cards()
        card = self._deck_in_use.pop()
        hand.add_card(card)
    
    def move_card(self, card: Card, fromHand: Hand, toHand: Hand):
        fromHand.remove_card(card)
        toHand.add_card(card)
    
    def junk_card(self, card: Card, hand: Hand):
        hand.remove_card(card)
        print(f"moving {card} to used deck...")
        self._deck_used.append(card)
        print(len(self._deck_used))
    
    def junk_cards(self, hand: Hand):
        while len(hand.get_cards()) > 0:
            self.junk_card(hand.get_cards()[0], hand)
    
    def junk_all(self, toJunk = []):
        for hand in toJunk:
            self.junk_cards(hand)
    
    def recycle_cards(self):
        while len(self._deck_used) > 0:
            print(f"recycling {self._deck_used[-1]}...")
            self._deck_in_use.append(self._deck_used.pop())

        from random import shuffle
        shuffle(self._deck_in_use)
    
    #-------------------
    # money mechanics
    #-------------------

    def move_money(self, amount: float, fromHand: Hand, toHand: Hand):
        fromHand.pays(amount)
        toHand.gains(amount)
    
    def empty_pots(self, extraHands: list = []):
        for hand in self._hands + extraHands:
            if hand.has_player():
                hand.takes_pot()

    #-------------------
    # game mechanics
    #-------------------
    
    def hands(self) -> list:
        return self._hands

    def check_options(self, hand: Hand):
        return self._check_func(hand)
    
    def start_round(self):
        self._roundcounter += 1
        thisRound = Round(self)
        self._rounds.append(thisRound)
        self._current_round = thisRound
        for hand in self._hands:
            hand._current_round = thisRound
            hand.start_round(thisRound)
        
        self._current_round = thisRound
    
    def set_main(self, func: callable):
        self.main = func
    
    def main(self):
        pass

    def action(self, hand: Hand, *args, **kwargs):
        action = Action(hand, self._current_round)
        action.set_type_identifier(self._action_identifier)
        action.set_options(self._check_func(hand))
        action.make_decision(*args, **kwargs)
        action.set_type()
        
        hash_id = GEN_HASH_ACTION(hand.get_player(), self._roundcounter, hand._action_number, action.ActionType)
        action.set_ID(hash_id)
        hand.record_action(action)
    
    def play_game(self):
        i = 0
        while True:
            self.start_round()
            self.main()
            if self.gameover() or input("play again? (y/n): ") == "n":
                self.recycle_cards()
                break
            i += 1


class Round:
    def __init__(self, game):
        self._game = game
        self._unique_ID = ""
        self._number = self._game.get_roundnumber()
        self._hands = []
        self._round_finished = False
        self._actions = []
        
        from datetime import datetime
        self._DateTime = datetime.now()

        self._actions = []

    def __str__(self) -> str:
        return f"round {self._number}"
    
    def __repr__(self) -> str:
        return f"round {self._number}"

    def set_ID(self, ID):
        self._unique_ID = ID
    
    def get_number(self):
        return self._number
    
    def record_action(self, action):
        self._actions.append(action)
    
    def set_hand(self, hand):
        self._hands.append(hand)

    def ended(self):
        self._round_finished = True
    
    def hands(self) -> list:
        return self._hands

class Action:
    def __init__(self, hand: Hand, round: Round):
        self.PlayerRoundID = ""
        self.ActionType = ""
        self.ActionSequence = hand._action_number
        self.player = hand.get_player()
        self.round = round
        self.hand = hand
        self.options = []
        self.result = None
        self.type_identifier = None

    def __str__(self) -> str:
        return f"{self.result} by {self.player} in round {self.round._number}."
    
    def __repr__(self) -> str:
        return f"{self.result} by {self.player} in round {self.round._number}."
    
    def set_ID(self, ID):
        self.PlayerRoundID = ID
    
    def get_ID(self):
        return self.PlayerRoundID
    
    def set_type_identifier(self, typeID):
        self.type_identifier = typeID

    def set_type(self):
        if self.result is dict:
            self.ActionType = self.result[self.type_identifier]
        elif self.result is list:
            self.ActionType = self.result[self.type_identifier]
        else:
            self.ActionType = self.result

    def set_options(self, options):
        self.options = options
    
    def make_decision(self, *args, **kwargs):
        doDecision = self.player.player_strategy(*args, **kwargs)
        self.set_result(doDecision)
    
    def set_result(self, result):
        self.result = result

    def append_result(self, key, value):
        self.result[key] = value
    
    def get_result(self):
        return self.result