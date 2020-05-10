class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 1 ## Start at 1
        
        ## Apply Newton's Method for 20 iterations:
        for _ in range(20):
            x = 0.5 * (x + (num / x))
        
        ## Check if the result squares to give num
        if pow(round(x), 2) == num:
            return True
        
        return False
# Mr ITK solution. Newton aka Babylonian method. I took screenshot sha!!

import math
class MySolution: # inspired by the guy that said we can use .pow(0.5) instead.
    def isPerfectSquare(self, num: int) -> bool:
        root = math.pow(num, 0.5)
        
        if math.ceil(root) - math.floor(root) == 0: # this came to me on the spot as an alternative to using some epsilon check
            return True
        
        return False