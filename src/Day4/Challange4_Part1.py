scratchcard_data = []


def calculate_points(scratchcard_lines):
    ans = 0

    for row in scratchcard_lines:
        # Splitting the line into winning numbers and numbers you have
        parts = row.strip().split('|')
        winning_numbers = set(map(int, parts[0].split()[2:]))  # Skipping 'Card X:'
        your_numbers = set(map(int, parts[1].split()))

        # Calculating points for this card
        matching_numbers = winning_numbers.intersection(your_numbers)
        if matching_numbers:
            card_points = 1 << (len(matching_numbers) - 1)  # 2^(n-1) where n is the number of matches
            ans += card_points

    return ans


for line in open('/example/file/path.txt').readlines():
    scratchcard_data.append(line.strip())

# Calculate the total points for the scratchcards
total_points = calculate_points(scratchcard_data)
print(total_points)
