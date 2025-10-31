# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Initially thought need to do a hashmap. But since it is an ascending/sorted linked list, can just set a current linked list pointer that changes once a new value is seen, and removes all subsequent until a new node with new node value is seen or pointer has reached the end. I.e. node.next == None

        ##New solution:
        1. Create a new list of unique numbers (numbers that only show up once) after travesing the existing linkedlist
        2. From the retrieved list, create a new linkedlist with the unique numbers i guess.
        Might have better solutions but this is the best i could think with
        """
        #base case: No values in linkedlist
        if not head:
            return head
        
        def removeduplicate(linkedlist):
            if linkedlist.next is None:
                return []
            result = []
            curr_val = None
            count = 0
            move = linkedlist
            while move:
                #print(curr_val,move.val, count)
                if curr_val != move.val and count <= 1:
                    result.append(curr_val)
                    curr_val = move.val
                    count = 1
                    move = move.next
                elif curr_val == move.val:
                    count += 1
                    move = move.next
                else:
                    curr_val = move.val
                    count = 1
                    move = move.next
            #print(curr_val, count)
            #ensure last value is accounted if it is a unique value
            if count == 1:
                result.append(curr_val)
            res = result[1:]
            #making sure that the entire linkedlist is not the same value. I.e. [2,2,2,2,2]
            if count > 1 and res == []:
                return 'Error'
            return res

        to_convert = removeduplicate(head)
        #print(to_convert)
        ##Handles linkedlist with JUST ONE VALUE inside
        if to_convert == 'Error':
            return None
        
        #handles linkedlist with one unique value. Just return that value
        if not to_convert:
            return head

        #all other cases that are not the top
        final = curr = ListNode(to_convert[0])

        for i in range(1, len(to_convert)):
            new_node = ListNode(to_convert[i])
            curr.next = new_node
            curr = curr.next
            

        return final
                    

        