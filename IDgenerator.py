import hashlib

# hash for cards
def GEN_HASH_CARD(face, suit, deck_number):
    unique_identifier = f"{face}-{suit}-{deck_number}"
    hash_object = hashlib.md5(unique_identifier.encode())
    return hash_object.hexdigest()

# hash for player
def GEN_HASH_PLAYER(player):
    unique_identifier = f"{player._name}-{player._DOB}"
    hash_object = hashlib.md5(unique_identifier.encode())
    return hash_object.hexdigest()

# hash for round
def GEN_HASH_ROUND(round_number, game):
    player_ids = '-'.join(sorted([str(player._unique_ID) for player in game._players]))
    unique_identifier = f"{player_ids}-{round_number}"
    hash_object = hashlib.md5(unique_identifier.encode())
    return hash_object.hexdigest()

# hash for action
def GEN_HASH_ACTION(player, round_number, action_sequence, action_type):
    unique_identifier = f"{player._unique_ID}-{round_number}-{action_sequence}-{action_type}"
    hash_object = hashlib.md5(unique_identifier.encode())
    return hash_object.hexdigest()

# hash for round
def GEN_HASH_PLAYERROUND(player, round_number):
    unique_identifier = f"{player._unique_ID}-{round_number}"
    hash_object = hashlib.md5(unique_identifier.encode())
    return hash_object.hexdigest()


def GEN_HASH_GAME(game, date_time, game_number):
    unique_identifier = f"{game}-{date_time}-{game_number}"
    hash_object = hashlib.md5(unique_identifier.encode())
    return hash_object.hexdigest()