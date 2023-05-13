from Pokemon import Pokemon
from Weather import Weather

class Context():
    def __init__(self, pvp=True, weather=[], friendship=1):
        self.mode = 1 if pvp else 0
        self.weather = weather if not pvp else [] # Weather does not apply in PvP
        self.friendship = friendship if not pvp else 1 # Friendship does not apply in PvP
    
    def damage_mod(self, attacker, defender):
        te = lambda m: m.type.against(*defender.species.types)
        stab = lambda m: 1.2 if m.type in attacker.species.types else 1
        wab = lambda m: 1.2 if m.type in self.weather else 1
        shadow = (1.2 if attacker.shadow else 1) * (1.2 if defender.shadow else 1)
        fsb = self.friendship
        return lambda m: te(m) * stab(m) * wab(m) * shadow * fsb

    def damage(self, attacker, defender):
        attack = attacker.attack * Pokemon.cpm[attacker.level]
        defense = defender.defense * Pokemon.cpm[defender.level]
        mod = self.damage_mod(attacker, defender)
        return lambda m: int((16*m.power[self.mode]*attack/defense*mod(m))//25)+1
    
    def fast_dps(self, attacker, defender):
        fast = attacker.moves[0]
        return self.damage(attacker, defender)(fast) / fast.duration[self.mode]
    
    # Only count the first cycle: cycle = False
    def cycle_dps(self, attacker, defender):
        fast = attacker.moves[0]
        cnt = lambda m: m.charge_count(fast, self.mode)
        dur = lambda m: m.charge_duration(fast, self.mode)
        dmg = self.damage(attacker, defender)
        return lambda m: (cnt(m) * dmg(fast) + dmg(m)) / dur(m)
    
    def combat(self, attacker, defender):
        print(attacker.short())

        mod = self.damage_mod(attacker, defender)
        dmg = self.damage(attacker, defender)
        fdps = self.fast_dps(attacker, defender)
        fast = attacker.moves[0]
        print(f'{fast}: {dmg(fast)}/ATK ({fdps:.1f} DPS) {100*mod(fast):.0f}%')

        cnt = lambda m: m.charge_count(fast, self.mode, cycle=True)
        dur = lambda m: m.charge_duration(fast, self.mode)
        cdps = self.cycle_dps(attacker, defender)
        for m in attacker.moves[1:]:
            print(f'{m}: {dmg(m)}/ATK ({cdps(m):.1f} DPS) in {dur(m):.1f}s ({cnt(m):.1f}x) {100*mod(m):.0f}%')
