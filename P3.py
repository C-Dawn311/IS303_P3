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
        attack = random.randrange(self.low_attack_points,self.high_attack_points + 1)
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

for iCount in range(0,3): 
    move = random.randrange(lstMoves)
    move.get_info(lstMoves[move -1])
    print("Generated attack value: ")
    move.generate_attack_value(lstMoves[move -1])
    lstMoves.remove(lstMoves[move - 1])