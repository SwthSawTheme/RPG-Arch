from src.game.game import Game

class AdventureTextGame(Game):


    def __init__(self,name):
        super().__init__(name)


    def startAdventure(self):
        print("Iniciando Aventura!")
        self.start()
        while self.player.isAlive() and len(self.mobs) > 0:
            current_mob = self.mobs[0]
            print(f"Lutando contra {current_mob.type}!")
            self.player.attack(current_mob)
            if current_mob.isAlive():
                current_mob.attack(self.player)
            else:
                print(f"Você derrotou o {current_mob.type}!")
                self.mobs.pop(0)
            self.getStatus()
    
    def getStatus(self):
        if not self.player.isAlive():
            print("Você foi morto! Fim de jogo.")
        elif len(self.mobs) == 0:
            print("Parabéns, você venceu todos os mobs!")
        else:
            print(f"Vida do Arqueiro: {self.player.health}")
            print(f"Flechas restantes: {self.player.arrows}")