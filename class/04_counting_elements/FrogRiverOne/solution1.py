def solution(X, A):
    test_list = [0] * X
    tag = 0
    for n, each in enumerate(A):
        if test_list[each-1] == 0:
            test_list[each-1] = 1
            tag += 1
        if tag == X:
            return n
    return -1
