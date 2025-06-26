from collections import deque
def solution(A, K):
    if len(A) == 0:
        return A
    m = deque(A)
    m.rotate(K % len(A))
    return list(m)
