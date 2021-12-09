from functools import reduce

grid = []
with open("in09.txt") as lines:
    for line in lines:
        grid.append([int(i) for i in line.strip()])

directions = [(-1,0), (0,-1), (1,0), (0,1)]

# find lowest points
lowpoints = []
for x, row in enumerate(grid):
    for y, val in enumerate(row):
        to_check = []
        for dx, dy in directions:
            if x + dx < 0 or y + dy < 0:
                continue
            if x + dx >= len(grid) or y + dy >= len(row):
                continue
            to_check.append(grid[x+dx][y+dy])
        if all(val < check for check in to_check):
            lowpoints.append(val)
print("part1:", sum(lowpoints) + len(lowpoints))

# part 2
to_check = {(x, y)
            for x in range(len(grid))
            for y in range(len(grid[0]))
            if grid[x][y] != 9}

basins = []
while to_check:
    # create the first basin
    curr_basin = [to_check.pop()]
    # make a list of coords in this basin to check
    to_check_sub = list(curr_basin)
    while to_check_sub:
        # as long as we found new coords in this basin, keep expanding it
        new_coords = []
        # expand every new-found coord
        for (x, y) in to_check_sub:
            # from that coord, check every direction
            for dx, dy in directions:
                # find the neighbor in that direction
                neighbor = (x + dx, y + dy)
                # if the neighbor is still in to_check, it's in the basin
                if neighbor in to_check:
                    to_check.remove(neighbor)
                    new_coords.append(neighbor)
                    curr_basin.append(neighbor)
        to_check_sub = new_coords
    basins.append(curr_basin)
    curr_basin = []

biggest_basins = sorted(basins, key=len)[-3:]
part2 = reduce(int.__mul__, (len(basin) for basin in biggest_basins))
print("part 2:", part2)