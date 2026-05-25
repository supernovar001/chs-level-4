def solution(arr1, arr2):
    print(arr1,'\n''\n''\n', arr2)
    
    sum_arr = [[]]
    for row in range(len(arr1)) :
        for y in range()
        for col in range(len(arr1[row])):
            for x in range(len(arr2)) :
                for y in range(len(arr2[x])) :
                   sum_arr[row][y] = arr1[row][col] * arr2[y][x]
    return sum_arr
print(solution([[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]]))	#[[15, 15], [15, 15], [15, 15]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))	#[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''
    a b     0,0 0,1
    c d     1,0 1,1
    e f     2,0 2,1
    
    A B     0,0 0,1
    C D     1,0 1,1
    
    aA+bC aB+bD
    cA+dC cB+dD
    eA+dC ce+fD
    

'''