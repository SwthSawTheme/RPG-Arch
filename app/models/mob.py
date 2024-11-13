from player import Player

class Mob(object):


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
