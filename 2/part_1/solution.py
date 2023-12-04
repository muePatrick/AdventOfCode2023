import re

max_balls = {
  "red": 12,
  "green": 13,
  "blue": 14
}

def getSolution(input):
  sum = 0

  for line in input.splitlines():
    all_games_valid = True

    id = re.findall(r"(?<=Game )\d+", line)[0]

    games = line.split(':')[1].split(';')
    for game in games:
      balls = [x.strip() for x in game.split(',')]
      ball_count = {
        "red": 0,
        "green": 0,
        "blue": 0
      }
      for ball in balls:
        values = ball.split(' ')
        count = values[0]
        color = values[1]
        ball_count[color] = ball_count[color] + int(count)
      for key in ball_count.keys():
        if ball_count[key] > max_balls[key]:
          all_games_valid = False

    if all_games_valid:
      sum = sum + int(id)

    print(f"{line} -> {id} -> {all_games_valid}")

  return sum
