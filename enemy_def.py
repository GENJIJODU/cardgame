class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.statuses = {}

    def attack_player(self, player):
        player.deal_damage(self.attack['damage'])

    def takes_damage(self, damage): 
        if 'weak' in self.statuses.keys():
            damage += self.statuses['weak']
        self.hp -= damage