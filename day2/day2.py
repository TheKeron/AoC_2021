with open('input2', 'r') as f:
    values = [x for x in (x.split(" ") for x in f.read().splitlines())]

def day2():
    h = 0
    d = 0
    aim = 0
    for x in values:
        if x[0] == 'forward':
            h += int(x[1])
            d += (aim * int(x[1]))
        elif x[0] == 'down':
            aim += int(x[1])
        elif x[0] == 'up':
            aim -= int(x[1])
    print(h*d)

day2()

