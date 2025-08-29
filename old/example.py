
from ttt import Grid, Game


if __name__ =="__main__":
    import random

    grid = Grid()
    game = Game(grid, ["p1", "p2"]) 
    print(game.get_dim())

    while game._game_over is False:
        x = random.randrange(3)
        y = random.randrange(3)
        game.play_move(x,y)


