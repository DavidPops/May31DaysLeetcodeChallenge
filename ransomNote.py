from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # magCount = {k:v for } Dict comprehension one liner trick.
        magCount = Counter(magazine)
        
        for char in ransomNote:
            if char not in magCount: return False
            magCount[char] -= 1
            if magCount[char] < 0: return False
            
        return True

solution = Solution()
solution.canConstruct("a", "b")
solution.canConstruct("aa", "ab")
solution.canConstruct("aa", "aab")