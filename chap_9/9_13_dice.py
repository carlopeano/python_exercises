from random import randint

class Dice:
    """An attempt to represent a dice"""

    def __init__(self, sides_number):
        """Initialize a die"""
        self.sides_number = sides_number
        self.first_face = 1


    def roll_dice(self):
        """
        Generate a random number between 1 and and 
        the number of the dice's sides
        """
        rolled_number = randint(self.first_face, self.sides_number)
        print( f"\nI throw a {self.sides_number}-sided dice and the "
            f"result is {rolled_number}")


    def multiple_rolls(self, rolls):
        """Roll the die multiple times"""
        self.rolls = rolls
        
        print(f"\nI throw a {self.sides_number}-sided dice "
                f"{self.rolls} times and the results are:")
        
        for roll in range(self.rolls):
            rolled_number = randint(self.first_face, self.sides_number)
            print(f"\t- Roll number {roll+1} is {rolled_number}")

        # n = 1
        # while n <= self.rolls:
        #     rolled_number = randint(self.first_face, self.sides_number)
        #     print(f"\t- Roll number {n} is {rolled_number}")
        #     n += 1


my_dice = Dice (6)
my_dice.roll_dice()
my_dice.multiple_rolls(10)

your_dice = Dice (10)
your_dice.roll_dice()
your_dice.multiple_rolls(10)

d20_dice = Dice(20)
d20_dice.roll_dice()
d20_dice.multiple_rolls(10)