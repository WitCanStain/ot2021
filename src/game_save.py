import dill

def save(level):
    game_state = create_game_state(level)
    # with open("savegame", "wb") as f:
    #     dill.dump(state, f)

def create_game_state(level):
    print(level.__dict__)