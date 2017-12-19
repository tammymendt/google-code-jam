import sys
from collections import namedtuple

Move = namedtuple('Move', ['move_index', 'button'])


class Robot:

    def __init__(self, name):
        self.name = name
        self.current_position = 1
        self.moves_left = []

    @property
    def next_move_index(self):
        return self.moves_left[0].move_index

    def push_button(self):
        current_move = self.moves_left[0]
        time = abs(current_move.button - self.current_position)
        self.current_position = current_move.button
        self.moves_left.pop(0)
        return time + 1

    def move(self, time):
        if self.moves_left:
            current_move = self.moves_left[0]
            if self.current_position >= current_move.button:
                self.current_position = max(
                    current_move.button, self.current_position - time)
            else:
                self.current_position = min(
                    current_move.button, self.current_position + time)


def init_robot_dict(input):

    robot_dict = {'O': Robot('O'), 'B': Robot('B')}

    input_array = input.split(' ')
    current_robot = input_array[0]
    index = 0
    for i in input_array:
        if i == 'O':
            current_robot = 'O'
        elif i == 'B':
            current_robot = 'B'
        else:
            robot_dict[current_robot].moves_left.append(Move(index, int(i)))
            index += 1

    return robot_dict


def solve_bot_trust(robot_dict):

    total_time = 0

    while robot_dict['O'].moves_left or robot_dict['B'].moves_left:

        if not robot_dict['O'].moves_left:
            pushing_robot = robot_dict['B']
            moving_robot = robot_dict['O']

        elif not robot_dict['B'].moves_left:
            pushing_robot = robot_dict['O']
            moving_robot = robot_dict['B']

        elif robot_dict['O'].next_move_index < robot_dict['B'].next_move_index:
            pushing_robot = robot_dict['O']
            moving_robot = robot_dict['B']

        elif robot_dict['B'].next_move_index < robot_dict['O'].next_move_index:
            pushing_robot = robot_dict['B']
            moving_robot = robot_dict['O']

        time = pushing_robot.push_button()
        moving_robot.move(time)
        total_time += time

    return total_time

if __name__ == "__main__":

    out_file = open(sys.argv[2],'w')
    in_file = open(sys.argv[1],'r')

    in_file.readline()
    case = 1
    for line in in_file:
        input = line.partition(' ')
        robots = init_robot_dict(line.partition(' ')[2])
        result = solve_bot_trust(robots)
        out_file.write('Case #%s: %s\n' % (str(case), str(result)))
        case += 1
