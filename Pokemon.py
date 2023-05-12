from Move import fast, main
from Species import species

class Pokemon:
    cpm = {
        1: 0.094, 1.5: 0.1351374318, 2: 0.16639787, 2.5: 0.192650919, 3: 0.21573247, 3.5: 0.2365726613, 4: 0.25572005, 4.5: 0.2735303812, 5: 0.29024988, 5.5: 0.3060573775, 6: 0.3210876, 6.5: 0.3354450362, 7: 0.34921268, 7.5: 0.3624577511, 8: 0.3752356, 8.5: 0.387592416, 9: 0.39956728, 9.5: 0.4111935514, 10: 0.4225, 10.5: 0.4329264091, 11: 0.44310755, 11.5: 0.4530599591, 12: 0.4627984, 12.5: 0.472336093, 13: 0.48168495, 13.5: 0.4908558003, 14: 0.49985844, 14.5: 0.508701765, 15: 0.51739395, 15.5: 0.5259425113, 16: 0.5343543, 16.5: 0.5426357375, 17: 0.5507927, 17.5: 0.5588305862, 18: 0.5667545, 18.5: 0.5745691333, 19: 0.5822789, 19.5: 0.5898879072, 20: 0.5974, 20.5: 0.6048236651, 21: 0.6121573, 21.5: 0.6194041216, 22: 0.6265671, 22.5: 0.6336491432, 23: 0.64065295, 23.5: 0.6475809666, 24: 0.65443563, 24.5: 0.6612192524, 25: 0.667934, 25.5: 0.6745818959, 26: 0.6811649, 26.5: 0.6876849038, 27: 0.69414365, 27.5: 0.70054287, 28: 0.7068842, 28.5: 0.7131691091, 29: 0.7193991, 29.5: 0.7255756136, 30: 0.7317, 30.5: 0.7347410093, 31: 0.7377695, 31.5: 0.7407855938, 32: 0.74378943, 32.5: 0.7467812109, 33: 0.74976104, 33.5: 0.7527290867, 34: 0.7556855, 34.5: 0.7586303683, 35: 0.76156384, 35.5: 0.7644860647, 36: 0.76739717, 36.5: 0.7702972656, 37: 0.7731865, 37.5: 0.7760649616, 38: 0.77893275, 38.5: 0.7817900548, 39: 0.784637, 39.5: 0.7874736075, 40: 0.7903, 40.5: 0.792803968, 41: 0.79530001, 41.5: 0.797800015, 42: 0.8003, 42.5: 0.802799995, 43: 0.8053, 43.5: 0.8078, 44: 0.81029999, 44.5: 0.812799985, 45: 0.81529999, 45.5: 0.81779999, 46: 0.82029999, 46.5: 0.82279999, 47: 0.82529999, 47.5: 0.82779999, 48: 0.83029999, 48.5: 0.83279999, 49: 0.83529999, 49.5: 0.83779999, 50: 0.84029999, 50.5: 0.84279999, 51: 0.84529999}
    
    def __init__(self, name, level, ivs, moves, shadow=False):
        self.name = name
        self.species = species[name]
        self.level = level
        self.attack = self.species.attack + ivs[0]
        self.defense = self.species.defense + ivs[1]
        self.stamina = self.species.stamina + ivs[2]
        self.cp = int(self.attack * self.defense**0.5 * self.stamina**0.5 * Pokemon.cpm[self.level]**2 / 10)
        self.moves = [fast[moves[0]]] + [main[m] for m in moves[1:]]
        self.shadow = shadow

    def short(self):
        return f'{self.name} (CP {self.cp})'

    def __str__(self):
        moves = "\n".join([f'[{m.type.name}] {m.name}: ({m.power})' for m in self.moves])
        return f'Lv.{self.level} {self.name} (CP {self.cp}) {"/".join([t.name for t in self.species.types])}\n{moves}'
        
    def __repr__(self):
        return f'Pokemon("{self.name}", {self.level}, [{self.attack - self.species.attack}, {self.defense - self.species.defense}, {self.stamina - self.species.stamina}], {[m.name for m in self.moves]})'

    # def damage_mod(self, enemy, pvp=1, weather=None, friendship=1):
    #     te = lambda m: m.type.against(*enemy.species.types)
    #     stab = lambda m: 1.2 if m.type in self.species.types else 1
    #     wab = lambda m: 1.2 if not pvp and m.type in weather else 1 # Weather boost does not apply in PvP
    #     shadow = (1.2 if self.shadow else 1) * (1.2 if enemy.shadow else 1)
    #     fsb = friendship if not pvp else 1 # Friendship does not apply in PvP
    #     return lambda m: te(m) * stab(m) * wab(m) * shadow * fsb

    # def damage_against(self, enemy, pvp=1, weather=None, friendship=1):
    #     attack = self.attack * Pokemon.cpm[self.level]
    #     defense = enemy.defense * Pokemon.cpm[enemy.level]
    #     mod = self.damage_mod(enemy, pvp, weather, friendship)
    #     return [int((16*m.power[pvp]*attack/defense*mod(m))//25)+1 for m in self.moves]

    # def fast_dps_against(self, enemy, pvp=1, weather=None, friendship=1):
    #     return self.damage_against(enemy, pvp, weather, friendship)[0] / self.moves[0].duration[pvp]

    # def charge_count(self, pvp=1, cycle=False):
    #     rate = lambda m: -m.energy[pvp] / self.moves[0].energy[pvp]
    #     count = lambda m: -(m.energy[pvp] // self.moves[0].energy[pvp])
    #     return [rate(m) if cycle else count(m) for m in self.moves[1:]]

    # def charge_duration(self, pvp=1, cycle=False):
    #     return [c * self.moves[0].duration[pvp] for c in self.charge_count(pvp, cycle)]

    # Only count the first cycle: cycle = False
    # def cycle_dps_against(self, enemy, pvp=1, weather=None, friendship=1):
    #     damage = self.damage_against(enemy, pvp, weather, friendship)
    #     return [(cnt * damage[0] + dmg) / dur for cnt, dur, dmg in zip(self.charge_count(pvp), self.charge_duration(pvp), damage[1:])]

    # def print_combat(self, enemy, pvp=1, weather=None, friendship=1):
    #     print(self.short())

    #     mod = self.damage_mod(enemy, pvp, weather, friendship)
    #     damage = self.damage_against(enemy, pvp, weather, friendship)
    #     fast_dps = self.fast_dps_against(enemy, pvp, weather, friendship)
    #     print(f'{self.moves[0]}: {damage[0]}/ATK ({fast_dps:.2f} DPS) {100*mod(self.moves[0]):.0f}%')

    #     count = self.charge_count(pvp, cycle=True)
    #     duration = self.charge_duration(pvp)
    #     cycle_dps = self.cycle_dps_against(enemy, pvp, weather, friendship)
    #     for i in range(len(self.moves)-1):
    #         print(f'{self.moves[i+1]}: {damage[i+1]}/ATK ({cycle_dps[i]:.1f} DPS) in {duration[i]:.1f}s ({count[i]:.1f}x) {100*mod(self.moves[i+1]):.0f}%')
