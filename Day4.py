import math

def merge(arr1, arr2, m, n):
    total = m + n
    gap = math.ceil(total / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < total:
            # case 1: both pointers in arr1
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # case 2: i in arr1, j in arr2
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

            # case 3: both in arr2
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        if gap == 1:
            break
        gap = math.ceil(gap / 2)


# Example Usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merge(arr1, arr2, len(arr1), len(arr2))

print("arr1 =", arr1)
print("arr2 =", arr2)
