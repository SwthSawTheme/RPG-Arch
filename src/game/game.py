

class Game(object):


    def __init__(self,name):
        self.name = name
        self.player = None
        self.mobs = []


    def start(self):
        print(f"Bem vindo a Arch-RPG {self.name}")
        self.player = archery(input("Qual o seu nome bravo arqueiro: "))
        self.spawnMob()

    def spawnMob(self):
        mob = Mobs.generateRandomMob()