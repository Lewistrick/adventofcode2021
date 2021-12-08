from collections import Counter, deque

lanterns = Counter(map(int, open("in06.txt").read().split(",")))
counts = deque([lanterns[i] for i in range(9)], maxlen=9)
# deque is slightly faster than list; defining maxlen is also slightly better

for day in range(256):
    counts.rotate(-1)
    counts[6] += counts[-1]
#     if day == 79:
#         print("part 1:", sum(counts))

# print("part 2:", sum(counts))