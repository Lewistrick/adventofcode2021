from collections import defaultdict
import numpy as np

# read input
grid = np.genfromtxt("in15.txt", delimiter=1, dtype=int)

directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

def pathfind(grid):
    """Pathfinder through a grid (top left - bottom right).

    This pathfinder finds the best route to the bottom right for every position
    in the grid, starting at the bottom right.

    The best route to the bottom right starting from the bottom right
    equals the number in the bottom right square, of course.

    Next, the shortest route from the bottom right's neighbors
    equals the bottom right square's value + the neighbor's value.

    So now, we accounted for all the neighbors of the bottom right square. The
    two neighbors are put in a stack. From now on, we select the position
    that has the lowest score, because it's guaranteed you can calculate the
    lowest score starting from there.
    The stack is actually a dictionary with {score: {positions}} mappings
    instead of just a list of positions, because the stack is expected to grow
    to a size of i+j for an i*j grid (in part 2, i=j=500), which would make
    searching in a list become very slow. Instead, we find the lowest score
    using min() and grab a random position to expand from.

    Once we arrive at a neighbor of the starting position of the ship (0, 0),
    we know we have found the shortest route from the starting position.
    As this position is never 'entered' by the ship (it's already there),
    we don't add the starting positions's value to the total score.
    """
    # start at the bottom right (ending position)
    startpos = tuple(n-1 for n in grid.shape)
    bestroutes = np.full(grid.shape, np.nan)
    bestroutes[startpos] = grid[startpos]
    # stack contains {score: [positions]} mappings
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

# Solve part 1
print("part 1:", pathfind(grid))

## Part 2
# Make 5 'incremented copies' of the grid to the right (hstack)
newgrid = grid.copy()
for i in range(1, 5):
    # The 'incremented copy' first increments the entire grid by 1
    # and 'rolls around' at 10...
    grid = (grid + 1) % 10
    # ... but that yields 0 values, which we increment to 1.
    grid[np.where(grid == 0)] = 1
    newgrid = np.hstack((newgrid, grid))
grid = newgrid

# For this new (wide) grid, do the same, but downward (vstack)
newgrid = grid.copy()
for i in range(1, 5):
    grid = (grid + 1) % 10
    grid[np.where(grid == 0)] = 1
    newgrid = np.vstack((newgrid, grid))
grid = newgrid

# Solve part 2 for the actual grid
print("part 2:", pathfind(grid))