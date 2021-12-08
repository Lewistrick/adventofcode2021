from collections import Counter

lanterns = Counter(map(int, open("in06.txt").read().split(",")))

for day in range(256):
    new = Counter({i-1: k for i, k in lanterns.items() if i > 0})
    new.update({6: lanterns[0], 8: lanterns[0]})
    lanterns = new
    if day == 79:
        print("part 1:", sum(lanterns.values()))

print("part 2:", sum(lanterns.values()))