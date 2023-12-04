import re
import math

max_balls = {
  "red": 12,
  "green": 13,
  "blue": 14
}

def getSolution(input):
  sum = 0

  for line in input.splitlines():
    games = line.split(':')[1].split(';')
    max_ball_count = {
      "red": 0,
      "green": 0,
      "blue": 0,
    }
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
        if ball_count[key] > max_ball_count [key]:
          max_ball_count[key] = ball_count[key]

    power = max_ball_count["red"] * max_ball_count["green"] * max_ball_count["blue"]

    sum = sum + power
    print(f"{line} -> {power}")

  return sum
