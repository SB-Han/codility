def solution(A):
    dict_form = {each: 0 for each in set(A)}
    for each in A:
        dict_form[each] += 1
    for k, v in dict_form.items():
        if v % 2 == 1:
            return k
