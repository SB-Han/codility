def solution(A):
    N = len(A)
    length = len(set(A)) == N
    one_to_N = sum(A) == N * (N+1) / 2
    if length and one_to_N:
        return 1
    else: 
    	return 0
