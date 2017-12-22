import sys


def solve_bot_trust(input_array):

    position_dict = {'O': 1, 'B':  1}
    time_since_last_push = {'O': 0, 'B': 0}

    time = 0

    for i in input_array[1:]:
        if i == 'O':
            pushing_bot = 'O'
            moving_bot = 'B'
        elif i == 'B':
            pushing_bot = 'B'
            moving_bot = 'O'
        else:
            pushing_bot_position = position_dict[pushing_bot]
            new_position = int(i)

            if time_since_last_push[pushing_bot] > 0:
                position_dict[pushing_bot] = calculate_position_after_move(
                    pushing_bot_position, new_position, time_since_last_push[pushing_bot]
                )

            time_taken = abs(new_position - position_dict[pushing_bot]) + 1
            position_dict[pushing_bot] = new_position
            time_since_last_push[pushing_bot] = 0
            time_since_last_push[moving_bot] += time_taken
            time += time_taken

    return time


def calculate_position_after_move(current_position, destiny_position, time):

    if current_position >= destiny_position:
        return max(destiny_position, current_position - time)
    else:
        return min(destiny_position, current_position + time)


if __name__ == "__main__":

    out_file = open(sys.argv[2],'w')
    in_file = open(sys.argv[1],'r')

    in_file.readline()
    case = 1
    for line in in_file:
        result = solve_bot_trust(line.split(' '))
        out_file.write('Case #%s: %s\n' % (str(case), str(result)))
        case += 1