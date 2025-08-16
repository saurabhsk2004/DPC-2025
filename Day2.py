def find_missing_number(arr):
    n = len(arr) + 1   # since one number is missing
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

# Example
arr = [1, 2, 4, 5]
print("Missing Number:", find_missing_number(arr))
