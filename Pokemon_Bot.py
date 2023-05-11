from os import system
from Type import Type
from argparse import ArgumentParser

def attack(enemy):
    attack_with = []
    avoid_attacking_with = []
    for attacker in Type:
        if attacker.against(enemy) < 1:
            avoid_attacking_with.append(attacker)
        elif attacker.against(enemy) > 1:
            attack_with.append(attacker)
    return attack_with, avoid_attacking_with

def defense(enemy):
    defend_as = []
    avoid_defending_as = []
    for defender in Type:
        if enemy.against(defender) < 1:
            defend_as.append(defender)
        elif enemy.against(defender) > 1:
            avoid_defending_as.append(defender)
    return defend_as, avoid_defending_as

parser = ArgumentParser()
parser.add_argument("enemy", nargs="+", help="enemy types")
parser.add_argument("-t", "--type", nargs='?', help="enemy attack type")
parser.add_argument("-s", "--show", action="store_true", help="show type stats")
parser.add_argument("-a", "--attack", action="store_true", help="consider attackers with super effective attacks")
parser.add_argument("-f", "--fight", action="store_true", help="consider only attackers with both super effective attacks")
parser.add_argument("-p", "--protect", action="store_true", help="avoid attackers with bad defensive typing")
parser.add_argument("-d", "--defend", action="store_true", help="consider attackers with good defensive typing")
parser.add_argument("-c", "--copy", action="store_true", help="copy the search key to the clipboard")
args = parser.parse_args()

# We only consider one type for now
enemy_type = Type[args.enemy[0].upper()]
enemy_attack_type = Type[args.type.upper()] if args.type else enemy_type

aw, aaw = attack(enemy_type)
da, ada = defense(enemy_attack_type)
key = ''

print(f'\nEnemy type: {enemy_type.name}')
if args.type:
    print(f'Enemy attack type: {enemy_attack_type.name}')
if args.show:
    print(f'\nAttack with: {"/".join([t.name for t in aw])}')
    print(f'Defend as: {"/".join([t.name for t in da])}')
    print(f'Avoid attacking with: {"/".join([t.name for t in aaw])}')
    print(f'Avoid defending as: {"/".join([t.name for t in ada])}')

if args.fight:
    key = f"{';'.join([f'@1{t.name}' for t in aw])}&{';'.join([f'@2{t.name}' for t in aw])}"
elif args.attack:
    key = f"{';'.join([f'@{t.name}' for t in aw])}&{'&'.join([f'!@{t.name}' for t in aaw])}"
else:
    key = f"{'&'.join([f'!@{t.name}' for t in aaw])}"

if args.defend:
    key = f"{key}&{';'.join([f'{t.name}' for t in da])}&{'&'.join([f'!{t.name}' for t in ada])}"
elif args.protect:
    key = f"{key}&{'&'.join([f'!{t.name}' for t in ada])}"

if args.copy:
    system(f'echo "{key}" | pbcopy')
print(f'\nSearch keyword:\n{key}\n')
