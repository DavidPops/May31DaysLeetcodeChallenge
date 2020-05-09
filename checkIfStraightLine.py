from typing import List
class Solution: # passed 34/66 test cases
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates) < 2): return False
        if len(coordinates) == 2: return True # got this without the hint
        
        for i in range(1, len(coordinates) - 1):
            x_cord = coordinates[i][0]
            y_cord = coordinates[i][1]
            next_x = coordinates[i+1][0]
            next_y = coordinates[i+1][1]
            prev_x = coordinates[i-1][0]
            prev_y = coordinates[i-1][1]
            if (abs(next_x - x_cord) != abs(x_cord - prev_x) or abs(next_y - y_cord) != abs(y_cord - prev_y)):
                return False
            
        return True

#   Hide Hint #3
# Use cross product to check collinearity.

# [[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]] basically a horizontal line. so hint 3 and hint 2 would have to do it.

# trying hint 2 first

class Hint2Solution: # passed 6/66 y=mx+c passed 4/66 y=mx
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates) < 2): return False
        if len(coordinates) == 2: return True
        
        # m = (coordinates[1][1] - coordinates[0][1]) - (coordinates[1][0] - coordinates[0][0]) # put - instead of /
        m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) # guessing float problems.
        print(m) # gives 0 for horizontal line y = mx + c ??
        
        for i in range(1, len(coordinates) - 1):
            if (coordinates[i][1] != (m * coordinates[i][0] + coordinates[i][1])): # trailing brackets. Stop forgeting
                return False
                
        return True

class Hint2SolutionV2: # passed 5/66
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates) < 2): return False
        if len(coordinates) == 2: return True
        
        # m = (coordinates[1][1] - coordinates[0][1]) - (coordinates[1][0] - coordinates[0][0]) # put - instead of /
        m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) # guessing float problems.
        print(m) # gives 0 for horizontal line
        
        for i in range(1, len(coordinates)):
            newM = (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0])
            if newM != m: return False # Shouldn't I use epsilon check?
                
        return True

# Division by zero problems. Only solved it in for loop initially. Forgot to correct the problem in initial assignment for value 'm's

class AcceptedSolution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (len(coordinates) < 2): return False
        if len(coordinates) == 2: return True
        
        # m = (coordinates[1][1] - coordinates[0][1]) - (coordinates[1][0] - coordinates[0][0]) # put - instead of /
        m = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) if (coordinates[1][0] - coordinates[0][0]) != 0 else float('inf') # guessing float problems.
        print(m) # gives 0 for horizontal line
        
        for i in range(1, len(coordinates)):
            newM = (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]) if (coordinates[i][0] - coordinates[i-1][0]) != 0 else float('inf')
            if newM != m: return False # Shouldn't I use epsilon check?
                
        return True

# lemme check for collinearity solution

# Just a shortcut for assignment in the python3 solution:
# (x1, y1), (x2, y2) = coordinates[:2]

# So basically at any point of time, any three coordinate should satisfy following condition to be colinear.
# (y2 - y1)(x3 - x1) == (x2 - x1)(y3 - y1)

class DiscussSolution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True

# Great job. I liked the way you avoided division by not having to compute slope. This certainly made code simpler.
# Just one more shortcut for python3 solution:
# for (x,y) in coordinates[2:]: