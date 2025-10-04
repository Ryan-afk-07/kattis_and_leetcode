# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        if k == 0:
            return head
        def countnodes(linkedlist):
            count = 0
            temp = linkedlist
            while temp:
                temp = temp.next
                count += 1
            return count
        
        length = countnodes(head)
        mod = k % length
        if mod == 0:
            return head
        if length == 1:
            return head
        remainder =length - (k % length)

        
        def split(times, linkedlist):
            curr = linkedlist
            new = None
            time = 0
            #split off
            while time < times:
                new_node = ListNode(curr.val)
                current = curr.next
                curr = current
                new_node.next = new
                new = new_node
                #print(curr, new)
                time += 1
            
            return curr, new

        def reversenode(linkedlist):
            curr = linkedlist
            prev = None
            while curr:
                #set a temp variable to be the next linkedlist node
                next_node = curr.next
                #set your current linkedlist to remove all behind values leaving just the first
                curr.next = prev
                #set your new returned linekdlist to add the new listnode in
                prev = curr
                #at the end make your current linkedlist to the next value perm
                curr = next_node
            return prev
        
        def addtwonodes(ll1, ll2):
            temp1 = ll1
            temp2 = ll2
            while temp1.next:
                temp1 = temp1.next
                print(temp1)
            temp1.next = temp2
            return ll1



        
        split1, split2 = split(remainder, head)
        rev2 = reversenode(split2)
        #print(split1, rev2)
        combine = addtwonodes(split1, rev2)
        return combine

            
                    


