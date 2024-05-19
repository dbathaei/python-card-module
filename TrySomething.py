from GameObjects import *
from datetime import datetime

game = Game()
game_id = GEN_HASH_GAME("Poker", datetime.now(), 1)
game.set_ID(game_id)
print(game._unique_ID)

game.import_deck(DECK_GENERATOR())
print(game._deck_in_use)

print(game._deck_in_use[0]._unique_ID)

print(game._roundcounter)
game.start_round()