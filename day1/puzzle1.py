import math

def calcFuel(weight):
    return math.floor(weight / 3) - 2

def calcFuelRecursively(weight):
    fuel = calcFuel(weight)
    total = 0
    while fuel > 0:
        total += fuel
        fuel = calcFuel(fuel)
    return total


with open('puzzle_1_input.txt') as fp:
    total = 0
    for line in fp:
        total += calcFuelRecursively(int(line))

    print(total)