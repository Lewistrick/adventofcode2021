from itertools import count
from collections import Counter, defaultdict

def score(bigrams, lastchar):
    """Calculate & output the 'score' for a given set of bigrams.

    We need the last character because the bigrams should only count the first
    character (to avoid duplicate counts), except for the last bigram
    (otherwise the second character of that bigram won't be counted).
    """
    counts = Counter()
    for (ch1, _), n in bigrams.items():
        counts.update({ch1: n})
    counts.update({lastchar: 1})
    occs = counts.values()
    return max(occs) - min(occs)

# Read input
rules = {}
with open("in14.txt") as lines:
    polymer = next(lines).strip()
    _ = next(lines) # empty line
    for line in lines:
        i, o = line.strip().split(" -> ")
        rules[tuple(i)] = o

# Count pairs of letters
bigrams = Counter(zip(polymer, polymer[1:]))

# We need the lastchar for the `score` function (it doesn't change though)
lastchar = polymer[-1]
for step in range(40):
    # From now on, the bigram counter will be a defaultdict
    new_bigrams = defaultdict(int)
    # Update the bigram counts
    for (c1, c2), n in bigrams.items():
        c3 = rules[(c1, c2)]
        new_bigrams[(c1, c3)] += n
        new_bigrams[(c3, c2)] += n
    bigrams = new_bigrams

    if step == 9:
        print("part 1:", score(bigrams, lastchar))

print("part 2:", score(bigrams, lastchar))
