def phone_number(nums):
    book,n = {},0
    for s in nums:
        d = book
        for c in s:
            if c not in d:
                n, d[c] = n+1, {}
            d = d[c]
    return n