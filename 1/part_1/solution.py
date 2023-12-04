def getSolution(input):
  sum = 0

  for line in input.splitlines():
    first_num = None
    last_num = None
    for char in line:
      is_num = char.isnumeric()
      if not is_num:
        continue

      if not first_num:
        first_num = char
      last_num = char

    calibration_value = int(f"{first_num}{last_num}")
    sum = sum + calibration_value
    print(f"{line} -> {first_num} / {last_num} = {calibration_value}")

  return sum
