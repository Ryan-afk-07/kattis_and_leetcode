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
            if not root:
                return
            if val == target:
                print(val, value, 'equal')
                if not root.left and not root.right:
                    summ = summ + value
                    final.append(summ)

            summ = summ + value
            if root.left:
                left = root.left
                checksum(left, target - val, summ)
            if root.right:
                right = root.right
                checksum(right, target - val, summ)
        
        checksum(root, targetSum, [])
        return final
            
        