from scripts.game import Game

if __name__ == "__main__":
    game = Game()
    while game.is_live:
        game.play()
    print('Exiting game')
