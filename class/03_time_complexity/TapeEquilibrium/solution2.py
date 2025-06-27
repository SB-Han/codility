def solution(A):
    suffix = sum(A[1:])
    prefix = A[0]
    current_min = abs(prefix - suffix)
    for each in A[1:len(A)-1]:
        prefix += each
        suffix -= each
        current = abs(prefix - suffix)
        if current < current_min:
            current_min = current
    return current_min
