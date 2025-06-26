def solution(N):
    return len(max(bin(N).lstrip('0b').strip('0').strip('1').split('1')))
