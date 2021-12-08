import numpy as np
import matplotlib.pyplot as plt

with open("in07.txt") as f:
    nums = np.array(sorted(map(int, f.read().split(","))))

# test input
# nums = np.array(sorted([16,1,2,0,4,2,7,1,2,14]))

# This is a brute-force approach, checking every *starting* position
# (luckily, the final position is one of the starting positions)
fuels = [np.abs(nums - nums[idx]).sum() for idx in range(len(nums))]
print("part 1:", min(fuels))

def part2(nums, pos):
    """Calculate the costs of every crab going from its starting position
    (given in `nums`) to the given position `pos`.

    The 'cost' is 0.5*(x^2+x) which is the formula for sum(1..x) where x is the
    (horizontal) distance that the crab has to walk to `pos`.
    """
    distances = np.abs(nums - pos)
    costs = 0.5 * (distances ** 2 + distances)
    # The necessary fuel is the sum of the costs
    return int(costs.sum())

# In part 2 the optimal position isn't one of the starting positions
# so we need to check the entire range (brute-force, again).
fuels = [part2(nums, pos) for pos in range(nums.min(), nums.max())]
print("part 2:", min(fuels))

# There should be some minmax-like to solve this in log(N)...