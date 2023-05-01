def get_pins(observed):
    combos = []
    neighbors = {
        "0": ["8"],
        "1": ["2", "4"],
        "2": ["1", "3", "5"],
        "3": ["2", "6"],
        "4": ["1", "5", "7"],
        "5": ["2", "4", "6", "8"],
        "6": ["3", "5", "9"],
        "7": ["4", "8"],
        "8": ["5", "7", "9", "0"],
        "9": ["6", "8"]
    }
    str_digits = str(observed)

    def get_combos(digits, idx, cur_combo):
        cur_digit = digits[idx]
        candidates = set(neighbors[cur_digit])
        candidates.add(cur_digit)

        def reached_end(candidate):
            combos.append(cur_combo + candidate)

        def go_deeper(candidate):
            get_combos(digits, idx + 1, cur_combo + candidate)

        [reached_end(candidate) if idx == len(digits) - 1 else go_deeper(candidate) for candidate in candidates]

    get_combos(str_digits, 0, "")
    return combos