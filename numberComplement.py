import math
class Solution:
    def findComplement(self, num: int) -> int:
        # binaryRep = bin(num)
        # flip = ~int(binaryRep, 2)
        # if num == 0: return 1
        # if num == 1: return 0
        if num & (num-1) == 0: return num - 1 # Knew this would come in handy
        
        flipper = (1 << math.ceil(math.log2(num))) - 1
        
        return flipper ^ num

solution = Solution()
solution.findComplement(0)
solution.findComplement(1)
solution.findComplement(5)
solution.findComplement(2)


def bitwiseComplement(self, N: int) -> int:
    if N == 0: 
        return 1
    else:
        return 2**(int(math.log2(N))+1)-1 - N

def bitwiseComplement2(self, N: int) -> int:
        # k bits = bit number necessary for num representation
        # Find first complement = biggest number that can be made with k bits - num
        bitNum = len(bin(N)[2:])
        return 2 ** bitNum - 1 - N