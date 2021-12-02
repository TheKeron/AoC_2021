with open('input2', 'r') as f:
    values = [x for x in f.read().splitlines()]

def day2():
    h = 0
    d = 0
    aim = 0
    for x in values:
        split = x.split(' ')
        if split[0] == 'forward':
            h += int(split[1])
            d += (aim * int(split[1]))
        elif split[0] == 'down':
            aim += int(split[1])
        elif split[0] == 'up':
            aim -= int(split[1])
    print(h*d)

day2()