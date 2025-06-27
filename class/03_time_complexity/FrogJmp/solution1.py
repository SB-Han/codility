def solution(X, Y, D):
    if X == Y:
        return 0
    elif (Y - X) % D == 0:
        return (Y - X) // D 
    else:
        return 1 + (Y - X) // D
