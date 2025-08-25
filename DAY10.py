from collections import defaultdict

def groupAnagrams_sorting(strs):
    """Solution 1: Using sorted string as key"""
    groups = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))  # sorting
        groups[key].append(word)
    return list(groups.values())


def groupAnagrams_counting(strs):
    """Solution 2: Using character count tuple as key"""
    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26  # for 26 lowercase letters
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(word)  # tuple is hashable
    return list(groups.values())


# ✅ Test both solutions
if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "bca", "cab", "xyz", "zyx", "yxz"],
        ["abc", "def", "ghi"]
    ]

    for strs in test_cases:
        print("Input:", strs)
        print("By Sorting:", groupAnagrams_sorting(strs))
        print("By Counting:", groupAnagrams_counting(strs))
        print("-" * 50)
