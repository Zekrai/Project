from random import randint
import time


Player = {'name': 'insert_name',
          'lvl': 1,
          'xp': 0,
          'gold': 0,
          'next level': 20,
          'stats': {'vit': 30,
                    'max_vit': 30,
                    'mana': 15,
                    'str': 1,
                    'dex': 1,
                    'int': 1,
                    'atk': [3, 7]}}


slime = {'name': 'Slime',
         'lvl': 1,
         'xp_gain': 20,
         'gold_gain': 10,
         'loot': 0,
         'stats': {'vit': 12,
                   'max_vit': 12,
                   'str': 1,
                   'dex': 1,
                   'int': 1,
                   'atk': [1, 3]}}


lil_hap = {'name': 'Lil Hap',
           'lvl': 1,
           'xp_gain': 38,
           'gold_gain': 30,
           'loot': 0,
           'stats': {'vit': 22,
                     'max_vit': 22,
                     'str': 1,
                     'dex': 1,
                     'int': 1,
                     'atk': [3, 8]}}


solignis = {'name': 'Solignis',
            'lvl': 1,
            'xp_gain': 96,
            'gold_gain': 12,
            'loot': 0,
            'stats': {'vit': 40,
                      'max_vit': 40,
                      'str': 1,
                      'dex': 1,
                      'int': 1,
                      'atk': [5, 12]}}


def level(player):
    while Player['xp'] >= Player['next level']:
        Player['lvl'] += 1
        Player['xp'] = player['xp'] - Player['next level']
        Player['next level'] = round(Player['next level']*2.25)
        print('You gained a level!')
        print('You now reached level {}, your stats increase!'.format(player['lvl']))


# Damage in battle
def take_dmg(attacker, defender):
    dmg = randint(attacker['stats']['atk'][0], attacker['stats']['atk'][1])
    defender['stats']['vit'] = defender['stats']['vit'] - dmg
    print('{} takes {} damage!'.format(defender['name'], dmg))
    if defender['stats']['vit'] <= 0:
        print('{} has been slain!'.format(defender['name']))
        print('{} awarded you '.format(defender['name']) + '{}'.format(defender['xp_gain'])
              + ' experience and {} gold!'.format(defender['gold_gain']))
        Player['xp'] += defender['xp_gain']
        Player['gold'] += defender['gold_gain']
        level(Player)


def battle_launcher():
    print('+----------------------------+')
    print('Who do you wish to battle?\n')
    cmd = input('1: Slime | 2: Solignis | 3: Lil Hap\n '
                'X : Exit battle\n')


    if "1" in cmd:
        commands(Player, slime)
    if "2" in cmd:
        commands(Player, solignis)
    if "3" in cmd:
        commands(Player, lil_hap)
    if "X" in cmd:
        print("You leave the dungeon to rest!")
        time.sleep(2)
        exit()
    else:
        pass


# Battle initiator and action management
def commands(player, enemy):
    print('you encountered a wild {}'.format(enemy['name']))
    print('battle initiated!')
    while True:
        print('------------------------------------------------------------')
        cmd = input('What will you do?').lower()
        if "1" in cmd:       # Basic attack
            take_dmg(player, enemy)
        if "2" in cmd:       # Abilities
            abilities()
            break
        if "3" in cmd:       # Spells
            # add spells
            break
        if "4" in cmd:       # Items
            # add item usage & bag
            break
        if "5" in cmd:       # Flee
            print('you flee from the battle against {}!'.format(enemy['name']))
            battle_launcher()

        while enemy['stats']['vit'] <= 0:
            enemy['stats']['vit'] = enemy['stats']['max_vit']
            battle_launcher()

        while player['stats']['vit'] <= 0:
            print("You lost the battle! You get teleported back to the entrance of the dungeon ...")
            player['stats']['vit'] = player['stats']['max_vit']

            if cmd == "1" or "2" or "3" or "4":
                take_dmg(enemy, Player)
            else:
                pass


battle_launcher()

