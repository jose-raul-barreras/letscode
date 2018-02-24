# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:04:09 2017

@author: jrb
"""


def matrixElementsSum(matrix):
    """
    https://codefights.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
    After becoming famous, CodeBots decided to move to a new building and live
    together. The building is represented by a rectangular matrix of rooms,
    each cell containing an integer - the price of the room. Some rooms are
    free (their cost is 0), but that's probably because they are haunted, so
    all the bots are afraid of them. That is why any room that is free or is
    located anywhere below a free room in the same column is not considered
    suitable for the bots.

    Help the bots calculate the total price of all the rooms that are suitable
    for them.

    Example
    matrix = [[0, 1, 1, 2],
              [0, 5, 0, 0],
              [2, 0, 3, 3]]
    the output should be matrixElementsSum(matrix) = 9.

    Here's the rooms matrix with unsuitable rooms marked with 'x':
    [[x, 1, 1, 2],
     [x, 5, x, x],
     [x, x, x, x]]
    Thus, the answer is 1 + 5 + 1 + 2 = 9.

    >>> matrix = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]
    >>> matrixElementsSum(matrix)
    9
    >>> matrix = [[1,1,1,0], [0,5,0,1], [2,1,3,10]]
    >>> matrixElementsSum(matrix)
    9
    >>> matrix = [[1,1,1], [2,2,2], [3,3,3]]
    >>> matrixElementsSum(matrix)
    18
    >>> matrix = [[0]]
    >>> matrixElementsSum(matrix)
    0

    """
    count = 0
    fact = [1 for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                fact[j] = 0
            count += matrix[i][j]*fact[j]
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
