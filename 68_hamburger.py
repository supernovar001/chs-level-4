def solution(ingredient):
    pattern = [1,2,3,1]
    count = 0
    for i in range(len(ingredient)-4+1):
        if ingredient[:-4] == pattern :
            count +=1
            del ingredient[:-4]

        # finding [1,2,3],[1] or else
            
    return count
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))

2, 1, 1, 2, 3
[1,2,3,1]