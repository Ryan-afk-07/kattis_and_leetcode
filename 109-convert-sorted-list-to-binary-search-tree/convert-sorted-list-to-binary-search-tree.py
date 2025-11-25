# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Do a 'quicksort' sort of thing, but in a binary tree format.
        Syntax is still quite similar, but now its performing root.left and root.right etc etc.
        """
        if not head:
            return head

        def listnodetolist(listnode):
            copy = listnode
            retrieved = []
            while copy:
                retrieved.append(copy.val)
                temp = copy.next
                copy = temp
            
            return retrieved
        
        sortedlist = listnodetolist(head)
        print(sortedlist)

        def quicksorttree(listi):
            if not listi:
                return None
            mid = len(listi)//2
            root = TreeNode(listi[mid])
            root.left = quicksorttree(listi[:mid])
            root.right = quicksorttree(listi[mid+1:])
            return root
        
        final = quicksorttree(sortedlist)
        return final
        