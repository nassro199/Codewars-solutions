def create_phone_number(n):
    area_code = "".join(str(x) for x in n[:3])
    first_three = "".join(str(x) for x in n[3:6])
    last_four = "".join(str(x) for x in n[6:])
    return f"({area_code}) {first_three}-{last_four}"