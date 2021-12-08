fn = "in01.txt"
with open(fn) as lines:
    ocean_depths = [int(x.strip()) for x in lines]

part1 = sum([n < m for n, m in zip(ocean_depths, ocean_depths[1:])])
print(part1)

window_length = 3
window_sums = [sum(ocean_depths[i : i + window_length])
              for i in range(len(ocean_depths) - window_length + 1)]
part2 = sum(n < m for n, m in zip(window_sums, window_sums[1:]))
print(part2)