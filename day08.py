data = [i.strip("\n") for i in open("in08.txt").readlines()]

# part 1
part1 = 0
with open("in08.txt") as f:
    lines = f.readlines()
    for line in lines:
        outputs = line.split("|")[-1].strip().split()
        part1 += sum(len(conns) in (2,3,4,7) for conns in outputs)
print("part1:", part1)

# part 2
class Display:
    nsegs = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

    def __init__(self, inputs, outputs):
        self.inputs = {"".join(sorted(i)) for i in inputs}
        self.outputs = ["".join(sorted(i)) for i in outputs]
        # The digits represent the connector-digit pairs,
        # e.g. {"abcde": [0,6,9]} means that the connector set "abcde"
        # could be representing 0, 6 or 9.
        self.digits = {g: list(range(10)) for g in self.inputs}
        # Rule out wrong-length possibilities
        for conns in self.digits.keys():
            self.digits[conns] = [num for num in self.digits[conns]
                                  if self.nsegs[num] == len(conns)]

    @classmethod
    def from_line(cls, line):
        inputs, outputs = line.split(" | ")
        return cls(inputs.split(), outputs.split())

    def solve(self):
        # find the connectors for the 1
        one = next(d for d in self.digits if len(d) == 2)
        # find the connectors for the 7
        seven = next(d for d in self.digits if len(d) == 3)
        # find the top right connector by looking at the 0, 6 and 9 connector sets:
        # the 6 doesn't use all of 7's segments, whereas 0 and 9 do
        six = next(d for (d, nums) in self.digits.items()
                         if nums == [0, 6, 9]
                         and not all(c in d for c in seven))
        # find the top right connector (the ch in the 1 that's not in the 6)
        topr = next(ch for ch in one if ch not in six)
        # find the bottom right connector (the other one in the 1)
        btmr = next(ch for ch in one if ch != topr)
        # find the three (that has both chs from the 1)
        three = next(d for d in self.digits if len(d) == 5 and all(ch in d for ch in one))
        # find the four
        four = next(d for d in self.digits if len(d) == 4)
        # the middle connector is the overlap between 3 and 4 that's not in the 1
        mid = next(ch for ch in four if ch not in one and ch in three)
        # the two is the only digit that doesn't use the btmr segment
        two = next(d for d in self.digits if not btmr in d)
        # find the five
        five = next(d for d in self.digits if len(d) == 5 and d not in (two, three))
        # find the last digits
        eight = next(d for d, x in self.digits.items() if 8 in x)
        zero = next(d for d in self.digits if len(d) == 6 and mid not in d)
        nine = next(d for d in self.digits if len(d) == 6 and d not in (zero, six))

        alldigits = {conns: digit for digit, conns in enumerate([
            zero, one, two, three, four, five, six, seven, eight, nine])}

        solution = sum(digit * (10 ** i) for i, digit in zip(
            range(len(self.outputs)-1, -1, -1),
            [alldigits[conns] for conns in self.outputs]
        ))
        return solution


part2 = sum(Display.from_line(line).solve() for line in lines)
print("part2:", part2)