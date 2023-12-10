import re

def check(schematic_map, line, column):
  line_count = len(schematic_map)
  column_count = len(schematic_map[0])

  if (line < 0 or line >= line_count):
    return False
  if (column < 0 or column >= column_count):
    return False

  if (schematic_map[line][column] != '.'):
    return True

  return False


def getSolution(input):
  schematic_map = []
  number_candidates = []
  sum = 0

  for line_number, line in enumerate(input.splitlines()):
   schematic_map.append([c for c in line])

   for number_match in re.finditer("(\d+)", line):
     number_candidates.append({
      "number": int(number_match.groups()[0]),
      "line": line_number,
      "column_start": number_match.span()[0],
      "column_end": number_match.span()[1],
     })

  for number in number_candidates:
    print('')
    print(number)

    if (check(schematic_map, number['line'], number['column_start'] - 1)
      or check(schematic_map, number['line'], number['column_end'])):
      sum = sum + number['number']
      continue

    for i in range(number['column_start'] - 1, number['column_end'] + 1):
      if (check(schematic_map, number['line'] - 1, i)
        or check(schematic_map, number['line'] + 1, i)):
        sum = sum + number['number']
        continue

  return sum
