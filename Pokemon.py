from Move import fast, main
from Species import species

class Pokemon:
    cpm = {
        1: 0.094, 1.5: 0.1351374318, 2: 0.16639787, 2.5: 0.192650919, 3: 0.21573247, 3.5: 0.2365726613, 4: 0.25572005, 4.5: 0.2735303812, 5: 0.29024988, 5.5: 0.3060573775, 6: 0.3210876, 6.5: 0.3354450362, 7: 0.34921268, 7.5: 0.3624577511, 8: 0.3752356, 8.5: 0.387592416, 9: 0.39956728, 9.5: 0.4111935514, 10: 0.4225, 10.5: 0.4329264091, 11: 0.44310755, 11.5: 0.4530599591, 12: 0.4627984, 12.5: 0.472336093, 13: 0.48168495, 13.5: 0.4908558003, 14: 0.49985844, 14.5: 0.508701765, 15: 0.51739395, 15.5: 0.5259425113, 16: 0.5343543, 16.5: 0.5426357375, 17: 0.5507927, 17.5: 0.5588305862, 18: 0.5667545, 18.5: 0.5745691333, 19: 0.5822789, 19.5: 0.5898879072, 20: 0.5974, 20.5: 0.6048236651, 21: 0.6121573, 21.5: 0.6194041216, 22: 0.6265671, 22.5: 0.6336491432, 23: 0.64065295, 23.5: 0.6475809666, 24: 0.65443563, 24.5: 0.6612192524, 25: 0.667934, 25.5: 0.6745818959, 26: 0.6811649, 26.5: 0.6876849038, 27: 0.69414365, 27.5: 0.70054287, 28: 0.7068842, 28.5: 0.7131691091, 29: 0.7193991, 29.5: 0.7255756136, 30: 0.7317, 30.5: 0.7347410093, 31: 0.7377695, 31.5: 0.7407855938, 32: 0.74378943, 32.5: 0.7467812109, 33: 0.74976104, 33.5: 0.7527290867, 34: 0.7556855, 34.5: 0.7586303683, 35: 0.76156384, 35.5: 0.7644860647, 36: 0.76739717, 36.5: 0.7702972656, 37: 0.7731865, 37.5: 0.7760649616, 38: 0.77893275, 38.5: 0.7817900548, 39: 0.784637, 39.5: 0.7874736075, 40: 0.7903, 40.5: 0.792803968, 41: 0.79530001, 41.5: 0.797800015, 42: 0.8003, 42.5: 0.802799995, 43: 0.8053, 43.5: 0.8078, 44: 0.81029999, 44.5: 0.812799985, 45: 0.81529999, 45.5: 0.81779999, 46: 0.82029999, 46.5: 0.82279999, 47: 0.82529999, 47.5: 0.82779999, 48: 0.83029999, 48.5: 0.83279999, 49: 0.83529999, 49.5: 0.83779999, 50: 0.84029999, 50.5: 0.84279999, 51: 0.84529999}
    
    def Parse(input):
        args = input.split()
        cp = int(args[0])
        title = lambda s: s.replace('-',' ').replace('_','-').title()
        name = title(args[1])
        ivs = [int(s) for s in args[-3:]]
        sp = species[name]
        level = calc_level(cp, sp.attack + ivs[0], sp.defense + ivs[1], sp.stamina + ivs[2])
        moves = [title(s) for s in args[2:-3]]

        pokemon = Pokemon(name, level, ivs, moves)
        if pokemon.cp != cp:
            print(f'CP mismatch: {pokemon.cp} != {cp}. Check IV inputs.')
        return pokemon
    
    def __init__(self, name, level, ivs, moves, types_override=None):
        self.name = name
        self.species = species[name]
        self.types = types_override if types_override else self.species.types
        self.level = level
        self.attack = self.species.attack + ivs[0]
        self.defense = self.species.defense + ivs[1]
        self.stamina = self.species.stamina + ivs[2]
        self.cp = int(self.attack * self.defense**0.5 * self.stamina**0.5 * Pokemon.cpm[self.level]**2 / 10)
        self.moves = [fast[moves[0]]] + [main[m] for m in moves[1:]]

    def __str__(self):
        moves = "\n".join([f'[{m.type.name}] {m.name}: ({m.damage})' for m in self.moves])
        return f'Lv.{self.level} {self.name} (CP {self.cp}) {"/".join([t.name for t in self.species.types])}\n{moves}'
        
    def __repr__(self):
        return f'Pokemon("{self.name}", {self.level}, [{self.attack - self.species.attack}, {self.defense - self.species.defense}, {self.stamina - self.species.stamina}], {[m.name for m in self.moves]}{f", {self.types}" if self.types != self.species.types  else ""})'
    
    # def attack(self, enemy):
    #     res = []
    #     for move in [self.fast, self.charge, self.charge_2]:
    #         if move:
    #             multiplier = chart[move][enemy.type] # Type effectiveness
    #             if move in [self.type, self.type_2]:
    #                 multiplier *= 1.2 # STAB
    #             if enemy.type_2:
    #                 multiplier *= chart[move][enemy.type_2] # Dual type effectiveness
    #             res.append(multiplier)
    #     return res

    # def combat(self, enemy):
    #     return self.attack(enemy), enemy.attack(self)

    # def print_combat(self, enemy):
    #     pc = lambda x: f'{x:.0%}'
    #     attack, defense = self.combat(enemy)
    #     print(f'{self.name} vs {enemy.name}\n')
    #     print(f'Fast({self.fast}): {pc(attack[0])}')
    #     print(f'Charge({self.charge}): {pc(attack[1])}')
    #     if self.charge_2:
    #         print(f'Charge({self.charge_2}): {pc(attack[2])}')
    #     print(f'\nFast({enemy.fast}): {pc(defense[0])}')
    #     print(f'Charge({enemy.charge}): {pc(defense[1])}')
    #     if enemy.charge_2:
    #         print(f'Charge({enemy.charge_2}): {pc(defense[2])}')

def calc_level(cp, attack, defense, stamina):
    cpm = (10 * (cp / (attack * defense**0.5 * stamina**0.5)))**0.5
    return min(Pokemon.cpm.items(), key=lambda x: abs(x[1] - cpm))[0]



# class Dummy(Pokemon):
#     def __init__(self, name, level, ivs, moves, types_override=None):
#         super().__init__(name, level, ivs, moves, types_override)
#         self.attack = self.defense = self.stamina = 0
#         self.cp = 0

# def stats(pokemon, enemy):
#     attack, defense = pokemon.combat(enemy)
#     max_attack = max(attack[1:])
#     min_defense = 1/max(defense)
#     total_score = attack[0] * max_attack * min_defense
#     attack_score = attack[0] * max_attack
#     return total_score, attack_score, attack[0], min_defense, pokemon.cp

# def compare(pokemons, enemy, show=5):
#     arr = list(zip(pokemons, map(lambda p: stats(p, enemy), pokemons)))
#     arr.sort(key=lambda x: x[1], reverse=True)
#     pc = lambda x: f'{x:.0%}'
#     print()
#     for i in range(min(show, len(pokemons))):
#         print(i+1, arr[i][0])
#         print(pc(arr[i][1][2]), pc(arr[i][1][1]/arr[i][1][2]), pc(arr[i][1][3]))
#     print()