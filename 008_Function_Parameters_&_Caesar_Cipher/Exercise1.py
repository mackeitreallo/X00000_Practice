#You are painting a wall.
#The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
#Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

#number of cans = (wall height ✖️ wall width) ÷ coverage per can.

#e.g. Height = 2, Width = 4, Coverage = 5

#number of cans = (2 ✖️ 4) ÷ 5

#But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

#IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.

#For every 1 can of paint
import math

coverage = 5
height = float(input("\nWhat is the height of the wall in meters?: "))
width = float(input("\nWhat is the width of the wall in meters?: "))

def compute(can = coverage, h = height, w = width):
    answer = round((int(math.ceil((h * w) / can))), 0)
    print(f"\nYou need {answer} cans to paint the wall.")

compute(can = coverage, h = height, w = width)
