def reverse_list(vals):
    left = 0
    right = len(vals) - 1

    while left < right:
        vals[left], vals[right] = vals[right], vals[left]
        left += 1
        right -= 1
