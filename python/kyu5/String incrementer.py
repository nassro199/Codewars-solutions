def increment_string(s):
    # Find the index of the last digit in the string
    i = len(s) - 1
    while i >= 0 and s[i].isdigit():
        i -= 1
    
    # Extract the string and the number parts
    prefix = s[:i+1]
    if i == len(s) - 1:
        number = 0
    else:
        number = int(s[i+1:])
    
    # Increment the number and format it with leading zeros
    number += 1
    num_digits = len(str(number))
    zeros = len(s) - i - num_digits - 1
    number_str = str(number).zfill(num_digits)
    
    # Combine the string and number parts
    return prefix + "0"*zeros + number_str