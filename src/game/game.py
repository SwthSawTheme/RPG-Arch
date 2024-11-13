from src.entities.mob import Mob
from src.characters.archery import Archery

class Game(object):


    def __init__(self,name):
        self.name = name
        self.player = None
        self.mobs = []


    def start(self):
        print(f"Bem vindo a Arch-RPG {self.name}")
        self.player = Archery(input("Qual o seu nome bravo arqueiro: "))
        self.spawnMob()

    def spawnMob(self):
        mob = Mob.generateRandomMob()
        self.mobs.append(mob)
        print(f"Um {mob.type} apareceu!")