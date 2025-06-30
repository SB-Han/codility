def solution(X, A):
    check_list = set()
    for n, v in enumerate(A):
        check_list |= set([v])
        if len(check_list) == X:
            return n
    return -1
