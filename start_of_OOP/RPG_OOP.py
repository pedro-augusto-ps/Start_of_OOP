import time
class Player:
    def __init__(self, name, life, attack, gold, inventory):
        self.name = name   
        self.life = life
        self.attack = attack
        self.gold = gold
        self.inventory = inventory

    def __str__(self):
        life_text = f"Player:{player1.life}"
        monster_life_text = f"Monster: {monster1.life}"
        return life_text, monster_life_text
    
    def take_damage(self):
        return player1.life - monster1.attack
    
    def is_alive(self):
        if self.life >0:
            player_alive = True
        else:
            player_alive = False
        return player_alive

class Monster:
    def __init__(self, name, life, attack, gold):
       self.name = name   
       self.life = life
       self.attack = attack
       self.gold = gold   

    def take_damage(self):
        return player1.life - monster1.attack
    
    def is_alive(self):
        if self.life >0:
            monster_alive = True
        else:
            monster_alive = False
        return monster_alive
    
while Monster.is_alive(Monster) or Player.is_alive(Player):
    player1 = Player("Hero", 60, 10, 0)
    monster1 = Monster("Orc", 100, 5, 20)
    print("---PLAYER---")
    monster1.take_damage()
    print(f"Monster life: {monster1.life}")
    print("---MONSTER---")
    player1.take_damage
    print(f"Player life: {player1.life}")
    time.sleep(1)