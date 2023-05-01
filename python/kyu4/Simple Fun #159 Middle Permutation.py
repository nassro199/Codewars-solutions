def middle_permutation(string):
    string = list(string)
    string.sort(reverse = True)
    string = "".join(string)
    safe, p, l = (len(string)-2)//2, 1 if len(string)%2 == 0 else 2, len(string)
    return "".join([string[x] for x in range(-safe-p,-safe)]) + "".join([string[x] for x in range(0,l-safe-p)]) + "".join([string[x] for x in range(l-safe,l) if safe != 0])