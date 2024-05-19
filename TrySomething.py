from GameObjects import *
from datetime import datetime

game = Game()
game_id = GEN_HASH_GAME("Poker", datetime.now(), 1)
game.set_ID(game_id)
print(game._unique_ID)
