h_pos = 0
depth = 0

commands = [line.split(' ') for line in open('input.txt', 'r')]
for c in commands:
    if c[0] == 'forward':
        h_pos += int(c[1])
    else:
        depth = depth + int(c[1]) if c[0] == 'down' else depth - int(c[1])

print(h_pos * depth)
