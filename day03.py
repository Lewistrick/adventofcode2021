# gamma rate = most common bit for each column
# epsilon = andersom: not(gamma)
# power consumption = dec(gamma) * dec(epsilon)

import numpy as np
from collections import Counter

with open("in03.txt") as lines:
    cols = np.array([list(line.strip()) for line in lines]).astype(int)

rows = cols.T

gamma = ""
epsilon = ""
for row in rows:
    n_zeros, n_ones = np.bincount(row)
    if n_zeros > n_ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
gam = int(gamma, 2)
eps = int(epsilon, 2)
print("part 1:", gam * eps)

## part 2

keep_cols = cols.copy()
for pos in range(cols.shape[1]):
    n_zeros, n_ones = np.bincount(keep_cols[:, pos])
    if n_ones >= n_zeros:
        keep_value = 1
    else:
        keep_value = 0
    keep_cols = keep_cols[keep_cols[:, pos] == keep_value]
    if len(keep_cols) == 1:
        break
oxygen = int("".join(keep_cols[0].astype(str)), 2)

keep_cols = cols.copy()
for pos in range(cols.shape[1]):
    n_zeros, n_ones = np.bincount(keep_cols[:, pos])
    if n_ones >= n_zeros:
        keep_value = 0
    else:
        keep_value = 1
    keep_cols = keep_cols[keep_cols[:, pos] == keep_value]
    if len(keep_cols) == 1:
        break

co2 = int("".join(keep_cols[0].astype(str)), 2)
print("part 2:", oxygen * co2)
