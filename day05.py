import re
from collections import defaultdict

line_re = re.compile("^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)$")
coords = []
diags = []
with open("in05.txt") as infile:
    for line in infile:
        x1, y1, x2, y2 = map(int, line_re.match(line.strip()).groups())
        if x1 == x2 or y1 == y2:
            coords.append((x1, y1, x2, y2))
        else:
            diags.append((x1, y1, x2, y2))

# the `occupied` dict contains {(x,y) : n} pairs where (x,y) is the coordinate
# and n is the number of lines that cross the space
occupied = defaultdict(int)
for x1, y1, x2, y2 in coords:
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            occupied[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            occupied[(x, y1)] += 1

print("part 1:", sum(1 for val in occupied.values() if val>1))

# for part 2, add the diagonals
for x1, y1, x2, y2 in diags:
    xr = range(x1, x2+1) if x1 < x2 else range(x1, x2-1, -1)
    yr = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
    for x, y in zip(xr, yr):
        occupied[(x, y)] += 1

print("part 2:", sum(1 for val in occupied.values() if val>1))
