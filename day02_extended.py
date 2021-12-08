import matplotlib.pyplot as plt
import pandas as pd

# two lists of positions and depths, one for each part of the puzzle
positions = [[0], [0]]
depths = [[0], [0]]
aims = [0]
with open("in02.txt") as commands:
    for direction, distance in map(str.split, commands):
        amount = int(distance)

        if direction == "up":
            # for part 1, move up
            positions[0].append(positions[0][-1])
            depths[0].append(depths[0][-1] - amount)
            # for part 2, don't move but just adjust the aim
            aims.append(aims[-1] - amount)
        elif direction == "down":
            # for part 1, move down
            positions[0].append(positions[0][-1])
            depths[0].append(depths[0][-1] + amount)
            # for part 2, don't move but just adjust the aim
            aims.append(aims[-1] + amount)
        elif direction == "forward":
            # for part 1, only adjust the position
            positions[0].append(positions[0][-1] + amount)
            depths[0].append(depths[0][-1])
            # for part 2, adjust both position and depth based on aim
            positions[1].append(positions[1][-1] + amount)
            depths[1].append(depths[1][-1] + aims[-1] * amount)

# plt.plot(positions[0], depths[0], ".-", label="part 1")
# plt.plot(positions[1], depths[1], ".-", label="part 2")
# # plt.yscale("log")
# plt.xlabel("position (forward)")
# plt.ylabel("depth (up/down)")
# plt.legend()
# plt.show()

posdf = pd.DataFrame({
    "position": positions[0],
    "depth1": depths[0]}).merge(
        pd.DataFrame({
            "position": positions[1],
            "depth2": depths[1]}),
        on="position")

plt.plot(posdf.depth2, posdf.depth1, ".-")
plt.xlabel("part 2")
plt.ylabel("part 1")
plt.show()