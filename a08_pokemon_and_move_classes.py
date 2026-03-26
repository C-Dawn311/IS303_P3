# Authors: Courtney Bingham, Anna Pettit, Braden Adams, Ethan Lawson

import random

# Classes

class Move:
    # Constructor - takes move name, elemental type, and attack point range
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points
    # prints all info out
    def get_info(self):
        return(f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points")
    # randomly generates number between low and high attack points
    def generate_attack_value(self):
        attack = random.randint(self.low_attack_points,self.high_attack_points)
        return attack


class Pokemon:
    # Constructor - takes name, elemental type, and starting hit points
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points
    # prints out info
    def get_info(self):
        return(f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}")
    # increases hit_poitns by 15 and prints out new messsage
    def heal(self):
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")

lstMoves = []
# Create 9 Move objects with name, elemental type, and attack point range
Move1 = Move("Tackle", "Normal", 5, 20)
Move2 = Move("Quick Attack", "Normal", 6, 25)
Move3 = Move("Slash", "Normal", 10, 30)
Move4 = Move("Flamethrower", "Fire", 5, 30)
Move5 = Move("Ember", "Fire", 10, 20)
Move6 = Move("Water Gun", "Water", 5, 15)
Move7 = Move("Hydro Pump", "Water", 20, 25)
Move8 = Move("Vine Whip", "Grass", 10, 25)
Move9 = Move("Solar Beam", "Grass", 18, 27)

lstMoves.append(Move1)
lstMoves.append(Move2)
lstMoves.append(Move3)
lstMoves.append(Move4)
lstMoves.append(Move5)
lstMoves.append(Move6)
lstMoves.append(Move7)
lstMoves.append(Move8)
lstMoves.append(Move9)

# Randomly select 3 moves, print their info and attack value, then remove them from the list
for iCount in range(0,3): 
    move_index = random.randrange(len(lstMoves))
    move = lstMoves[move_index]

    print(move.get_info())
    print(f"Generated attack value: {move.generate_attack_value()}")
    

    lstMoves.pop(move_index)

input("Press enter to continue...")