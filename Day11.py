from itertools import permutations

def permute_unique(s: str, mode="backtrack"):
    """
    Generate all unique permutations of a string.
    mode = "backtrack" -> uses backtracking (efficient for duplicates)
    mode = "itertools" -> uses itertools.permutations (shorter but less efficient)
    """
    if mode == "backtrack":
        result = []
        used = [False] * len(s)
        chars = sorted(s)  # sort to handle duplicates

        def backtrack(path):
            if len(path) == len(chars):
                result.append("".join(path))
                return
            for i in range(len(chars)):
                if used[i]:
                    continue
                # skip duplicates
                if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(chars[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return result

    elif mode == "itertools":
        return list(set("".join(p) for p in permutations(s)))

    else:
        raise ValueError("Invalid mode! Use 'backtrack' or 'itertools'.")


# Test Cases
print("Backtracking:", permute_unique("abc", mode="backtrack"))
print("Itertools:", permute_unique("abc", mode="itertools"))

print("Backtracking:", permute_unique("aab", mode="backtrack"))
print("Itertools:", permute_unique("aab", mode="itertools"))

print("Backtracking:", permute_unique("aaa", mode="backtrack"))
print("Itertools:", permute_unique("aaa", mode="itertools"))

print("Backtracking:", permute_unique("a", mode="backtrack"))
print("Itertools:", permute_unique("a", mode="itertools"))
