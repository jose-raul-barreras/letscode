# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:04:09 2017

@author: jrb
"""


def almostIncreasingSequence(sequence):
    """
    https://codefights.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
    Given a sequence of integers as an array, determine whether it is possible
    to obtain a strictly increasing sequence by removing no more than one
    element from the array.

    Example
    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false;

    There is no one element in this array that can be removed in order to get
    a strictly increasing sequence.

    For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.

    You can remove 3 from the array to get the strictly increasing sequence
    [1, 2]. Alternately, you can remove 2 to get the strictly increasing
    sequence [1, 3].

    Input/Output
        [time limit] 4000ms (py3)
        [input] array.integer sequence

        Constraints:
        2 ≤ sequence.length ≤ 105,
        -105 ≤ sequence[i] ≤ 105.

        [output] boolean
        Return true if it is possible to remove one element from the array in
        order to get a strictly increasing sequence, otherwise return false.

        >>> sequence = [1, 3, 2, 1]
        >>> almostIncreasingSequence(sequence)
        False
        >>> sequence = [1, 3, 2]
        >>> almostIncreasingSequence(sequence)
        True
        >>> sequence = [1, 2, 1, 2]
        >>> almostIncreasingSequence(sequence)
        False
        >>> sequence = [1, 4, 10, 4, 2]
        >>> almostIncreasingSequence(sequence)
        False
        >>> sequence = [10, 1, 2, 3, 4, 5]
        >>> almostIncreasingSequence(sequence)
        True
        >>> sequence = [1, 1, 1, 2, 3]
        >>> almostIncreasingSequence(sequence)
        False
        >>> sequence = [0, -2, 5, 6]
        >>> almostIncreasingSequence(sequence)
        True
        >>> sequence = [1, 2, 3, 4, 5, 3, 5, 6]
        >>> almostIncreasingSequence(sequence)
        False
        >>> sequence = [40, 50, 60, 10, 20, 30]
        >>> almostIncreasingSequence(sequence)
        False
        >>> sequence = [1, 1]
        >>> almostIncreasingSequence(sequence)
        True
        >>> sequence = [10, 1, 2, 3, 4, 5, 6, 1]
        >>> almostIncreasingSequence(sequence)
        False
        >>> sequence = [1, 2, 3, 4, 3, 6]
        >>> almostIncreasingSequence(sequence)
        True
        >>> sequence = [1, 2, 3, 4, 99, 5, 6]
        >>> almostIncreasingSequence(sequence)
        True
        >>> sequence = [1, 1, 2, 3, 3]
        >>> almostIncreasingSequence(sequence)
        False
        >>> sequence = [1,2,3,4,5,6,-9000]
        >>> almostIncreasingSequence(sequence)
        True
    """
    _min = -100000
    _max = 100000
    count = 0
    for i in range(len(sequence)):
        if sequence[i] <= _min or sequence[i] == _max:
            count += 1
        if i > 0 and (sequence[i] <= sequence[i-1]):
            _max = sequence[i-1]
            if i > 1:
                _min = sequence[i-2]
            count += 1

    if count <= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
