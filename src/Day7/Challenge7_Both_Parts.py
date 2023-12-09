import collections

input_file_path = "/example/file/path.txt"

with open(input_file_path, 'r') as file:
    data = file.read()

cardval = {v: i for i, v in enumerate('AKQJT98765432')}


def rank(hand):
    c = collections.Counter(hand)
    if 5 in c.values():
        return 1
    if 4 in c.values():
        return 2
    if 3 in c.values():
        if 2 in c.values():
            return 3
        return 4
    if 2 in c.values():
        if collections.Counter(c.values())[2] == 2:
            return 5
        return 6
    return 7


answer_a = sum(
    (i + 1) * b
    for (i, (h, b)) in enumerate(reversed(sorted([
        ([rank(hand)] + [cardval[c] for c in hand], int(bid))
        for hand, bid in [
            line.split()
            for line in data.strip().splitlines()
        ]
    ])))
)

cardval = {v: i for i, v in enumerate('AKQT98765432J')}


def j_rank(hand):
    if 'J' not in hand:
        return rank(hand)
    c = collections.Counter(hand)
    try:
        most_common = next(
            card for card, count in c.most_common() if card != 'J')
    except StopIteration:
        return rank(hand)
    return rank(hand.replace('J', most_common))


answer_b = sum(
    (i + 1) * b
    for (i, (h, b)) in enumerate(reversed(sorted([
        ([j_rank(hand)] + [cardval[c] for c in hand], int(bid))
        for hand, bid in [
            line.split()
            for line in data.strip().splitlines()
        ]
    ])))
)

print(answer_a, answer_b)
