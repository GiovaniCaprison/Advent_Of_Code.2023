import re

new_file_path = '/example/file/path.txt'

with open(new_file_path, 'r') as file:
    calibration_data = file.readlines()


def corrected_extract_and_sum_digits(data):
    total_sum = 0
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    for line in data:
        first_match = re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        first_digit = first_match.group() if first_match else None
        if first_digit in number_map:
            first_digit = number_map[first_digit]

        last_match = re.search(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1])
        if last_match:
            last_digit = last_match.group()[::-1]
            if last_digit in number_map:
                last_digit = number_map[last_digit]
        else:
            last_digit = None

        if first_digit is not None and last_digit is not None:
            total_sum += int(first_digit + last_digit)

    return total_sum


corrected_total_sum = corrected_extract_and_sum_digits(calibration_data)
print(corrected_total_sum)
