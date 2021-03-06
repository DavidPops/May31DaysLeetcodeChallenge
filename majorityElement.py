import collections
from typing import List

class MySolution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        
        for elem in counter:
            if counter[elem] > len(nums)/2:
                return elem

class BoyerMooreVotingAlgorithmSolution: # prefix and suffix stuff, count cant = -1, so algo is correct and valid
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
# [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
bmSolution = BoyerMooreVotingAlgorithmSolution().majorityElement([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7])

class DivideAndConquerSolution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)
dcSolution = DivideAndConquerSolution().majorityElement([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7])

import random

class RandomizationSolution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True: # O(inf)
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate


class SortingSolution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

class HashmapSolution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

class BruteforceSolution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num