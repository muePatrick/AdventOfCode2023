import re

def check_gear(schematic_map, line, column):
  line_count = len(schematic_map)
  column_count = len(schematic_map[0])

  if (line < 0 or line >= line_count):
    return False
  if (column < 0 or column >= column_count):
    return False

  if (schematic_map[line][column] == '*'):
    return True

  return False


def getSolution(input):
  schematic_map = []
  number_candidates = []
  gear_candidates = []
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

    if (check_gear(schematic_map, number['line'], number['column_start'] - 1)):
      gear_candidates.append({
        'number': number['number'],
        'gear_position': (number['line'], number['column_start'] - 1)
      })
      continue

    if (check_gear(schematic_map, number['line'], number['column_end'])):
      gear_candidates.append({
        'number': number['number'],
        'gear_position': (number['line'], number['column_end'])
      })
      continue

    for i in range(number['column_start'] - 1, number['column_end'] + 1):
      if (check_gear(schematic_map, number['line'] - 1, i)):
        gear_candidates.append({
          'number': number['number'],
          'gear_position': (number['line'] - 1, i)
        })
        continue

      if (check_gear(schematic_map, number['line'] + 1, i)):
        gear_candidates.append({
          'number': number['number'],
          'gear_position': (number['line'] + 1, i)
        })
        continue

  print('')
  print(gear_candidates)
  gear_candidates_count = len(gear_candidates)
  for gear_index, gear_candidate in enumerate(gear_candidates):
    for gear2_index in range(gear_index+1, gear_candidates_count):
      if (gear_candidate['gear_position'] == gear_candidates[gear2_index]['gear_position']):
        print('')
        print(gear_candidate)
        sum = sum + (gear_candidate['number'] * gear_candidates[gear2_index]['number'])

  return sum
