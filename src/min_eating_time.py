def can_eat_all(piles, h, k):
    sorted(piles)
    hours = 0
    for pile in piles:
        hours += (pile + k - 1) // k
    return hours <= h


def min_eating_speed(piles, h):
    if h < len(piles):
        return f"The hours must be equal or greater then size of piles"
    sorted(piles)
    low = 1
    high = max(piles)
    while low <= high:
        mid = (low + high) // 2
        if can_eat_all(piles, h, mid):
            high = mid - 1
        else:
            low = mid + 1
    return low


print(min_eating_speed([10, 9, 27, 3, 17], 6))
