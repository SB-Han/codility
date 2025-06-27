def solution(X, Y, D):
    div, mod = divmod(Y-X, D)
    return div + int(bool(mod))
