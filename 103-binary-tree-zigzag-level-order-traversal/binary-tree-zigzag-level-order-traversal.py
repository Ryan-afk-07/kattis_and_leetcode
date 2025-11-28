# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        its a breadth first search for a binary tree. But how to do it, abit clueless.
        """
        if not root:
            return []
        final = [[root.val]]
        
        queue = [root]
        #stores the next layer of nodes.
        mid = []
        #stores the values of the next layer of nodes.
        mid_val = []
        ##while loop needs to be fine-tuned to go right to left after left to right
        direction = 0
        while queue:
            if direction == 0:
                for i in queue:
                    print(len(queue))
                    if i.right:
                        mid.append(i.right)
                        mid_val.append(i.right.val)
                    if i.left:
                        mid.append(i.left)
                        mid_val.append(i.left.val)
                    print(len(queue))
            else:
                for i in queue:
                    if i.left:
                        mid.append(i.left)
                        mid_val.append(i.left.val)
                    if i.right:
                        mid.append(i.right)
                        mid_val.append(i.right.val)
            final.append(mid_val)
            queue = list(reversed(mid))
            mid = []
            mid_val = []
            direction = 1 - direction

        return final[:-1]