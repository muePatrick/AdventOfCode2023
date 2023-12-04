import re

number_mapping = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "ten": 10
}

re_first_number = "^.*?(one|two|three|four|five|six|seven|eight|nine|\d).*$"
re_last_number  = "^.*(one|two|three|four|five|six|seven|eight|nine|\d).*$"

def getSolution(input):
  sum = 0
  for line in input.splitlines():
    first_num = re.findall(re_first_number, line)[0]
    last_num = re.findall(re_last_number, line)[0]

    if not first_num.isnumeric():
      first_num = number_mapping[first_num]
    if not last_num.isnumeric():
      last_num = number_mapping[last_num]

    calibration_value = int(f"{first_num}{last_num}")
    sum = sum + calibration_value
    print(f"{line} -> {first_num} / {last_num} = {calibration_value}")

  return sum
