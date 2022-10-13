def get_cards():
    cards = []

    #Deal Damage
    card1 = {}
    card1['name'] = "Sword"
    card1['type'] = "attack"
    card1['cost'] = 2
    card1['effect'] = {'damage':10}
    cards.append(card1)

    #Buff Skill
    card2 = {}
    card2['name'] = "Armor Up!"
    card2['type'] = "buff"
    card2['cost'] = 5
    card2['effect'] = {'armor':1}
    cards.append(card2)

    #Draw
    card3 = {}
    card3['name'] = "Ponder"
    card3['type'] = "draw"
    card3['cost'] = 1
    card3['effect'] = 3
    cards.append(card3)

    #Debuff Enemy
    card4 = {}
    card4['name'] = "Enfeeble"
    card4['type'] = "debuff"
    card4['cost'] = 1
    card4['effect'] = {'weak':3}
    cards.append(card4)

    #Debuff Enemy
    card5 = {}
    card5['name'] = "Flex"
    card5['type'] = "buff"
    card5['cost'] = 1
    card5['effect'] = {'str':2}
    cards.append(card5)
    return cards
