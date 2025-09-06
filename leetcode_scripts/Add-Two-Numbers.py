# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def rev_listnode(listnode):
            #setting initial parameters
            temp = listnode
            prev = None

            while temp != None:
                #setting the front variable to next so as to reverse the list
                front = temp.next
                #doing this allows the front now to be the back (which is None for the first)
                temp.next = prev
                #kind of creating a new prev variable that contains the new listnode but reversed
                prev = temp
                #kind of like reducing the temp variable to None
                temp = front
            

            return prev

        def extract_list(listnode):
            lis = []
            temp = listnode
            while temp != None:
                lis.append(str(temp.val))
                temp = temp.next
            return int("".join(lis))

        lis1rev = rev_listnode(l1)
        lis2rev = rev_listnode(l2)
        intlis1 = extract_list(lis1rev)
        intlis2 = extract_list(lis2rev)
        final_int = list(reversed(str(intlis1 + intlis2)))

        def insertTail(head, val):
            if head is None:
                return ListNode(int(val))
            temp = head
            while temp.next is not None:
                temp = temp.next

            new_node = ListNode(int(val))
            temp.next = new_node

            return head
        
        final = ListNode(int(final_int[0]))
        for i in range(1, len(final_int)):
            final = insertTail(final, final_int[i])



        return final

        

        