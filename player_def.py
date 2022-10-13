class Player:
  def __init__(self, name, resource_pool, hp):
    self.name = name
    self.resource_pool = resource_pool
    self.hp = hp
    self.max_hp = hp
    self.str = 0
    self.dex = 0
    self.int = 0
    self.armor = 3

  def deal_damage(self, damage): 
    self.hp -= max(0,(damage - self.armor))

  def damage_enemy(self, enemy, card):
    total_damage = card['effect']['damage'] + self.str
    enemy.takes_damage(total_damage)
