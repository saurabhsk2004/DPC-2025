def reverseWords(s: str) -> str:
    # Step 1: Split by spaces (split() handles multiple spaces automatically)
    words = s.split()
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
    
    # Step 3: Join them with a single space
    return " ".join(reversed_words)

print(reverseWords("the sky is blue"))      # "blue is sky the"
print(reverseWords("  hello world  "))      # "world hello"
print(reverseWords("a good   example"))     # "example good a"
print(reverseWords("    "))                 # ""
print(reverseWords("word"))                 # "word"
