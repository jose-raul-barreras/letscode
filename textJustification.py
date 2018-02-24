# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:04:09 2017

@author: jrb
"""
def justify(strings, L):
    res = []
    if len(strings) == 1:
        rest = L - sum([len(w) for w in strings[0]])
        res.append(' '.join(strings[0])+' ')
    else:
        for s in strings:
            rest = L - sum([len(w) for w in s])
            while rest > 0:
                if len(s) > 1:
                    for i in range(len(s)-1):
                        if rest > 0:
                            s[i] = s[i]+' '
                            rest -= 1
                        else:
                            break
                else:
                    s[0] += ' '*rest
                    rest = 0
            res.append(''.join(s))
    return res

def textJustification(words, L):
    """
    https://codefights.com/interview/ibANT8ZGc3shACBRF/description
    Given an array of words and a length L, format the text such that each
    line has exactly L characters and is fully justified on both the left and
    the right. Words should be packed in a greedy approach; that is, pack as
    many words as possible in each line. Add extra spaces when necessary so
    that each line has exactly L characters.

    Extra spaces between words should be distributed as evenly as possible. If
    the number of spaces on a line does not divide evenly between words, the
    empty slots on the left will be assigned more spaces than the slots on the
    right. For the last line of text and lines with one word only, the words
    should be left justified with no extra space inserted between them.

    Example
        For words = ["This", "is", "an", "example", "of", "text", "justification."]
        and L = 16, the output should be

        textJustification(words, L) = ["This    is    an",
                                       "example  of text",
                                       "justification.  "]

        >>> words = ["This", "is", "an", "example", "of", "text", "justification."]
        >>> L = 16
        >>> textJustification(words, L)
        ["This    is    an", "example  of text", "justification.  "]

        >>> words = ["Two", "words."]
        >>> L = 10
        >>> textJustification(words, L)
        ["Two words."]
    """

    res = []
    while words != []:
        s = []
        while len(s)+sum([len(w) for w in s])+len(words[0]) <= L:
            s.append(words[0])
            words = words[1:]
            if words == []:
                break
        res.append(s)
    print(res)
    return justify(res, L)

if __name__ == "__main__":
    words = ["Two", "words."]
    L = 10
    textJustification(words, L)

#    import doctest
#    doctest.testmod()
