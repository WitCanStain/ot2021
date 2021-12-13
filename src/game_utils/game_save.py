import os
import pickle

dirname = os.path.dirname(__file__)

class GameSave():

    def save_game(game_state):
        """Serialises the game_state into an output file.

        Args:
            game_state: game state data.

        Returns:
            bool: A boolean value indicating success or failure.
        """
        try:
            path = os.path.join(dirname, "..", "saved_games", "savegame")
            with open(path, "wb") as file:
                pickle.dump(game_state, file)
            return True
        except Exception as error:
            print(error)
            return False

    def load_game(save_file):
        """Loads game state data from the given save_file.

        Args:
            save_file: the save file from which data is being read.

        Returns:
            game_state: deserialised game state data.
        """

        game_state = None
        with open(save_file, "rb") as file:
            game_state = pickle.load(file)
        return game_state
