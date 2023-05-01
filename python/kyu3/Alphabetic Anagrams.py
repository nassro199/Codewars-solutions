import math

def listPosition(word):
    if len(word) == 1:
        return 1

    unique_words = sorted(set(word))
    freq_letters = [word.count(letter) for letter in unique_words]

    total_combinations = math.factorial(len(word)) // math.prod([math.factorial(freq) for freq in freq_letters])

    increment = [0] + [freq * total_combinations // len(word) for freq in freq_letters[:-1]]
    increment = [sum(increment[:i + 1]) for i in range(len(increment))]

    return increment[unique_words.index(word[0])] + listPosition(word[1:])