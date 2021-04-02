from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    sum_list = [0 for i in range(len(stairway))]
    sum_list[0] = stairway[0]
    sum_list[1] = stairway[1]
    for i in range(2, len(stairway)):
        sum_list[i] = stairway[i] + min(sum_list[i - 1], sum_list[i - 2])
    return sum_list[-1]


if __name__ == '__main__':
    print(stairway_path(st))
