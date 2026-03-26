# Braden Adams

bulbasaur = Pokemon("Bulbasaur", "Grass", 60)

charmander = Pokemon("Charmander", "Fire", 55)

squirtle = Pokemon("Squirtle", "Water", 65)

charmander.get_info()

charmander.heal()

lstPokemon = [bulbasaur, charmander, squirtle]

for pokemon in lstPokemon:
    pokemon.get_info()