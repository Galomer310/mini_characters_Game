
class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack
    def basic_attack(self, other_character):
        pass

class Druid(Character):
    def meditate(self):
        self.life += 10
        self.attack -= 2
        return f"your life is now {self.life} but your attack is {self.attack}"
    def animal_help(self):
        self.attack += 5
        return f"your attack is now {self.attack}"
    def fight(self, other_character):
        other_character.life -= (other_character.life * 0.75 + other_character.attack * 0.75)
        return f" {other_character.name} now have {other_character.life} life"

class Worrior(Character):
    def brawl(self, other_character):
        other_character.life -= other_character.attack * 2
        other_character.attack += 0.5 * other_character.attack
        return f"{other_character.name} have {other_character.life} life and {other_character.attack} attack"
    def train(self):
        self.attack += 2
        self.life += 2
        return f" your life and attack now are {self.life} life , {self.attack} attack"
    def roar(self, other_character):
        other_character.attack -= 3
        return f"{other_character.name} now have {other_character.attack} attack"


class Mage(Character):
    def curse(self, other_character):
        other_character.attack -= 2
        return f"{other_character.name} attack was reduce to {other_character.attack}"
    def summon(self):
        self.attack += 3
        return f"{self.name} attack is now {self.attack}"
    def cast_spell(self, other_character):
        other_character.life -= other_character.attack / other_character.life
        return f"you subtracts your aponent life to {other_character.life} "

player1 = Druid('Gal')
player2 = Worrior('Angelica')
player3 = Mage('orli')

print(player1.meditate())
print(player1.animal_help())
print(player1.fight(player2))

print(player2.brawl(player1))
print(player2.train())
print(player2.roar(player3))

print(player3.curse(player1))
print(player3.summon())
print(player3.cast_spell(player2))