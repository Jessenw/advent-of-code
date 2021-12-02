input = [int(line) for line in open('input.txt', 'r')]
count = sum(input[i] > input[i - 1] for i in range(len(input)))
print(count)