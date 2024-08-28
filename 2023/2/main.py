import re

def problem1(calibrations):
    sum = 0
    for calibration in calibrations:
        numbers = re.findall(r'\d', calibration)
        numbers = [int(number) for number in numbers]
        sum += numbers[0] * 10 + numbers[::-1][0]
    print(sum)

def problem2(calibrations):
    number_map = {
        'one': "o1e",
        'two': "t2o",
        'three': "t3e",
        'four': "f4r",
        'five': "f5e",
        'six': "s6x",
        'seven': "s7n",
        'eight': "e8t",
        'nine': "n9e",
    }
    converted = []
    for calibration in calibrations:
        for key, value in number_map.items():
            calibration = calibration.replace(key, str(value))
        converted.append(calibration)
    problem1(converted)

if __name__ == '__main__':
    with open("data", "r") as file:
        calibrations = file.readlines()
    problem1(calibrations)
    problem2(calibrations)
