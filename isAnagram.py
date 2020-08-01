def is_anagram(input1, input2):
    """Check if two functions are anagrams of each other."""
    return sorted(input1.upper()) == sorted(input2.upper())