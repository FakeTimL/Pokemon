from Pokemon import Pokemon
from Dummy import Dummy

inventory = [Pokemon("Aggron", 35, [15, 11, 12], ['Smack Down', 'Stone Edge']), 
             Pokemon("Flareon", 35, [9, 15, 6], ['Ember', 'Fire Blast']), 
             Pokemon("Gigalith", 28, [11, 15, 15], ['Mud Slap', 'Rock Slide']), 
             Pokemon("Jolteon", 34, [12, 10, 7], ['Volt Switch', 'Thunderbolt']), 
             Pokemon("Flareon", 31, [10, 8, 11], ['Ember', 'Overheat']), 
             Pokemon("Aggron", 30, [11, 10, 15], ['Iron Tail', 'Heavy Slam']), 
             Pokemon("Jolteon", 31, [14, 15, 14], ['Volt Switch', 'Thunderbolt']), 
             Pokemon("Staraptor", 34, [13, 12, 7], ['Quick Attack', 'Brave Bird']), 
             Pokemon("Kingler", 33, [10, 14, 14], ['Bubble', 'Crabhammer']), 
             Pokemon("Staraptor", 33, [10, 14, 14], ['Wing Attack', 'Close Combat']), 
             Pokemon("Flareon", 29, [15, 15, 10], ['Fire Spin', 'Overheat']), 
             Pokemon("Braviary", 30, [9, 4, 10], ['Steel Wing', 'Brave Bird']), 
             Pokemon("Aggron", 30, [13, 0, 14], ['Smack Down', 'Thunder']), 
             Pokemon("Vaporeon", 29, [10, 7, 15], ['Water Gun', 'Water Pulse']), 
             Pokemon("Blissey", 34, [11, 14, 14], ['Pound', 'Psychic']), 
             Pokemon("Muk", 32.5, [12, 15, 12], ['Infestation', 'Thunder Punch']), 
             Pokemon("Pyroar", 34, [8, 10, 13], ['Incinerate', 'Overheat']), 
             Pokemon("Sawk", 32, [14, 11, 8], ['Low Kick', 'Focus Blast']), 
             Pokemon("Vaporeon", 28, [15, 5, 7], ['Water Gun', 'Aqua Tail']), 
             Pokemon("Vaporeon", 28, [10, 12, 4], ['Water Gun', 'Water Pulse']), 
             Pokemon("Unfezant", 33, [8, 14, 11], ['Air Slash', 'Hyper Beam']), 
             Pokemon("Sawk", 34, [5, 5, 12], ['Poison Jab', 'Focus Blast']), 
             Pokemon("Incineroar", 28, [15, 14, 5], ['Fire Fang', 'Dark Pulse']), 
             Pokemon("Aggron", 28, [15, 5, 10], ['Iron Tail', 'Rock Tomb']), 
             Pokemon("Stoutland", 29, [14, 15, 13], ['Ice Fang', 'Wild Charge']), 
             Pokemon("Donphan", 28, [9, 14, 10], ['Tackle', 'Earthquake']), 
             Pokemon("Unfezant", 30, [14, 8, 14], ['Air Slash', 'Sky Attack']), 
             Pokemon("Gyarados", 25, [13, 1, 6], ['Waterfall', 'Outrage']), 
             Pokemon("Slowking", 34, [13, 13, 10], ['Confusion', 'Blizzard']), 
             Pokemon("Toucannon", 32, [8, 14, 8], ['Peck', 'Flash Cannon']), 
             Pokemon("Seismitoad", 33, [15, 8, 15], ['Mud Shot', 'Sludge Bomb']), 
             Pokemon("Decidueye", 29, [10, 15, 14], ['Razor Leaf', 'Brave Bird']), 
             Pokemon("Avalugg", 26, [5, 10, 14], ['Ice Fang', 'Mirror Coat']), 
             Pokemon("Jolteon", 28, [15, 13, 5], ['Volt Switch', 'Thunderbolt']), 
             Pokemon("Braviary", 26, [14, 7, 15], ['Steel Wing', 'Rock Slide']), 
             Pokemon("Snorlax", 25, [13, 6, 11], ['Lick', 'Return']), 
             Pokemon("Kingler", 28.5, [14, 14, 4], ['Bubble', 'Water Pulse']), 
             Pokemon("Granbull", 34, [5, 10, 15], ['Snarl', 'Crunch']), 
             Pokemon("Snorlax", 25, [12, 6, 6], ['Lick', 'Return']), 
             Pokemon("Blissey", 28, [15, 11, 12], ['Pound', 'Dazzling Gleam']), 
             Pokemon("Togekiss", 23, [13, 15, 14], ['Air Slash', 'Dazzling Gleam']), 
             Pokemon("Granbull", 32, [8, 12, 13], ['Charm', 'Crunch']), 
             Pokemon("Rapidash", 33, [14, 9, 13], ['Fire Spin', 'Heat Wave']), 
             Pokemon("Blissey", 27.5, [14, 15, 15], ['Pound', 'Hyper Beam']), 
             Pokemon("Poliwrath", 30, [15, 6, 12], ['Bubble', 'Ice Punch']), 
             Pokemon("Aggron", 25, [15, 12, 14], ['Iron Tail', 'Return']), 
             Pokemon("Jolteon", 27, [6, 10, 14], ['Thunder Shock', 'Thunderbolt']), 
             Pokemon("Hitmonlee", 30, [15, 7, 7], ['Rock Smash', 'Low Sweep']), 
             Pokemon("Drifblim", 34, [13, 9, 13], ['Astonish', 'Ominous Wind']), 
             Pokemon("Greninja", 29, [9, 6, 15], ['Feint Attack', 'Hydro Pump']), 
             Pokemon("Drifblim", 34, [15, 7, 6], ['Hex', 'Ominous Wind']), 
             Pokemon("Drifblim", 32, [15, 12, 11], ['Hex', 'Shadow Ball']), 
             Pokemon("Stoutland", 26, [11, 15, 14], ['Ice Fang', 'Wild Charge']), 
             Pokemon("Drifblim", 34, [12, 6, 13], ['Hex', 'Icy Wind']), 
             Pokemon("Masquerain", 35, [12, 13, 13], ['Infestation', 'Silver Wind']), 
             Pokemon("Slowbro", 29, [15, 7, 12], ['Confusion', 'Water Pulse']), 
             Pokemon("Drifblim", 31.5, [14, 13, 10], ['Astonish', 'Ominous Wind']), 
             Pokemon("Pyroar", 28, [5, 7, 7], ['Incinerate', 'Dark Pulse']), 
             Pokemon("Drifblim", 30, [15, 15, 11], ['Astonish', 'Shadow Ball']), 
             Pokemon("Crawdaunt", 30, [8, 11, 13], ['Snarl', 'Vise Grip']), 
             Pokemon("Toxicroak", 29, [12, 14, 12], ['Counter', 'Sludge Bomb']), 
             Pokemon("Golduck", 29, [13, 15, 13], ['Water Gun', 'Psychic']), 
             Pokemon("Exploud", 30, [15, 13, 9], ['Bite', 'Fire Blast']), 
             Pokemon("Hitmonlee", 27.5, [15, 14, 8], ['Rock Smash', 'Low Sweep']), 
             Pokemon("Solrock", 31, [10, 14, 15], ['Confusion', 'Solar Beam']), 
             Pokemon("Oricorio (Baile Style)", 30, [14, 13, 13], ['Pound', 'Hurricane']), 
             Pokemon("Mr. Mime", 33, [14, 14, 12], ['Zen Headbutt', 'Shadow Ball']), 
             Pokemon("Masquerain", 32, [15, 14, 8], ['Infestation', 'Ominous Wind']), 
             Pokemon("Staraptor", 25, [12, 15, 8], ['Wing Attack', 'Brave Bird']), 
             Pokemon("Rapidash", 30, [13, 3, 4], ['Low Kick', 'Drill Run']), 
             Pokemon("Crobat", 26, [14, 15, 12], ['Air Slash', 'Shadow Ball']), 
             Pokemon("Toxicroak", 29, [7, 5, 14], ['Poison Jab', 'Mud Bomb']),
             Pokemon("Mr. Mime", 32, [13, 6, 15], ['Confusion', 'Psybeam']), 
             Pokemon("Alolan Muk", 25, [13, 6, 15], ['Snarl', 'Return']), 
             Pokemon("Staraptor", 24, [15, 15, 6], ['Quick Attack', 'Heat Wave']), 
             Pokemon("Hitmonchan", 30, [7, 10, 14], ['Bullet Punch', 'Fire Punch']),
             Pokemon("Drifblim", 29, [7, 15, 14], ['Hex', 'Ominous Wind']),
             Pokemon("Masquerain", 30, [13, 12, 9], ['Air Slash', 'Air Cutter']), 
             Pokemon("Garbodor", 29, [12, 14, 7], ['Take Down', 'Gunk Shot']), 
             Pokemon("Archeops", 20, [12, 13, 12], ['Wing Attack', 'Ancient Power']), 
             Pokemon("Furfrou", 34, [10, 12, 14], ['Sucker Punch', 'Dark Pulse']), 
             Pokemon("Hitmontop", 35, [4, 14, 9], ['Counter', 'Gyro Ball']),
             Pokemon("Octillery", 28, [14, 15, 15], ['Water Gun', 'Aurora Beam']), 
             Pokemon("Togedemaru", 31.5, [14, 10, 11], ['Spark', 'Wild Charge']), 
             Pokemon("Electrode", 34, [13, 15, 4], ['Spark', 'Foul Play']), 
             Pokemon("Sawk", 24, [9, 13, 10], ['Poison Jab', 'Focus Blast']), 
             Pokemon("Sawsbuck", 28, [14, 6, 6], ['Feint Attack', 'Wild Charge']), 
             Pokemon("Aggron", 23, [4, 2, 15], ['Smack Down', 'Rock Tomb']),
             Pokemon("Tangela", 30, [6, 14, 14], ['Infestation', 'Solar Beam']), 
             Pokemon("Xatu", 30, [14, 7, 15], ['Air Slash', 'Aerial Ace']), 
             Pokemon("Snorlax", 20, [14, 12, 14], ['Zen Headbutt', 'Hyper Beam']), 
             Pokemon("Snorlax", 20, [15, 10, 14], ['Lick', 'Outrage']), 
             Pokemon("Hitmontop", 31, [12, 8, 12], ['Counter', 'Gyro Ball']), 
             Pokemon("Slowbro", 26, [12, 5, 12], ['Water Gun', 'Surf']), 
             Pokemon("Electrode", 32, [11, 11, 15], ['Spark', 'Foul Play']), 
             Pokemon("Snorlax", 20, [11, 15, 12], ['Zen Headbutt', 'Heavy Slam']), 
             Pokemon("Jolteon", 22, [13, 14, 14], ['Volt Switch', 'Discharge']), 
             Pokemon("Lanturn", 33, [8, 15, 13], ['Water Gun', 'Hydro Pump']), 
             Pokemon("Snorlax", 20, [13, 10, 10], ['Zen Headbutt', 'Earthquake']), 
             Pokemon("Snorlax", 20, [11, 12, 11], ['Zen Headbutt', 'Body Slam']), 
             Pokemon("Gyarados", 20, [0, 8, 13], ['Dragon Breath', 'Outrage']), 
             Pokemon("Stunfisk", 30, [10, 10, 14], ['Thunder Shock', 'Mud Bomb']), 
             Pokemon("Togedemaru", 30, [14, 5, 10], ['Thunder Shock', 'Wild Charge']), 
             Pokemon("Vaporeon", 20, [13, 15, 13], ['Water Gun', 'Aqua Tail']), 
             Pokemon("Qwilfish", 31, [14, 13, 13], ['Water Gun', 'Ice Beam']), 
             Pokemon("Solrock", 28, [7, 15, 8], ['Confusion', 'Rock Slide']), 
             Pokemon("Wigglytuff", 35, [14, 12, 11], ['Charm', 'Hyper Beam']),
             Pokemon("Kleavor", 20, [10, 13, 11], ['Air Slash', 'Stone Edge']),
             Pokemon("Duosion", 32, [15, 14, 6], ['Hidden Power (Steel)', 'Psyshock']), 
             Pokemon("Zangoose", 26, [13, 15, 5], ['Shadow Claw', 'Night Slash']), 
             Pokemon("Lanturn", 31, [9, 15, 9], ['Charge Beam', 'Hydro Pump']), 
             Pokemon("Tangrowth", 21, [4, 15, 15], ['Infestation', 'Sludge Bomb']), 
             Pokemon("Tangela", 28, [13, 4, 15], ['Vine Whip', 'Sludge Bomb']), 
             Pokemon("Bruxish", 26, [13, 8, 12], ['Bite', 'Aqua Tail']), 
             Pokemon("Fearow", 31, [15, 14, 9], ['Steel Wing', 'Sky Attack']), 
             Pokemon("Wigglytuff", 34, [9, 15, 12], ['Pound', 'Ice Beam']), 
             Pokemon("Sawk", 22, [15, 5, 13], ['Poison Jab', 'Body Slam']), 
             Pokemon("Lanturn", 29, [13, 12, 10], ['Water Gun', 'Surf']),
             Pokemon("Meloetta (Aria Forme)", 15, [14, 12, 11], ['Confusion', 'Hyper Beam']), 
             Pokemon("Solrock", 26, [13, 12, 7], ['Rock Throw', 'Rock Slide']), 
             Pokemon("Hitmonlee", 23, [14, 15, 11], ['Double Kick', 'Low Sweep']), 
             Pokemon("Mr. Mime", 27, [12, 15, 9], ['Confusion', 'Psychic']), 
             Pokemon("Sawk", 22, [15, 5, 4], ['Low Kick', 'Focus Blast']), 
             Pokemon("Brionne", 33, [14, 11, 12], ['Water Gun', 'Aqua Jet']), 
             Pokemon("Lopunny", 29, [13, 14, 8], ['Double Kick', 'Focus Blast']), 
             Pokemon("Zangoose", 25, [13, 13, 3], ['Shadow Claw', 'Night Slash']), 
             Pokemon("Sawk", 21, [10, 15, 15], ['Poison Jab', 'Focus Blast']), 
             Pokemon("Gengar", 21, [6, 11, 12], ['Shadow Claw', 'Focus Blast']), 
             Pokemon("Tapu Fini", 20, [14, 13, 15], ['Water Gun', 'Surf']), 
             Pokemon("Zangoose", 25, [14, 1, 11], ['Shadow Claw', 'Dig']), 
             Pokemon("Pelipper", 28, [10, 12, 9], ['Water Gun', 'Blizzard']), 
             Pokemon("Espeon", 18, [14, 11, 13], ['Confusion', 'Psychic Fangs']), 
             Pokemon("Fearow", 29, [15, 8, 11], ['Peck', 'Sky Attack']), 
             Pokemon("Aurorus", 20, [14, 13, 11], ['Rock Throw', 'Meteor Beam']), 
             Pokemon("Blissey", 20, [15, 14, 13], ['Zen Headbutt', 'Dazzling Gleam']), 
             Pokemon("Purugly", 29, [10, 14, 14], ['Shadow Claw', 'Play Rough']), 
             Pokemon("Hitmonchan", 23, [14, 12, 14], ['Bullet Punch', 'Close Combat']), 
             Pokemon("Dewott", 32, [14, 13, 11], ['Water Gun', 'Water Pulse']),

             Pokemon("Mega Beedrill", 21, [11, 14, 12], ['Infestation', 'Sludge Bomb'])]

sunshine = [Pokemon("Munchlax", 28, [12, 14, 14], ['Tackle', 'Body Slam']), 
            Pokemon("Galarian Stunfisk", 25, [11, 12, 13], ['Mud Shot', 'Earthquake', 'Rock Slide']), 
            Pokemon("Stoutland", 18.5, [14, 12, 15], ['Ice Fang', 'Wild Charge', 'Crunch']), 
            Pokemon("Donphan", 17.5, [15, 15, 12], ['Mud Slap', 'Earthquake']), 
            Pokemon("Lopunny", 26, [15, 12, 10], ['Low Kick', 'Fire Punch'])]

little = [Pokemon("Gible", 16, [15, 14, 10], ['Mud Shot', 'Body Slam']), 
            Pokemon("Shieldon", 20, [14, 14, 13], ['Tackle', 'Heavy Slam']), 
            Pokemon("Cottonee", 25.5, [13, 14, 15], ['Charm', 'Seed Bomb']), 
            Pokemon("Bidoof", 25, [12, 15, 15], ['Tackle', 'Crunch']), 
            Pokemon("Shellder", 16.5, [13, 15, 14], ['Ice Shard', 'Water Pulse']), 
            Pokemon("Meowth", 24.5, [10, 14, 15], ['Bite', 'Dark Pulse']), 
            Pokemon("Ponyta", 10.5, [13, 15, 9], ['Ember', 'Flame Wheel']), 
            Pokemon("Larvitar", 17, [14, 13, 13], ['Rock Smash', 'Crunch']), 
            Pokemon("Mankey", 15, [13, 14, 15], ['Karate Chop', 'Low Sweep']), 
            Pokemon("Torchic", 16.5, [11, 11, 14], ['Ember', 'Flamethrower']), 
            Pokemon("Snover", 15, [14, 12, 14], ['Powder Snow', 'Stomp'])]

def parse(pokemons):
    while True:
        print()
        try:
            pokemon = Dummy.parse(input())
            if input(pokemon):
                continue
            pokemons.append(pokemon)
        except:
            break
    print(', \n             '.join([repr(pokemon) for pokemon in pokemons]))
