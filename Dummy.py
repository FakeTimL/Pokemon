from Pokemon import Pokemon
from Species import species

class Dummy:
    @staticmethod
    def parse(str):
        args = str.split()
        cp = int(args[0])
        title = lambda s: s.replace('-',' ').replace('_','-').title()
        name = title(args[1])
        ivs = [int(s) for s in args[-3:]]
        sp = species[name]
        level = Dummy.pred_level(cp, sp.attack + ivs[0], sp.defense + ivs[1], sp.stamina + ivs[2])
        moves = [title(s) for s in args[2:-3]]

        pokemon = Pokemon(name, level, ivs, moves)
        if pokemon.cp != cp:
            print(f'CP mismatch: {pokemon.cp} != {cp}. Check IV inputs.')
        return pokemon

    @staticmethod
    def pred_level(cp, attack, defense, stamina):
        cpm = (10 * (cp / (attack * defense**0.5 * stamina**0.5)))**0.5
        return min(Pokemon.cpm.items(), key=lambda x: abs(x[1] - cpm))[0]
    
    @staticmethod
    def model(name, level=50, ivs=[15, 15, 15], moves=['Tackle', 'Struggle']):
        return Pokemon(name, level, ivs, moves)

    @staticmethod
    def dummy(name=None, level=None, ivs=None, moves=None):
        pass
