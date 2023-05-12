from enum import Enum
from Type import Type

class Weather(Enum):
    SUNNY = {Type.GRASS, Type.FIRE, Type.GROUND}
    RAINY = {Type.WATER, Type.ELECTRIC, Type.BUG}
    PARTLY_CLOUDY = {Type.NORMAL, Type.ROCK}
    CLOUDY = {Type.FAIRY, Type.FIGHTING, Type.POISON}
    WINDY = {Type.DRAGON, Type.FLYING, Type.PSYCHIC}
    SNOW = {Type.ICE, Type.STEEL}
    FOG = {Type.GHOST, Type.DARK}
    NULL = {}
    