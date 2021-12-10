from collections import deque

# found a trick to calculate scores for part 1, but it's not codegolf-worthy
scores1 = {ch: round(57 * 21 ** (2 - ord(ch) % 19 % 5)) for ch in ")]}>"}
# same for the scores for part 2
scores2 = {ch: s for s, ch in enumerate(")]}>", 1)}
pairs = {ch1: ch2 for ch1, ch2 in ["{}", "[]", "()", "<>"]}
pairs_rev = {ch2: ch1 for ch1, ch2 in ["{}", "[]", "()", "<>"]}

def check_incorrect(chars):
    """Used for part 1"""
    # This queue only contains opening characters.
    # If a matching closing character is found, the last one is removed.
    q = deque()
    for ch in chars:
        if ch in pairs:
            # add opening character
            q.append(ch)
        elif q and pairs_rev[ch] != q.pop():
            # the closer doesn't match the last opener in the queue
            # (i.e. another closer was expected)
            # so return the score of the character that was found
            return scores1[ch]
    return 0

def check_incomplete(chars):
    """Used for part 2.

    This function will only receive correct strings because the incorrect
    strings are handled by part 1.
    """
    # This queue only contains opening characters.
    # When a matching closing character is found, the last one is removed.
    q = deque()
    for ch in chars:
        if ch in pairs:
            # add opener
            q.append(ch)
        else:
            # remove opener
            q.pop()
    score = 0
    while q:
        score = 5 * score + scores2[pairs[q.pop()]]
    return score

part1 = 0
incomplete_scores = []
with open("in10.txt") as f:
    for line in f:
        incorrect_score = check_incorrect(line.strip())
        part1 += incorrect_score
        # if the line is incorrect, pass it to the part 2 function
        if incorrect_score == 0:
            incomplete_scores.append(check_incomplete(line.strip()))

print("part 1:", part1)
print("part 2:", sorted(incomplete_scores)[len(incomplete_scores) // 2])
