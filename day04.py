import numpy as np

class BingoCard:
    def __init__(self, grid):
        self.grid = grid
        self.crossed = np.zeros(grid.shape)
        self.diag_x = range(self.grid.shape[0])
        self.diag_y = range(self.grid.shape[1]-1, -1, -1)

    @classmethod
    def from_lines(cls, lines):
        grid = np.array(lines)
        return cls(grid)

    def __str__(self):
        """Print the grid; replace crossed numbers by 'XX'."""
        output = ""
        for y, row in enumerate(self.grid):
            for x, val in enumerate(row):
                if self.crossed[y, x]:
                    output += "XX "
                else:
                    output += f"{val:2d} "
            output += "\n"
        return output

    def cross(self, num):
        """Cross one number from the card."""
        matches = np.where(self.grid == num)
        self.crossed[matches] = 1

        # check for horizontal bingos
        for line in self.crossed:
            if (line == 1).all():
                return True

        # check for vertical bingos
        for line in self.crossed.T:
            if (line == 1).all():
                return True

        # check for diagonal bingos
        diags = [self.grid[self.diag_x, self.diag_x],
                 self.grid[self.diag_x, self.diag_y]]
        for line in diags:
            if (line == 1).all():
                return True

        # if we get here, no diags are found
        return False

    def score(self):
        """Calculate the sum of not-crossed numbers."""
        open_ids = np.where(self.crossed == 0)
        left_nums = self.grid[open_ids]
        return left_nums.sum()

    def reset(self):
        """Uncross all numbers."""
        self.crossed = np.zeros(self.grid.shape)


# Read the input file and save as BingoCard instances
with open("in04.txt") as lines:
    numbers = list(map(int, next(lines).split(",")))

    bingocards = []
    currcard = []
    for line in lines:
        if line.strip():
            currcard.append(list(map(int, line.split())))
        elif not currcard:
            continue
        else:
            bingocards.append(BingoCard.from_lines(currcard))
            currcard = []
    bingocards.append(BingoCard.from_lines(currcard))

# part1

has_bingo = False
for num in numbers:
    for card in bingocards:
        has_bingo = card.cross(num)
        if has_bingo:
            break
    if has_bingo:
        break
print("part 1:", card.score() * num)

## part 2
for card in bingocards:
    card.reset()

for num in numbers:
    keep_ids = []
    for idx, card in enumerate(bingocards):
        if not card.cross(num):
            keep_ids.append(idx)

    # if no cards are kept, assume that there's only one card left
    if not len(keep_ids):
        break

    # remove all bingocards that won
    bingocards = [bingocards[keep_id] for keep_id in keep_ids]

card = bingocards[0]
print("part 2:", card.score() * num)
