def solution(A, K):
    if len(A) == 0:
        return A
    for i in range(len(A) - K % len(A)):
        A.append(A.pop(0))
    return A
