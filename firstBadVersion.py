# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1: return n
        while n > 0:
            if isBadVersion(n) and not isBadVersion(n - 1): return n # Seems 10^7 is max loop iterations online Judge can handle. We need binary search
            n -= 1
        # if n == 1: return n
        # for i in range(n, 0):
        #     if not isBadVersion(i) and isBadVersion(i + 1): This was much simpler and straightforward
        #         return i + 1
#         foundBad = False
        
#         if n == 1: return n
        
#         while n > 0:
#             if (foundBad and not isBadVersion(n)): return n + 1
#             if (isBadVersion(n)): foundBad = True
            # n -= 1
    
    def firstBadVersionBinarySearch(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = n // 2
        start = 1
        end = n
        if n == 1: return n # Special case, coz mid would be 0 off the bat
        
        while (start <= end): # Can cause infinite loop use < instead of <=
            print(start, end, mid) # Gives output limit exceeded.
            if isBadVersion(mid) and isBadVersion(mid + 1):
                end = mid
                mid = ((end - start) // 2) + start # think of minMaxScaler. Beans Cooker(start - end)?? 💀
            if not isBadVersion(mid) and not isBadVersion(mid + 1):
                start = mid
                mid = ((end - start) // 2) + start
            if not isBadVersion(mid) and isBadVersion(mid + 1):
                return mid + 1
            if not isBadVersion(mid - 1) and isBadVersion(mid):
                return mid