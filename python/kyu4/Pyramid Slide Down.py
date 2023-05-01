def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]

    last_layer = pyramid[-1]
    add_layer = []
    for i in range(1, len(last_layer)):
        add_layer.append(max(last_layer[i], last_layer[i-1]))
    
    pyramid[-2] = [a+b for a, b in zip(pyramid[-2], add_layer)]
    
    return longest_slide_down(pyramid[:-1])