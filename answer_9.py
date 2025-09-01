"""
 Write a function that accepts a word as a parameter
    and returns the number of vowels (a, e, i, o, u) in the word.
    Example: count_vowels("apple") → 2
"""
def  accepts_word(word):
    vowel = "aeiou"
    count = 0
    for char in word:
        if char in vowel:
            count += 1
    return count
        
    
    

word = input("Write a word that let me count the vowels: ").lower()
print(accepts_word(word))
