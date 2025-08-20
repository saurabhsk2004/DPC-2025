def find_zero_sum_subarrays(arr):
    prefix_sum = 0
    hashmap = {}  # prefix_sum -> list of indices
    result = []

    for i, num in enumerate(arr):
        prefix_sum += num

        # Case 1: subarray starts from index 0
        if prefix_sum == 0:
            result.append((0, i))

        # Case 2: subarray found using previous same prefix sum
        if prefix_sum in hashmap:
            for start_index in hashmap[prefix_sum]:
                result.append((start_index + 1, i))

        # Add current index to hashmap
        hashmap.setdefault(prefix_sum, []).append(i)

    return result


# 🔹 Test Cases
print(find_zero_sum_subarrays([1, 2, -3, 3, -1, 2]))
# Expected: [(0, 2), (1, 3)]

print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1]))
# Expected: [(1, 2), (0, 3)]

print(find_zero_sum_subarrays([1, 2, 3, 4]))
# Expected: []

print(find_zero_sum_subarrays([0, 0, 0]))
# Expected: [(0,0), (0,1), (0,2), (1,1), (1,2), (2,2)]

print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0]))
# Expected: [(0, 3), (4, 4)]
