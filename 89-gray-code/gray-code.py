class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        A bit of bfs algorithm-ish thing.
        
        inclusive_rng = [i for i in range(2**n)]
        bit_rng = [bin(i)[2:] for i in range(2**n)]
        max_bit = max([len(bin(i)[2:]) for i in range(2**n)])
        up_bit_rng = ["0" * (max_bit - len(bin(i)[2:])) + bin(i)[2:] for i in range(2**n)]
        #print(up_bit_rng)
        gray_code = []
        def compare_bit(bit1, bit2):
            count = 0
            for i in range(len(bit1)):
                if bit1[i] == bit2[i]:
                    pass
                else:
                    count += 1
            
            if count > 1:
                return False
            else:
                return True
        
        def findloop(current_node, lis, lenn, final):
            #print(lis, current_node, lenn, final)
            #when the n-bit gray code sequence is full. All integers have been rightly fitted into the final list. Now we check if the last and first value will be able to form a loop (i.e. their binary numbers only HAVE ONE DIFFERING BIT)
            if lenn == len(inclusive_rng):
                first_val = "0" * (max_bit - len(bin(final[0])[2:])) + bin(final[0])[2:]
                last_val = "0" * (max_bit - len(bin(final[-1])[2:])) + bin(final[-1])[2:]
                if compare_bit(first_val, last_val) == True:
                    return final
                else:
                    return False
            #create a copy for mutatbility. If not the for loop will not be able to run at the first instance
            liss = lis.copy()
            liss.remove(current_node)
            #print(liss)
            current_bit = "0" * (max_bit - len(bin(current_node)[2:])) + bin(current_node)[2:]
            #print(current_bit)
            for i in liss:
                bit_i = "0" * (max_bit - len(bin(i)[2:])) + bin(i)[2:]
                if compare_bit(current_bit, bit_i) == True:
                    #this is to ensure that we get the utmost first legitimate value through a for loop of recursive func.
                    result = findloop(i, liss, lenn + 1, final + [i])
                    if result:
                        return result
            return False

        return findloop(0, inclusive_rng, 1, [0])
        """
        result = []
        total_numbers = 1 << n
        #total_numbers part understandable since doing 1 << n is essentially taking the 2^n value. As a left shift means a x2 formula

        for i in range(total_numbers):
            print(i, i>>1)
            """
            magic formula in which whenever a number is XOR-ed with its right shifted value, it will always return a result that is one bit off from the prev value.
            """
            result.append(i ^ (i >> 1))

        return result




        