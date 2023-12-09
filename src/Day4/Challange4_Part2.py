scratchcard_data = []


def count_total_scratchcards(scratchcard_lines):
    scratchcards = []
    for row in scratchcard_lines:
        parts = row.strip().split('|')
        winning_numbers = set(map(int, parts[0].split()[2:]))
        your_numbers = set(map(int, parts[1].split()))
        scratchcards.append((winning_numbers, your_numbers))

    total_cards = len(scratchcards)
    to_process = list(range(total_cards))

    while to_process:
        next_round = []
        for card_index in to_process:
            winning_numbers, your_numbers = scratchcards[card_index]
            matching_numbers = len(winning_numbers.intersection(your_numbers))
            for i in range(card_index + 1, card_index + 1 + matching_numbers):
                if i < total_cards:
                    next_round.append(i)

        total_cards += len(next_round)
        to_process = next_round

    return total_cards


for line in open('/example/file/path.txt').readlines():
    scratchcard_data.append(line.strip())

total_scratchcards = count_total_scratchcards(scratchcard_data)
print(total_scratchcards)
