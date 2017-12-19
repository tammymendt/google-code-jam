import sys
from fractions import math
from functools import reduce


def solve_apocalypse(input_array):

    t_array = []
    for i in range(0, len(input_array)):
        for j in range(i + 1, len(input_array)):
            t = abs(input_array[i] - input_array[j])
            if t != 0:
                t_array.append(t)

    T = reduce(lambda x, y: math.gcd(x, y), t_array)

    if input_array[0] % T == 0:
        return 0

    return T - (input_array[0] % T)


if __name__ == "__main__":

    out_file = open(sys.argv[2],'w')
    in_file = open(sys.argv[1],'r')
    in_file.readline()
    case = 1
    for line in in_file:
        input = line.split(' ')
        n = int(line[0])
        result = solve_apocalypse(list(map(int, input[1:])))
        out_file.write('Case #%s: %s\n' % (str(case), str(result)))
        case += 1
