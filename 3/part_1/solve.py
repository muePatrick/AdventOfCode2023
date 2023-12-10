from solution import getSolution

if __name__ == '__main__':
  with open('input.txt', 'r') as input_file:
    input = input_file.read()
    solution = getSolution(input)
    print(solution)
