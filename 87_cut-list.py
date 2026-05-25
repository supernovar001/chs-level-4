def solution(n, left, right):
    # 1
    arr = [[0]*n for _ in range(n)]
    # print(arr)
    
    # 2####
    for i in range(n):
        for j in range(i+1):
            arr[i][j] = i+1 
            arr[j][i] = i+1
    z = []
    # 3 nxn -> n*n  
    for i in range(n):
        z += arr[i]
    # print(z)
    
    # 4
    arr = z[left:right+1]
    return arr
    '''
    
 i=0   1 2 3 4      j=0
 i=1   2 2 3 4
 i=2   3 3 3 4
 i=3   4 4 4 4
    
    '''