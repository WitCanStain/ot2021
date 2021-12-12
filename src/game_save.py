import os
import pickle

dirname = os.path.dirname(__file__)

def save_game(game_state):
    path = os.path.join(dirname, "saved_games", "savegame")
    with open(path, "wb") as f:
        pickle.dump(game_state, f)

def load_game(save_file):

    game_state = None
    with open(save_file, "rb") as f:
        game_state = pickle.load(f)
    return game_state