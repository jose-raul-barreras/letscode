# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 18:34:04 2017

@author: jrb
"""

def quartiles(X):
    X = sorted(X)
    if len(X)%2 == 0:
        Q1 = median( X[0:len(X)//2+1] )
        Q2 = (X[len(X)//2]+X[len(X)//2+1])/2
        Q3 = median( X[len(X)//2:])
        #print(X[0:len(X)//2], X[len(X)//2], X[len(X)//2:])
    else:
        L = X[0:len(X)//2]
        U = X[len(X)//2+1:]
        Q2 = X[len(X)//2]
        Q1 = median(L)
        Q3 = median(U )
        #print("*",L, Q2, U)
    return (int(Q1), int(Q2), int(Q3))


def median (X):
    """X most be sorted"""
    if len(X)%2 == 0:
        return (X[len(X)//2-1]+X[len(X)//2])/2
    else:
        return X[len(X)//2]

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#print(sorted(arr))
(q1, q2, q3) = quartiles(arr)
print(q1)
print(q2)
print(q3)