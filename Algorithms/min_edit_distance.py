# -*- coding: utf-8 -*-
import sys
REPLACE = 0
REMOVE = 1
INSERT = 2


def min_edit_distance(s1, s2):
    """
    This algorithm finds minimal edit distance between two
    sentence using dynamic programming.
    In this algorithm you can do three thing with every
    char in sentences:
    - Replace char from s1 to another char;
    - Remove char from s1;
    - Insert char into s1;
    :param s1: first sentence
    :param s2: second sentence
    :return: med -
    """
    len1 = len(s1)
    len2 = len(s2)

    # Init matrix
    m = [None] * (len1 + 1)
    op = [None] * (len1 + 1)
    for i in range(len1+1):
        m[i] = [0] * (len2+1)
        op[i] = [-1] * (len2+1)

    # Init horizontal and vertical axis value in matrix
    for j in range(1, len2+1):
        m[0][j] = j
    for i in range(1, len1+1):
        m[i][0] = i

    # Find best values
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            cost = 1

            if s1[i-1] == s2[j-1]: cost = 0
            replaceCost = m[i-1][j-1] + cost
            removeCost = m[i-1][j] + 1
            insertCost = m[i][j-1] + 1
            cost = (replaceCost, removeCost, insertCost)
            m[i][j] = min(cost)
            op[i][j] = cost.index(m[i][j])

    ops = []
    i = len1
    j = len2
    while i != 0 or j != 0:
        if op[i][j] == REMOVE or j == 0:
            ops.append('Remove {0} char {1} of {2}'.format(i, s1[i-1], s1))
            i -= 1
        if op[i][j] == INSERT or i == 0:
            ops.append('Insert {0} char {1} of {2}'.format(j, s2[j - 1], s2))
            j -= 1
        else:
            if m[i-1][j-1] < m[i][j]:
                fmt = 'Replace {0} char of {1} ({2}) with {3}'
                ops.append(fmt.format(i, s1, s1[i-1], s2[j-1]))
            i, j = i-1, j-1
    return m[len1][len2], ops


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        s1 = input('Input first sentence s1: ')
        s2 = input('Input second sentence s2: ')
    if len(sys.argv) == 3 and \
            isinstance(sys.argv[1], str) and isinstance(sys.argv[2], str):
        s1, s2 = tuple(sys.argv[1:])
    else:
        raise ValueError("Wrong types of in input args. They have to bee a string.")
    med = min_edit_distance(s1, s2)
    print('*+*' * 11)
    print('NUMBER OF OPERATION: {0}\n'.format(med[0]))
    print(",\n".join(med[1]))
    print('*+*' * 11)

