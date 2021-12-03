import numpy as np
from collections import Counter

with open('input3', 'r') as f:
    values = [x for x in f.read().splitlines()]
    digits = []
    for value in values:
        tmp = [int(digit) for digit in str(value)]
        digits.append(tmp)

def rating(val):
    array = digits.copy()
    for i in range(12):
        count_values = Counter(arr[i] for arr in array)
        if val:
            value = 1 if count_values[1] >= count_values[0] else 0
            
        else:
            value = 0 if count_values[0] <= count_values[1] else 1
        for j, y in enumerate(digits):
            if len(array) == 1:
                break
            if y[i] != value:
                try:
                    array.remove(y)
                except:
                    continue

    ret = map(str, array[0])
    ret = ''.join(ret)
    return int(ret, 2)

def day3():
    # Part One
    ones = np.count_nonzero(digits, axis=0)
    zero = len(values) - ones
    gamma_arr = []
    epsilon_arr = []
    for i, x in enumerate(ones):
        if ones[i] >= zero[i]:
            gamma_arr.append('1')
            epsilon_arr.append('0')
        else:
            gamma_arr.append('0')
            epsilon_arr.append('1')
    gamma = ''.join(gamma_arr)
    epsilon = ''.join(epsilon_arr)
    print('Part one: ' + str(int(gamma, 2) * int(epsilon, 2)))

    #Part Two
    oxygen = rating(1)
    co2 = rating(0)
    print('Part two: ', str(oxygen * co2))

day3()