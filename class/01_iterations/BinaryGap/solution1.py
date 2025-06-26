maximum = 31
def return_binary(N):
    binary = ''
    for i in range(maximum, -1, -1):
        criterion = 2 ** i
        if N >= criterion:
            binary += '1'
            N -= criterion
        else:
            binary += '0'
    return str(int(binary))

def solution(N):
    binary = return_binary(N)
    binary_gap = current_max = 0
    for each in binary:
        if each == '0':
            binary_gap += 1
        elif each == '1':
            if binary_gap > current_max:
                current_max = binary_gap
            binary_gap = 0
    return(current_max)
