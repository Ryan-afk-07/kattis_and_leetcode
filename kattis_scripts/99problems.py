n = input()

#theory:
'''
1. if n < 99, automatically round up to 99
2. if n > 99 - multiple scenarios
2.1 if last 2 digits of n is < 49, round down
2.2 if last 2 digits of n is >= 50, round up
2.3 if last 2 digits of n IS == 49, round up.
'''




if int(n) <= 99:
    print(99)
else:
    tens = int(n[-2:])
    if tens < 49:
        print(int(n) - tens - 1)
    else:
        print(int(n) + (99 - tens))
