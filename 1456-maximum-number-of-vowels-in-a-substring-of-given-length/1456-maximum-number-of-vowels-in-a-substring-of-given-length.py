class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        substring = s[:k]
        curr_vowels = 0
        for sub in substring:
            if sub in vowels:
                curr_vowels += 1
        max_vowels = curr_vowels
        left = 1
        for right in range(k,len(s)):
            if s[right] in vowels:
                curr_vowels += 1
            if s[right-k] in vowels: # here i can not use left because edge cases where k  = 1 and left and right indices mean the same thing i will be decreasing without knowing

                curr_vowels -= 1
            left += 1
            max_vowels = max(max_vowels,curr_vowels)
        return max_vowels




        