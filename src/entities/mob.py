from src.characters.player import Player
import random

class Mob(object):

    types = ["Goblin","Orc","Troll"]

    def __init__(self,type:str,health:int,damage:int):
        self.type = type
        self.health = health
        self.damage = damage

    def attack(self,player:"Player"):
        pass

    def takeDamage(self,value:int):
        pass

    def isAlive(self) -> bool:
        pass

    @classmethod
    def generateRandomMob(cls):
        type = random.choice(cls.types)
        health = random.randint(20,50)
        damage = random.randint(3,10)
        return cls(type,health,damage)