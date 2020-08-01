# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:03:59 2020

@author: Hp
"""

from isAnagram import is_anagram

def test_anagram():
    """Test Cases for Verifying Anagrams """
    assert is_anagram("", "") == True
    assert is_anagram("A", "A")  == True
    assert is_anagram("A", "B") == False
    assert is_anagram("ab", "ba")  == True
    assert is_anagram("AB", "ab")  == True
    

if __name__ == "__main__":
    test_anagram()
    print("Everything passed")