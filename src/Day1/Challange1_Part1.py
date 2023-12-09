import re

file_path = '/example/file/path.txt'

with open(file_path, 'r') as file:
    calibration_data = file.readlines()


def calculate_calibration_sum(data):
    total_sum = 0
    for line in data:
        digits = re.findall(r'\d', line)
        if digits:
            calibration_value = int(digits[0] + digits[-1])
            total_sum += calibration_value
    return total_sum


total_calibration_sum = calculate_calibration_sum(calibration_data)
print(total_calibration_sum)
