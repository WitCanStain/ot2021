import os
import pickle

dirname = os.path.dirname(__file__)

def save_game(game_state):
    """Serialises the game_state into an output file.

    Args:
        game_state: game state data.

    Returns:
        bool: A boolean value indicating success or failure.
    """
    try:
        path = os.path.join(dirname, "saved_games", "savegame")
        with open(path, "wb") as f:
            pickle.dump(game_state, f)
        return True
    except Exception as e:
        print(e)
        return False

def load_game(save_file):
    """Loads game state data from the given save_file.

    Args:
        save_file: the save file from which data is being read.

    Returns:
        game_state: deserialised game state data.
    """

    game_state = None
    with open(save_file, "rb") as f:
        game_state = pickle.load(f)
    return game_state