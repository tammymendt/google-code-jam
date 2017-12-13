import sys
from functools import reduce


def calculate_profit(rides, capacity, len_groups, group_array):

    # Easy solution for when the sum of all groups doesnt reach the capacity
    sum_of_groups = reduce(lambda x, y: x + y, group_array)

    if sum_of_groups <= capacity:
        return sum_of_groups * rides

    # Structure required to speed up computation for very large R
    profit_in_time_array = [(None, None) for i in range(0, len_groups)]
    profit_in_time_array[0] = (0, 0)

    current_index = 0
    profit = 0
    ride = 0

    while ride < rides:

        # Check if we've been on this index before to speed up computation
        past_profit, past_ride = profit_in_time_array[current_index]

        if past_ride is not None and past_ride < ride:
            rides_past = ride - past_ride
            profit_made = profit - past_profit
            j = int((rides - past_ride) / rides_past)
            if j > 0:
                ride = past_ride + rides_past * j
                profit = past_profit + profit_made * j
                if ride == rides:
                    break

        # Regular code that works for small values of R
        available_seats = capacity
        group_count = 0

        while True:
            if group_array[current_index] > available_seats or \
                            group_count == len_groups:
                break
            available_seats -= group_array[current_index]
            current_index = (current_index + 1) % len_groups
            group_count += 1

        profit += (capacity - available_seats)
        ride += 1

        # Data structure to speed up computation must be updated
        if profit_in_time_array[current_index][0] is None:
            profit_in_time_array[current_index] = (profit, ride)

    return profit


if __name__ == "__main__":

    in_file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[2], 'w+')

    cases = int(in_file.readline())

    for i in range(0, cases):
        meta_data = in_file.readline().split(' ')
        groups = list(map(int, in_file.readline().split(' ')))
        rides = int(meta_data[0])
        capacity = int(meta_data[1])
        len_groups = int(meta_data[2])

        result = calculate_profit(rides, capacity, len_groups, groups)
        out_file.write('Case #%s: %s\n' % (str(i + 1), str(result)))

