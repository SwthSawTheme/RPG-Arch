

class Player(object):


    def __init__(self,name:str,health=100,damage=10):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self,mob):
        print(f"{self.name} ataca {mob.type} causando {self.damage} de dano.")
        mob.takeDamage(self.damage)

    def takeDamage(self,value:int):
        self.health -= value

    def isAlive(self) -> bool:
        return self.health > 0
