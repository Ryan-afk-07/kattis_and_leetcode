n = input()
line = input().split()
#changing the byte decimal to 8 bit binary
for i in range(int(n)):
    byte_string = bin(int(line[i]))[2:]
    byte_string_zero = byte_string.zfill(8)
    byte_string_rev = byte_string_zero[::-1]
    unscramble = [0]*8
    #doing a reverse XOL and shift (reverse based on understanding that right shift will ALWAYS have a new 0
    for i in range(len(byte_string_rev)):
        if byte_string_rev[i] == "0" and i == 0:
            unscramble[i] = 0
        elif byte_string_rev[i] == "1" and i == 0:
            unscramble[i] = 1
        elif byte_string_rev[i] == "0":
            unscramble[(i)] = unscramble[i-1]
        else:
            unscramble[i] = (1 - unscramble[i-1])
    answer = "".join(str(i) for i in unscramble[::-1])
    ans_bit = "0b" + answer
    print(int(ans_bit, 2), end = " ")    




            


                
            


