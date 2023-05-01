def rgb(r, g, b):
    # Round values outside of 0-255 range to nearest valid value
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))
    
    # Convert to hexadecimal string and pad with zeroes if needed
    return '{:02X}{:02X}{:02X}'.format(r, g, b)