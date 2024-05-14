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

- Game
- Round
- Action