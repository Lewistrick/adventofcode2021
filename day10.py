from collections import deque


def check_incorrect(chars):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    pairs = {ch2: ch1 for ch1, ch2 in ["{}", "[]", "()", "<>"]}
    q = deque()
    for ch in chars:
        if ch in pairs.values():
            q.append(ch)
        elif q:
            if pairs[ch] != q.pop():
                return scores[ch]
    return 0

def check_incomplete(chars):
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    pairs = {ch1: ch2 for ch1, ch2 in ["{}", "[]", "()", "<>"]}
    q = deque()
    for ch in chars:
        if ch in pairs.keys():
            q.append(ch)
        else:
            pch = q.pop()
    score = 0
    while q:
        score *= 5
        score += scores[pairs[q.pop()]]
    return score

part1 = 0
incomp_scores = []
with open("in10.txt") as f:
    for line in f:
        incorr_score = check_incorrect(line.strip())
        part1 += incorr_score
        if incorr_score == 0:
            # if the line is correct, pass it to the part 2 function
            incomp_scores.append(check_incomplete(line.strip()))

print(part1)

incomp_scores.sort()
part2 = incomp_scores[len(incomp_scores) // 2]
print(part2)
