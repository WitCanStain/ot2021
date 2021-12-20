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
        except:
            print(error)
            print("Something went wrong - saving was unsuccessful!")
            return False

    def load_game(save_file):
        """Loads game state data from the given save_file, attempting to first load the file as a path and then
        as a file within the save_games directory.

        Args:
            save_file: the save file from which data is being read.

        Returns:
            game_state: deserialised game state data.
        """
        try:
            if os.path.exists(save_file):
                path = save_file
            else:
                path = os.path.join(dirname, "..", "saved_games", save_file)
            
            game_state = None
            with open(path, "rb") as file:
                game_state = pickle.load(file)
            return game_state

        except FileNotFoundError as error:
            print(error)
            print("Savefile not found! Are you sure it exists in the saved_games folder?")
            return False

    def generate_level_map_from_file(map_file):
        """Generates a level map from the given file, attempting to first load the file as a path and then
        as a file within the level_maps directory.

        Args:
            map_file: the map file from which data is being read.
        
        Returns:
            level_map: a list object representing the generated level map.
        """
        try:
            level_map = []
            if os.path.exists(map_file):
                path = map_file
            else:
                path = os.path.join(dirname, "..", "level_maps", map_file)
            with open(path, "rb") as file:
                level_map = [line for line in file.read().decode().splitlines()]
                print(level_map)
            return level_map
        except FileNotFoundError as error:
            print(error)
            print("Level map file not found! Did you type in the name correctly?")
            return False
        



