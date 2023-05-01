def find_short(s):
    # split the string into a list of words
    words = s.split()

    # find the length of each word
    lengths = [len(word) for word in words]

    # return the minimum length
    return min(lengths)