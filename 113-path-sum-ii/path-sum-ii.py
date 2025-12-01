# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        final = []
        def checksum(root, target, summ):
            value = [root.val]
            val = root.val
            print(value, val, 'start')
            #set a list version to be appended to the final list, and a pure value version to be used for the subsequent statements.
            #above statement just returns once a leaf node is passed
            if not root:
                return
            #current value gives the sum - it must be a leaf node for the eventual result to be saved into the final list
            if val == target:
                print(val, value, 'equal')
                if not root.left and not root.right:
                    summ = summ + value
                    final.append(summ)

            summ = summ + value
            #iterating through the left and right nodes (if there is)
            if root.left:
                left = root.left
                checksum(left, target - val, summ)
            if root.right:
                right = root.right
                checksum(right, target - val, summ)
        
        checksum(root, targetSum, [])
        return final
            
        