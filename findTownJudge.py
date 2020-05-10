from typing import List
class Solution: # passed 86/89
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = set()
        trusters = set()
        everyone = set()
        
        for a,b in trust: # started using some unpacking features
            everyone.add(a)
            everyone.add(b)
            if a != b:
                trusted.add(b)
                trusters.add(a)
                
        judge = everyone - trusters
        # judge = trusted - trusters
        if (len(judge)) == 0: return -1
        return judge.pop()

# discovered its a graph problem and also I did not discover a slight detail in the problem.

# https://leetcode.com/problems/find-the-town-judge/discuss/624269/JavaC%2B%2BPython3-or-With-Explanation-or-Single-array
class InspiredSolution: # borrows ideas from Boyer Moore
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusts = [0] * (N+1)
        for (a, b) in trust:
            trusts[a] -= 1
            trusts[b] += 1
            
        for i in range(1, len(trusts)):
            if trusts[i] == N-1:
                return i
        return -1