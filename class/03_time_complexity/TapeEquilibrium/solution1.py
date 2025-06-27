def prefixsum(A):
    sums = [A[0]]
    for n in range(len(A)-1):
        sums.append(sums[n]+A[n+1])
    return sums

def suffixsum(A):
    sums = [A[-1]]
    for n in range(len(A) -1):
        sums.append(sums[n] + A[len(A) - 2 - n])
    return sums

def solution(A):
    ps, ss = prefixsum(A), suffixsum(A)
    diff = [ abs(ps[n] - ss[len(A) - 2 -n]) for n in range(len(A) - 1)]
    return min(diff)
