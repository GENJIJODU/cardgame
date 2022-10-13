from errno import WSAEDQUOT
from cards import get_cards
import random
import os
from player_def import Player
from enemy_def import Enemy

player = Player("Player1", 15, 100)

enemy1 = Enemy("Grub", 50, {'damage':15})
enemy2 = Enemy("Boris", 150, {'damage':9})
enemies = {}
enemies[enemy1.name] = enemy1
enemies[enemy2.name] = enemy2

deck = []
all_cards = get_cards()
deck_size = 100
while deck_size:
    deck.append(all_cards[random.randint(0,len(all_cards)-1)].copy())
    deck_size -= 1
random.shuffle(deck)

def render(player, enemies, hand, turn):
    os.system("CLS")
    print(f"Turn: {turn}")
    print('Enemies:')
    for enemy in enemies.values():
        print(f"{enemy.name} - HP: {enemy.hp} - Intent: {enemy.attack} - Statuses: {enemy.statuses}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Player:")
    print(f"HP:{player.hp} - Deck:{len(deck)} - Armor: {player.armor} - STR: {player.str} - Energy:{player.resource_pool} - Hand:")
    for index, card in enumerate(hand):
        print(f"[{index}]: {card}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def draw(hand, deck, count):
    while count:
        if deck:
            topcard = deck.pop()
            hand.append(topcard)
        count -= 1

def get_valid_enemy(enemies):
    while True: 
                print('Target an Enemy: ')
                enemyname = input()
                if enemyname in enemies.keys():
                    return enemyname



################### COMBAT LOOOOOOP ###########################
turn = 1
hand = []
while True:
    # Draw for turn
    draw(hand, deck, 2)

    # Regain Resources
    player.resource_pool = min(15, player.resource_pool + 10)

    player_turn = True
    while player_turn:
        # Big time graphics
        render(player, enemies, hand, turn)

        # Choose valid card or pass
        while True:
            if hand:
                print(f'Play a card[0-{len(hand)-1}] or enter p to pass: ')
            else:
                print("You have no cards in hand. Enter 'p' to pass. ")
            selection = input()
            if selection == 'p':
                break
            if selection.isnumeric() and 0 <= int(selection) < len(hand):
                if hand[int(selection)]['cost'] > player.resource_pool:
                    print("you do not have enough resources to play that card!")
                else:
                    break

        # Pass turn
        if selection == 'p':
            break # PLAYER PASSES THE TURN

        # Grab card from hand
        selection = int(selection)
        card = hand.pop(selection)

        # Pay the mana
        player.resource_pool -= card['cost']

        # ATTACK
        if card['type'] == 'attack':
            # Validate target enemy
            enemyname = get_valid_enemy(enemies)
            # Damage Enemy
            enemy = enemies[enemyname]
            player.damage_enemy(enemy, card)
            # Check State
            if enemy.hp < 1:
                enemies.pop(enemy.name)

        #BUFF
        elif card['type'] == 'buff':
            player.resource_pool -= card['cost']
            #ARMOR
            for stat in card['effect'].keys():
                if stat == "armor":
                    player.armor += card['effect'][stat]
                elif stat == "str":
                    player.str += card['effect'][stat]
                elif stat == "dex":
                    player.dex += card['effect'][stat]
                elif stat == "int":
                    player.int += card['effect'][stat]

        #DRAW
        elif card['type'] == 'draw':
            draw(hand, deck, card['effect'])

        #DEBUFF
        elif card['type'] == 'debuff':
            #Target an Enemy
            enemy = enemies[get_valid_enemy(enemies)]
            #Increment all enemy statuses indicated ont he card
            for status in card['effect'].keys():
                if status in enemy.statuses.keys():
                    enemy.statuses[status] += card['effect'][status]
                else:
                    enemy.statuses[status] = card['effect'][status]

        # Check State
        if not enemies:
            print("you Win")
            quit()


    #Enemy Turn
    for enemy in enemies.values():
        enemy.attack_player(player)

        # Check State
        if player.hp < 1:
            print('you LOSE')
            quit()
        
    #Increment Turn Counter
    turn += 1
