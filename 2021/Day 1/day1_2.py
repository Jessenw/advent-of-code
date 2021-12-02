input = [int(line) for line in open('input.txt', 'r')]
sums = [sum(input[i: i + 3]) for i in range(len(input) - 2)] # -3 + 1 = -2
count = sum(sums[i] > sums[i - 1] for i in range(len(sums)))
print(count)