from src.characters.player import Player
import random

class Mob(object):

    types = ["Goblin","Orc","Troll"]

    def __init__(self,type:str,health:int,damage:int):
        self.type = type
        self.health = health
        self.damage = damage

    def attack(self,player:"Player"):
        print(f"{self.type} ataca {player.name} causando {self.damage} de dano.")
        player.takeDamage(self.damage)

    def takeDamage(self,value:int):
        self.health -= value
        print(f"{self.type} tomou {value} de dano! Vida atual: {self.health}")


    def isAlive(self) -> bool:
        return self.health > 0

    @classmethod
    def generateRandomMob(cls):
        type = random.choice(cls.types)
        health = random.randint(20,50)
        damage = random.randint(3,10)
        return cls(type,health,damage)