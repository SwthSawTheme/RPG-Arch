

class Player(object):


    def __init__(self,name:str,health:int,damage:int,arrows:int):
        self.name = name
        self.health = health
        self.damage = damage
        self.arrows = arrows

    def attack(self,mob):
        pass

    def collectArrows(self,qty:int):
        pass

    def takeDamage(self,value: int):
        pass

    def isAlive(self) -> bool:
        pass
