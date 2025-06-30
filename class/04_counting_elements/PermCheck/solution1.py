def solution(A):
    length = len(set(A)) == len(A)
    maximum = max(A) == len(A)
    minimum = min(A) == 1
    if length and maximum and minimum:
        return 1
    else: return 0;
