def queue_time(customers, n):
    tills = [0] * n
    for customer in customers:
        tills[tills.index(min(tills))] += customer
    return max(tills)