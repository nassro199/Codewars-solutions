def duplicate_encode(word):
    # Convert the word to lowercase
    word = word.lower()
    # Create a dictionary to store the count of each character in the word
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Use a list comprehension to create the encoded string
    encoded_str = "".join(["(" if char_count[char] == 1 else ")" for char in word])
    return encoded_str