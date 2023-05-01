def count(s):
    char_counts = {}
    for c in s:
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts
