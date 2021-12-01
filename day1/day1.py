with open('input1', 'r') as f:
    num = [int(x) for x in f.read().splitlines()]


def day1():

    sum_list = []
    for i, x in enumerate(num):
        try:
            sum_list.append(num[i] + num[i+1] + num[i+2])
        except IndexError:
            pass

    count = 0
    for i, x in enumerate(sum_list):
        if i == 0:
            continue

        if x > sum_list[i-1]:
            count += 1
        
    print(count)


day1()