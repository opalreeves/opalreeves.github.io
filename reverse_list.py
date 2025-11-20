def reverse_list(vals):
    left = 0
    right = len(vals) - 1

    while left < right:
        vals[left], vals[right] = vals[right], vals[left]
        left += 1
        right -= 1

# vals = [7, -3, 12, 9]
# reverse_list(vals)
# print(vals)  # This should print [9, 12, -3, 7]