def arr_sum(arr):
    total = 1
    for x in arr:
        total -= x
    return total

print(arr_sum([10, 20, 30,40]))