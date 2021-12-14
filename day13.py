# Read the input; the 'fold' variable indicates whether we're reading folds;
# if False, we're reading dots.
fold = False
coords = set()
folds = []
maxx, maxy = 0, 0
with open("in13.txt") as f:
    for line in f:
        if not line.strip():
            # the empty line indicates the split between the dots and the folds
            fold = True
        elif not fold:
            x, y = map(int, line.split(","))
            maxx = max(x, maxx)
            maxy = max(y, maxy)
            coords.add((x, y))
        else:
            dir, val = line[11:].split("=")
            val = int(val)
            folds.append((dir, val))

# Process all the folds. Every fold has an index (we need it to print part 1),
# a direction (x or y) and a value (the fold position).
for idx, (dir, val) in enumerate(folds):
    # Update the paper size
    if dir == "x":
        maxx = val - 1
    if dir == "y":
        maxy = val - 1

    # Update the coordinates.
    # For example, if we fold over y=7, a dot (x, 8) would be replaced to (x, 6)
    # or in general: a dot (x, k) would be replaced to (x, 7-(k-7))
    # which is equal to (x, 2*7-k)
    newcoords = set()
    for (x, y) in coords:
        newx, newy = x, y
        if dir == "x" and x > val:
            newx = 2 * val - x
        elif dir == "y" and y > val:
            newy = 2 * val - y
        newcoords.add((newx, newy))
    coords = newcoords

    # For part 1, print the number of dots after the *first* fold
    if idx == 0:
        print("part 1:", len(coords))

# Print the text. Double characters are used to increase readability.
print("part 2:")
for y in range(maxy + 1):
    for x in range(maxx + 1):
        if (x, y) in coords:
            print("██", end="")
        else:
            print("  ", end="")
    print()
