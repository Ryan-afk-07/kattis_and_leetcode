n, k = map(int, input().split())

r_sum = sum(int(input) for _ in range(k))
#setting conditions to find the min and maximum value for a specific range i presume?
if n > k:
    r_max = (r_sum + (n-k)*3)/n
    r_min = (r_sum + (n-k)*-3)/n
else:
    r_max = r_sum/n
    r_min = r_sum/n

    
print(r)

'''

Question requires us to provide an overall rating based on ratings from the judges.

'''
