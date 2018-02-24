# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:04:09 2017

@author: jrb
"""


def allLongestStrings(inputArray):
    """
    https://codefights.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
    Given an array of strings, return another array containing all of its longest strings.

    Example
    For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
    allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

    Input/Output
    [time limit] 4000ms (py3)
    [input] array.string inputArray

    A non-empty array.
    Constraints:
    1 ≤ inputArray.length ≤ 10,
    1 ≤ inputArray[i].length ≤ 10.

    [output] array.string

    Array of the longest strings, stored in the same order as in the inputArray.

    inputArray: ["aba",
 "aa",
 "ad",
 "vcd",
 "aba"]
Output:
Empty
Expected Output:
["aba",
 "vcd",
 "aba"]

 nput:
inputArray: ["aa"]
Output:
Empty
Expected Output:
["aa"]
Console Output:
Empty

nput:
inputArray: ["abc",
 "eeee",
 "abcd",
 "dcd"]
Output:
Empty
Expected Output:
["eeee",
 "abcd"]
    """
    res = []
    _max = 0
    for s in inputArray:
        if len(s) > _max:
            res = []
            res.append(s)
            _max = len(s)
        elif len(s) == _max:
            res.append(s)
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
