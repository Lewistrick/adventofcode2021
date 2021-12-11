from itertools import count
import numpy as np

# read data as np-array
grid = np.genfromtxt("in11.txt", delimiter=1, dtype=int)

# the directions in which a neighbor can be
dirs = (
    (-1,-1), (-1,0), (-1,1),
    ( 0,-1),         ( 0,1),
    ( 1,-1), ( 1,0), ( 1,1))

xmax, ymax = grid.shape

def find_neighbors(x, y, skip):
    return [(x+dx, y+dy)
            for (dx, dy) in dirs
            if 0<=x+dx<xmax and 0<=y+dy<ymax
            and (x+dx, y+dy) not in skip]

n_flashes = 0
for step in count(1):
    # update the energy level of every octopus
    grid += 1

    # keep track of which octopuses flashed in this step
    flashed = set()

    # keep activating until no flashes occur
    while True:
        # find the coords of flashing coordinates,
        # but leave the ones out that already flashed
        flashes = set(zip(*np.where(grid > 9))) - flashed

        # if there are no new flashes, this step is over
        if not flashes:
            break

        # find neighbors of flashes
        for flash in flashes:
            neighbors = find_neighbors(*flash, skip=flashes|flashed)
            for x, y in neighbors:
                grid[x, y] += 1

        # update the set of flashed octopuses in this step
        flashed |= flashes

    # update the number of flashes seen
    n_flashes += len(flashed)

    # update the grid (all flashed octopuses' energy levels are set to 0)
    for x, y in flashed:
        grid[x, y] = 0

    if step == 100:
        print("part 1:", n_flashes)

    if len(flashed) == grid.shape[0] * grid.shape[1]:
        print("part 2:", step)
        break