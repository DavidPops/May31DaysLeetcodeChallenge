class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        setJ = set(J)
        count = 0
        
        for char in S:
            if char in setJ: count += 1
                
        return count

    def numJewelsInStonesBitManipulation(self, J: str, S: str) -> int:
        """ O(n + m) time complexity, O(1) space complexity (using only 2 variables)"""
        count = 0
        bitfield = 0
        
        # Using bits in @bitfield as an array of boolean values
        # First loop sets bits from @J
        for c in J:
            idx = ord(c) - 65
            bitfield |= (1 << idx)
            
        # Second loop checks if the bit is set, if it is then increment the counter
        for c in S:
            idx = ord(c) - 65
            if (bitfield & (1 << idx)):
                count += 1
                
        return count

solution = Solution()
solution.numJewelsInStones("aA", "aAAbbbb")