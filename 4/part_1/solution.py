import math

def getSolution(input):
  sum = 0

  for line in input.splitlines():
    winning_count = 0

    groups = line.split(': ')[1].split(' | ')
    winning_numbers = [int(x) for x in groups[0].split(' ') if x != '']
    your_numbers = [int(x) for x in groups[1].split(' ') if x != '']

    for number in your_numbers:
      if number in winning_numbers:
        if winning_count == 0:
          winning_count = 1
        else:
          winning_count = winning_count * 2

    sum = sum + winning_count

  return sum
