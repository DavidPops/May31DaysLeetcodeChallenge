class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicts = collections.Counter(s)
        
        for index, char in enumerate(s):
            if dicts[char] == 1:
                return index
        
        return -1