position = 0
depths = [0, 0] # two values, one for each part of the puzzle
aim = 0
with open("in02.txt") as commands:
    for direction, distance in map(str.split, commands):
        amount = int(distance) * (-1 if direction == "down" else 1)
        if direction in ("up", "down"):
            depths[0] -= amount
            aim -= amount
        elif direction == "forward":
            position += amount
            depths[1] += (aim * amount)
for part, depth in enumerate(depths, 1):
    print(f"Part {part}: {position * depth}")