def get_sum(a, b):
    if a == b:
        return a
    elif a > b:
        a, b = b, a # swap the values of a and b
    return sum(range(a, b+1))