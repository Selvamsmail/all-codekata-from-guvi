def find_number_of_swaps(val):
    n = len(val)
    sortedval = list(enumerate(val))
    sortedval.sort(key = lambda x : x[1])
    visited = [False]*n
    
    swap = 0
    for i in range(n):
        if visited[i] or sortedval[i][0] == i:
            continue
    
        jumping = 0
        # what next 
        j = i 
        while not visited[j]:
            visited[j] = True
            # updated the visited. check for swaps.
            j = sortedval[j][0]
            jumping+=1
        if jumping > 1:
            swap +=1
    return swap 
        
n = int(input())
val = list(map(int,input().split()))
print(find_number_of_swaps(val))

# Sample Input :
# 5
# 1 5 4 3 2
# Sample Output :
# 2