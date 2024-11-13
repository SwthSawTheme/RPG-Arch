from src.characters.player import Player


class Archery(Player):


    def __init__(self,name,arrows=10):
        super().__init__(name,health=80,damage=10)
        self.arrows = arrows

    def attack(self, mob):
        if self.arrows > 0:
            super().attack(mob)
            self.arrows -= 1
            print(f"{self.name} usou uma flecha! Flechas restantes: {self.arrows}")
        else:
            print(f"{self.name} está sem flechas! Não pode atacar.")

    def getArrows(self,qtd):
        self.arrows += qtd
        print(f"{self.name} pegou {qtd} flechas. Flechas totais: {self.arrows}")