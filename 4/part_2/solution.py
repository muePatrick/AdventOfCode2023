import re

def getSolution(input):
  sum = 0
  cards_map = []

  for line in input.splitlines():
    parts = line.split(': ')

    card_index = re.findall("\d+", parts[0])[0]

    number_groups = parts[1].split(' | ')
    winning_numbers = [int(x) for x in number_groups[0].split(' ') if x != '']
    your_numbers = [int(x) for x in number_groups[1].split(' ') if x != '']

    cards_map.append({
      "card_index": int(card_index),
      "winning_numbers": winning_numbers,
      "your_numbers": your_numbers,
      "card_count": 1,
    })

  for i, card in enumerate(cards_map):
    winning_count = 0
    for number in card['your_numbers']:
      if number in card['winning_numbers']:
        winning_count = winning_count + 1
        # if the card was already duplicated to the winning-action multiple times
        for x in range(0, card['card_count']):
          cards_map[i + winning_count]['card_count'] = cards_map[i + winning_count]['card_count'] + 1

  for card in cards_map:
    sum = sum + card['card_count']

  return sum
