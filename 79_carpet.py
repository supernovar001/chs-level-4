def solution(brown, yellow):
    width, height = 0, 0
    for i in range(1, brown*yellow):
        if i*((brown + yellow-4)//2  - i) == brown*yellow :
            print(i)
            width = i
    # print(f"brown= {brown}, yellow = {yellow}, width ={width}")
    height = (brown + yellow-4)//2 - width
    return [width, height]
    
    # brown 가로*세로 - (가로-2)*(세로-2)
    # brown =  +2가로 + 2세로 - 4
    # yellow = (가로-2)*(세로-2) = 가로*세로 - 2가로 -2 세로 -4
    # brown + yellow = 가로*세로
    # 가로+세로 = (brown+yellow-4)//2
    
print(solution(10,2))#4.3
print(solution(8,1))#3.3