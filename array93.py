def isalternating(val,n):
    if not n > 1:
        return
    
    # find the initial direction.
    increasing = val[0] < val[1]
    
    for i in range(1, n-1):
        if increasing and val[i] < val[i+1]: # if teh current order needs to check for increase.
            return 'no'
        if not increasing and val[i] > val[i+1]: #if the current order is decreasing
            return 'no'
        increasing = not increasing
    return 'yes'

n = int(input())
a = list(map(int,input().split()))
print(isalternating(a,n)) 