from functools import reduce
def solution(A):
    return reduce(lambda x,y: x^y, A)
