# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None: return False
        parent_x, parent_y = None, None
        x_depth, y_depth, depth = 0, 0, 1
        working = queue.Queue()
        working.put([root])
        
        while not working.empty(): # not making the ! mistake
            if parent_x is not None and parent_y is not None: 
                return (x_depth == y_depth) and (parent_x != parent_y)
            current = working.get()
            nextNode = []
            
            for node in current:
                if (node.left and node.left.val == x) or (node.right and node.right.val == x): 
                    parent_x = node
                    x_depth = depth + 1
                if (node.left and node.left.val == y) or (node.right and node.right.val == y): 
                    parent_y = node
                    y_depth = depth + 1
                if node.left is not None: nextNode.append(node.left)
                if node.right is not None: nextNode.append(node.right)
            
            if len(nextNode) > 0: working.put(nextNode)
            depth += 1
        
        return False