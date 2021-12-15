from collections import defaultdict
import numpy as np

# read input
grid = np.genfromtxt("in15.txt", delimiter=1, dtype=int)

directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

def pathfind(grid):
    # start at the bottom right (ending position)
    startpos = tuple(n-1 for n in grid.shape)
    bestroutes = np.full(grid.shape, np.nan)
    bestroutes[startpos] = grid[startpos]
    # stack contains {score: [positions]} mappings
    # where score is bestroute[position]
    # so we can find the lowest number quickly
    stack = defaultdict(set, {int(bestroutes[startpos]): {startpos}})
    while stack:
        lowest_dist = min(stack)
        if not stack[lowest_dist]:
            del stack[lowest_dist]
            continue

        # get one of the positions with the lowest distance
        x, y = stack[lowest_dist].pop()

        neighbors = [(x+dx, y+dy) for (dx, dy) in directions
                    if  0 <= x+dx < grid.shape[0]
                    and 0 <= y+dy < grid.shape[1]
                    and np.isnan(bestroutes[x+dx, y+dy])]

        for n in neighbors:
            if n == (0, 0):
                return lowest_dist # the position (0, 0) isn't accounted for
            bestroutes[n] = lowest_dist + grid[n]
            stack[bestroutes[n]].add(n)

print("part 1:", pathfind(grid))

# part 2
# make 5 copies of the grid to the right (hstack)
newgrid = grid.copy()
for i in range(1, 5):
    grid = (grid + 1) % 10
    grid[np.where(grid == 0)] = 1
    newgrid = np.hstack((newgrid, grid))
grid = newgrid

# make 5 copies of the new grid downward (vstack)
newgrid = grid.copy()
for i in range(1, 5):
    grid = (grid + 1) % 10
    grid[np.where(grid == 0)] = 1
    newgrid = np.vstack((newgrid, grid))
grid = newgrid

print("part 2:", pathfind(grid))