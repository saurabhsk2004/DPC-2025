def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Take first string as reference
    prefix = strs[0]

    for s in strs[1:]:
        # Reduce prefix until it matches start of string s
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


# Example usage
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))  # Output: "fl"
