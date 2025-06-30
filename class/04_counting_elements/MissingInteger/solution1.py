def solution(A):
    A = sorted(list(set([each for each in A if each > 0])))
    if len(A) == 0:
        return 1
    current = 1
    for each in A:
        if each == current:
            current += 1
        else:
            break
    return current
