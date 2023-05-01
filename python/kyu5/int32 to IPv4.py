def int32_to_ip(int32):
    # Convert the integer to binary with 32 bits
    binary = '{0:032b}'.format(int32)
    # Split the binary into 4 octets of 8 bits each
    octets = [binary[i:i+8] for i in range(0, len(binary), 8)]
    # Convert each octet from binary to decimal
    decimals = [int(octet, 2) for octet in octets]
    # Join the decimals into a string with dots
    return '.'.join(str(decimal) for decimal in decimals)