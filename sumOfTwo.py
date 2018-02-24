# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:51:58 2017

@author: jrb
"""


def sumOfTwo(a, b, v):
    """
    From https://codefights.com/i
    You have two integer arrays, a and b, and an integer target value v.
    Determine whether there is a pair of numbers, where one number is taken
    from a and the other from b, that can be added together to get a sum of v.
    Return true if such a pair exists, otherwise return false.

    Example
    For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
    sumOfTwo(a, b, v) = true.

    Input/Output
        [time limit] 4000ms (py3)
        [input] array.integer a
            An array of integers.

            Constraints:
            0 ≤ a.length ≤ 10^5,
            -10^9 ≤ a[i] ≤ 10^9.

        [input] array.integer b
            An array of integers.

            Constraints:
            0 ≤ b.length ≤ 10^5,
            -10^9 ≤ b[i] ≤ 10^9.

        [input] integer v
            Constraints:
            -10^9 ≤ v ≤ 10^9.

        [output] boolean
            true if there are two elements from a and b which add up to v,
            and false otherwise.

    >>> a = [1, 2, 3]
    >>> b = [10, 20, 30, 40]
    >>> v = 42
    >>> sumOfTwo(a, b, v)
    True
    >>> a = [1, 2, 3]
    >>> b = [10, 20, 30, 40]
    >>> v = 50
    >>> sumOfTwo(a, b, v)
    False
    >>> a = []
    >>> b = [1, 2, 3, 4]
    >>> v = 4
    >>> sumOfTwo(a, b, v)
    False
    >>> a = [10, 1, 5, 3, 8]
    >>> b = [100, 6, 3, 1, 5]
    >>> v = 4
    >>> sumOfTwo(a, b, v)
    True
    >>> a = [1, 4, 3, 6, 10, 1, 0, 1, 6, 5]
    >>> b = [9, 5, 6, 9, 0, 1, 2, 1, 6, 10]
    >>> v = 8
    >>> sumOfTwo(a, b, v)
    True
    >>> a = [3, 2, 3, 7, 5, 0, 3, 0, 4, 2]
    >>> b = [6, 8, 2, 9, 7, 10, 3, 8, 6, 0]
    >>> v = 2
    >>> sumOfTwo(a, b, v)
    True
    >>> a = [4, 6, 4, 2, 9, 6, 6, 2, 9, 2]
    >>> b = [3, 4, 5, 1, 4, 10, 9, 9, 6, 4]
    >>> v = 5
    >>> sumOfTwo(a, b, v)
    True
    >>> a = [6, 10, 25, 13, 20, 21, 11, 10, 18, 21]
    >>> b = [21, 10, 6, 0, 29, 25, 1, 17, 19, 25]
    >>> v = 37
    >>> sumOfTwo(a, b, v)
    True
    >>> a = [22, 26, 6, 22, 17, 11, 9, 22, 7, 12]
    >>> b = [14, 25, 22, 27, 22, 30, 6, 26, 30, 27]
    >>> v = 56
    >>> sumOfTwo(a, b, v)
    True
    """
    r = set([v-x for x in set(a)])
    return any(y in r for y in set(b))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
