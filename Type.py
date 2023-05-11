from enum import Enum

class Type(Enum):
    NORMAL = 'N'
    FIRE = 'F'
    WATER = 'W'
    ELECTRIC = 'E'
    GRASS = 'G'
    ICE = 'I'
    FIGHTING = 'T'
    POISON = 'P'
    GROUND = 'U'
    FLYING = 'L'
    PSYCHIC = 'S'
    BUG = 'B'
    ROCK = 'R'
    GHOST = 'H'
    DRAGON = 'D'
    DARK = 'K'
    STEEL = 'M'
    FAIRY = 'Y'

    def against(self, other, other2=None):
        return chart[self.name][other.name] * (chart[self.name][other2.name] if other2 else 1)
    
    def __repr__(self):
        return f'Type.{self.name}'

chart = {'NORMAL': {'NORMAL': 1, 'FIRE': 1, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1, 'ICE': 1, 'FIGHTING': 1, 'POISON': 1, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 1, 'BUG': 1, 'ROCK': 0.625, 'GHOST': 0.390625, 'DRAGON': 1, 'DARK': 1, 'STEEL': 0.625, 'FAIRY': 1},
        'FIRE': {'NORMAL': 1, 'FIRE': 0.625, 'WATER': 0.625, 'ELECTRIC': 1, 'GRASS': 1.6, 'ICE': 1.6, 'FIGHTING': 1, 'POISON': 1, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 1, 'BUG': 1.6, 'ROCK': 0.625, 'GHOST': 1, 'DRAGON': 0.625, 'DARK': 1, 'STEEL': 1.6, 'FAIRY': 1},
        'WATER': {'NORMAL': 1, 'FIRE': 1.6, 'WATER': 0.625, 'ELECTRIC': 1, 'GRASS': 0.625, 'ICE': 1, 'FIGHTING': 1, 'POISON': 1, 'GROUND': 1.6, 'FLYING': 1, 'PSYCHIC': 1, 'BUG': 1, 'ROCK': 1.6, 'GHOST': 1, 'DRAGON': 0.625, 'DARK': 1, 'STEEL': 1, 'FAIRY': 1},
        'ELECTRIC': {'NORMAL': 1, 'FIRE': 1, 'WATER': 1.6, 'ELECTRIC': 0.625, 'GRASS': 0.625, 'ICE': 1, 'FIGHTING': 1, 'POISON': 1, 'GROUND': 0.390625, 'FLYING': 1.6, 'PSYCHIC': 1, 'BUG': 1, 'ROCK': 1, 'GHOST': 1, 'DRAGON': 0.625, 'DARK': 1, 'STEEL': 1, 'FAIRY': 1},
        'GRASS': {'NORMAL': 1, 'FIRE': 0.625, 'WATER': 1.6, 'ELECTRIC': 1, 'GRASS': 0.625, 'ICE': 1, 'FIGHTING': 1, 'POISON': 0.625, 'GROUND': 1.6, 'FLYING': 0.625, 'PSYCHIC': 1, 'BUG': 0.625, 'ROCK': 1.6, 'GHOST': 1, 'DRAGON': 0.625, 'DARK': 1, 'STEEL': 0.625, 'FAIRY': 1},
        'ICE': {'NORMAL': 1, 'FIRE': 0.625, 'WATER': 0.625, 'ELECTRIC': 1, 'GRASS': 1.6, 'ICE': 0.625, 'FIGHTING': 1, 'POISON': 1, 'GROUND': 1.6, 'FLYING': 1.6, 'PSYCHIC': 1, 'BUG': 1, 'ROCK': 1, 'GHOST': 1, 'DRAGON': 1.6, 'DARK': 1, 'STEEL': 0.625, 'FAIRY': 1},
        'FIGHTING': {'NORMAL': 1.6, 'FIRE': 1, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1, 'ICE': 1.6, 'FIGHTING': 1, 'POISON': 0.625, 'GROUND': 1, 'FLYING': 0.625, 'PSYCHIC': 0.625, 'BUG': 0.625, 'ROCK': 1.6, 'GHOST': 0.390625, 'DRAGON': 1, 'DARK': 1.6, 'STEEL': 1.6, 'FAIRY': 0.625},
        'POISON': {'NORMAL': 1, 'FIRE': 1, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1.6, 'ICE': 1, 'FIGHTING': 1, 'POISON': 0.625, 'GROUND': 0.625, 'FLYING': 1, 'PSYCHIC': 1, 'BUG': 1, 'ROCK': 0.625, 'GHOST': 0.625, 'DRAGON': 1, 'DARK': 1, 'STEEL': 0.390625, 'FAIRY': 1.6},
        'GROUND': {'NORMAL': 1, 'FIRE': 1.6, 'WATER': 1, 'ELECTRIC': 1.6, 'GRASS': 0.625, 'ICE': 1, 'FIGHTING': 1, 'POISON': 1.6, 'GROUND': 1, 'FLYING': 0.390625, 'PSYCHIC': 1, 'BUG': 0.625, 'ROCK': 1.6, 'GHOST': 1, 'DRAGON': 1, 'DARK': 1, 'STEEL': 1.6, 'FAIRY': 1},
        'FLYING': {'NORMAL': 1, 'FIRE': 1, 'WATER': 1, 'ELECTRIC': 0.625, 'GRASS': 1.6, 'ICE': 1, 'FIGHTING': 1.6, 'POISON': 1, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 1, 'BUG': 1.6, 'ROCK': 0.625, 'GHOST': 1, 'DRAGON': 1, 'DARK': 1, 'STEEL': 0.625, 'FAIRY': 1},
        'PSYCHIC': {'NORMAL': 1, 'FIRE': 1, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1, 'ICE': 1, 'FIGHTING': 1.6, 'POISON': 1.6, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 0.625, 'BUG': 1, 'ROCK': 1, 'GHOST': 1, 'DRAGON': 1, 'DARK': 0.390625, 'STEEL': 0.625, 'FAIRY': 1},
        'BUG': {'NORMAL': 1, 'FIRE': 0.625, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1.6, 'ICE': 1, 'FIGHTING': 0.625, 'POISON': 0.625, 'GROUND': 1, 'FLYING': 0.625, 'PSYCHIC': 1.6, 'BUG': 1, 'ROCK': 1, 'GHOST': 0.625, 'DRAGON': 1, 'DARK': 1.6, 'STEEL': 0.625, 'FAIRY': 0.625},
        'ROCK': {'NORMAL': 1, 'FIRE': 1.6, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1, 'ICE': 1.6, 'FIGHTING': 0.625, 'POISON': 1, 'GROUND': 0.625, 'FLYING': 1.6, 'PSYCHIC': 1, 'BUG': 1.6, 'ROCK': 1, 'GHOST': 1, 'DRAGON': 1, 'DARK': 1, 'STEEL': 0.625, 'FAIRY': 1},
        'GHOST': {'NORMAL': 0.390625, 'FIRE': 1, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1, 'ICE': 1, 'FIGHTING': 1, 'POISON': 1, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 1.6, 'BUG': 1, 'ROCK': 1, 'GHOST': 1.6, 'DRAGON': 1, 'DARK': 0.625, 'STEEL': 1, 'FAIRY': 1},
        'DRAGON': {'NORMAL': 1, 'FIRE': 1, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1, 'ICE': 1, 'FIGHTING': 1, 'POISON': 1, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 1, 'BUG': 1, 'ROCK': 1, 'GHOST': 1, 'DRAGON': 1.6, 'DARK': 1, 'STEEL': 0.625, 'FAIRY': 0.390625},
        'DARK': {'NORMAL': 1, 'FIRE': 1, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1, 'ICE': 1, 'FIGHTING': 0.625, 'POISON': 1, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 1.6, 'BUG': 1, 'ROCK': 1, 'GHOST': 1.6, 'DRAGON': 1, 'DARK': 0.625, 'STEEL': 1, 'FAIRY': 0.625},
        'STEEL': {'NORMAL': 1, 'FIRE': 0.625, 'WATER': 0.625, 'ELECTRIC': 0.625, 'GRASS': 1, 'ICE': 1.6, 'FIGHTING': 1, 'POISON': 1, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 1, 'BUG': 1, 'ROCK': 1.6, 'GHOST': 1, 'DRAGON': 1, 'DARK': 1, 'STEEL': 0.625, 'FAIRY': 1.6},
        'FAIRY': {'NORMAL': 1, 'FIRE': 0.625, 'WATER': 1, 'ELECTRIC': 1, 'GRASS': 1, 'ICE': 1, 'FIGHTING': 1.6, 'POISON': 0.625, 'GROUND': 1, 'FLYING': 1, 'PSYCHIC': 1, 'BUG': 1, 'ROCK': 1, 'GHOST': 1, 'DRAGON': 1.6, 'DARK': 1.6, 'STEEL': 0.625, 'FAIRY': 1}}
