# Authors: Courtney Bingham, Anna Pettit, Braden Adams, Ethan Lawson

import random

# Classes

class Move:
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points
    # prints all info out
    def get_info(self):
        print(f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points")
    # randomly generates number between low and high attack points
    def generate_attack_value(self):
        attack = random.randrange(self.low_attack_points,self.high_attack_points)
        return attack


class Pokemon:
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = self.hit_points
    # prints out info
    def get_info(self):
        print(f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}")
    # increases hit_poitns by 15 and prints out new messsage
    def heal(self):
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")

lstMoves = []

Move1 = Move("Tackle", "Normal", 5, 20)
Move2 = Move("Quick Attack", "Normal", 6, 25)
Move3 = Move("Slash", "Normal", 10, 30)
Move4 = Move("Flamethrower", "Fire", 5, 30)
Move5 = Move("Ember", "Fire", 10, 20)
Move6 = Move("Water Gun", "Water", 5, 15)
Move7 = Move("Hydro", "Pump", 20, 25)
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

for iCount in range(0,3): 
    move = random.randrange(lstMoves)
    move.get_info(lstMoves[move -1])
    print("Generated attack value: ")
    move.generate_attack_value(lstMoves[move -1])
    lstMoves.remove(lstMoves[move - 1])