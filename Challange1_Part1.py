import re

file_path = '/Users/louisgrennell/PycharmProjects/pythonProject/input.txt'

# Reading the file
with open(file_path, 'r') as file:
    calibration_data = file.readlines()


def calculate_calibration_sum(data):
    total_sum = 0
    for line in data:
        # Extracting digits from each line
        digits = re.findall(r'\d', line)
        if digits:
            # Combining the first and last digit to form a two-digit number
            calibration_value = int(digits[0] + digits[-1])
            total_sum += calibration_value
    return total_sum


# Calculating the total sum of calibration values
total_calibration_sum = calculate_calibration_sum(calibration_data)
print(total_calibration_sum)
