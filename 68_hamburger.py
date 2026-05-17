def solution(ingredient):
    pattern = [ 1 , 2 , 3 , 1 ]
    stack = []  # to immedietely stack hamburger's ingredient
    count = 0   # the number of perfect hamburger

    for item in ingredient :
        stack.append(item)  # append ingredient order 

        # stack의 가장 최근 끝 4개원소가 [1,2,3,1]이면 햄버거를 만들고 stack에서 제거해야한다
        if stack[-4:] == pattern :  
            count +=1
            del stack[:-4]
    
    return count

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1])) # 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2])) # 0

# if you make hamburger, the [1,2,3,1] list became deleted 
# 1. stack 사용하는 이유  # stack.append(item)
    # 재료가 순서대로 들어와서 하나씩 보면서 쌓아야한다

    # [2, 1, "1, 2, 3, 1"] delete
    # [2, "1, 2, 3, 1"] delete
    # [2] last