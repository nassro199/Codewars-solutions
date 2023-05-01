from itertools import combinations

def choose_best_sum(t, k, ls):
    best_sum = -1
    for distances in combinations(ls, k):
        sum_distances = sum(distances)
        if sum_distances <= t and sum_distances > best_sum:
            best_sum = sum_distances
    return best_sum if best_sum >= 0 else None