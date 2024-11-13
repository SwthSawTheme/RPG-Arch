from src.game.game import Game
from src.characters.player import Player

class AdventureTextGame(Game):


    def __init__(self,name):
        super().__init__(name)


    def startAdventure(self):
        print("Iniciando Aventura!")
        self.start()

        while self.player