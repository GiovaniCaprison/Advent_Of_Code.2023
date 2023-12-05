scratchcard_data = []


def count_total_scratchcards(scratchcard_lines):
    # Parsing the scratchcards into a more usable format
    scratchcards = []
    for row in scratchcard_lines:
        parts = row.strip().split('|')
        winning_numbers = set(map(int, parts[0].split()[2:]))  # Skipping 'Card X:'
        your_numbers = set(map(int, parts[1].split()))
        scratchcards.append((winning_numbers, your_numbers))

    total_cards = len(scratchcards)  # Starting with the original set of scratchcards
    to_process = list(range(total_cards))  # List of indices of scratchcards to process

    while to_process:
        next_round = []  # Cards to process in the next round
        for card_index in to_process:
            winning_numbers, your_numbers = scratchcards[card_index]
            matching_numbers = len(winning_numbers.intersection(your_numbers))
            # For each match, add a copy of the next card, if it exists
            for i in range(card_index + 1, card_index + 1 + matching_numbers):
                if i < total_cards:
                    next_round.append(i)

        # Add the number of cards won in this round to the total
        total_cards += len(next_round)
        # Set the cards to process in the next round
        to_process = next_round

    return total_cards


for line in open('/example/file/path.txt').readlines():
    scratchcard_data.append(line.strip())

# Counting the total number of scratchcards including copies
total_scratchcards = count_total_scratchcards(scratchcard_data)
print(total_scratchcards)
