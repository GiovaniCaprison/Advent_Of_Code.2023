scratchcard_data = []


def calculate_points(scratchcard_lines):
    ans = 0

    for row in scratchcard_lines:
        parts = row.strip().split('|')
        winning_numbers = set(map(int, parts[0].split()[2:]))
        your_numbers = set(map(int, parts[1].split()))

        matching_numbers = winning_numbers.intersection(your_numbers)
        if matching_numbers:
            card_points = 1 << (len(matching_numbers) - 1)
            ans += card_points

    return ans


for line in open('/example/file/path.txt').readlines():
    scratchcard_data.append(line.strip())

total_points = calculate_points(scratchcard_data)
print(total_points)
