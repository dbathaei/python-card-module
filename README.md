# Python Card Module

#### A card module made in python.

## Base Objects

- **Card**
    - **Attributes**
        - _face = Clubs, Diamonds, Hearts, Spades
        - _suit = Ace, ...., 10, Jack, Queen, King, Joker
        - _special_attribute = T/F
        - _unique_ID = md5 ID.
    
    - **Methods**
        - set_ID(id)
        - set_value(valueDict: dict)
        - set_value_direct(value: int)

        - face()
        - suit()
        - value()
        - ID()
        - special()
        - get_value()

- **Player**
    - **Attributes**
        - _name = string
        - _money = integer
        - _DOB = yyymmdd
        - _hands = list
        - _unique_ID = md5 ID.
        - _betting_strategy = callable
        - _playing_strategy = callable
    
    - **Methods**
        - set_hand(hand: Hand)
        - remove_hand(hand: Hand)
        - set_ID(id)
        - set_strategy(strategy: callable, type = "bet" or "play")
        - name()
        - money()
        - DOB()
        - bet_strategy(*args, **kwargs)
        - player_strategy(*args, **kwargs)
        - get_chips(amount: float)
        - buys_in(amount: float, hand: Hand)
        - cashes_out(hand: Hand)

- **Hand**
    - **Attributes**
        - _cards = list
        - _values = list
        - _value = int
        - _special_attributes = dict
        - _total_cash = integer
        - _pot = 0
        - _lost = T/F
        - _won = T/F
        - _stop = T/F
        - _player = class Player
        - _unique_ID = md5 ID.
        - _extra = T/F
        - _rounds = dict
        - _current_round = class Round
        - _action_number = int
    
    - **Methods**
        - set_ID(id)
        - set_player(player: Player)
        - reset_hand()
        - set_sa(attribute: str, someValue = True)
        - get_action_number()
        - has_player()
        - get_player()
        - is_playing()
        - get_cards()
        - values()
        - value()
        - total_cash()
        - pot()
        - check_sa(attribute: str)
        - is_extra()
        - stops()
        - starts()
        - wins()
        - loses()
        - add_card(card: Card)
        - remove_card(card: Card)
        - load_cash(amount: float)
        - cash_out()
        - bets(amount: float)
        - gains(amount: float)
        - takes_pot()
        - sum_values()
        - can_pay_bet(amount: float)
        - start_round(round: Round)
        - record_action(action: Action)

## Game Objects

- **Game**
    - **Attributes**
        - _name = str
        - _nPlayers = int
        - _players = list
        - _deck_in_use = list
        - _deck_used = list
        - _hands = list
        - _bank = float
        - _rounds = list
        - _roundcounter = int
        - _unique_ID = md5 ID.
        - _current_round = class Round
        - _actions = list
        - _check_func = callable
        - _gameover = T/F
        - _action_identifier = any
    
    - **Methods**
        - set_ID(id)
        - set_check_func(check_func: callable)
        - set_action_identifier(identifier: any)
        - game_starts()
        - game_over()
        - gameover()
        - get_roundnumber()
        - add_player(player: Player, hand: Hand)
        - remove_player(player: Player, remove_hands: bool)
        - import_deck(deck: list, valueDict: dict)
        - empty_decks() --> THIS RETURNS the decks for storing.
        - deal_card(hand: Hand)
        - move_card(card: Card, fromHand, toHand)
        - junk_card(card: Card, hand: Hand)
        - junk_cards(hand: Hand)
        - junk_all(toJunk: list)
        - recycle_cards()
        - move_money(amount: float, fromHand, toHand)
        - empty_pots(extraHands: list)
        - hands()
        - check_options(hand: Hand)
        - start_round()
        - set_main(func: callable)
        - main()
        - action(hand: Hand, *args, **kwargs):
        - play_game() ==> still working on this.


- **Round**
    - **Attributes**
        - _game = class Game
        - _unique_ID = md5 ID.
        - _number = self._game.get_roundnumber()
        - _hands = list
        - _round_finished = T/F
        - _actions = list
    - **Methods**
        - set_ID(id)
        - get_number()
        - record_action(action: any)
        - set_hand(hand: Hand)
        - ended()
        - hands()
- **Action** (constructed with a Hand, and a Round)
    - **Attributes**
        - PlayerRoundID = md5 ID.
        - ActionType = any
        - ActionSequence = hand._action_number
        - player = hand.get_player()
        - round = class Round
        - hand = class Hand
        - options = list
        - results = any
        - type_identifier = any

    - **Methods**
        - set_ID(id)
        - get_ID(id)
        - set_type_identifier(typeID: any)
        - set_type()
        - set_options(options)
        - make_decision(*args, **kwargs)
        - set_result(result)
        - append_result(key, value)
        - get_result()
        