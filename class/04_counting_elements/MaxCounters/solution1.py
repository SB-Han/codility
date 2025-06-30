def solution(N, A):
    counter = [0] * N
    stacked = temp_max = 0
    for each in A:
        if each < N + 1:
            index = each - 1
            if counter[index] < stacked:
                counter[index] = stacked
            counter[index] += 1
            temp_max = max(temp_max, counter[index])
        else:
            stacked = temp_max
    counter = [each if each > stacked else stacked for each in counter]
    return counter
