def solution(park, routes):    
    initial_point = [0,0]
    now_position = [0,0]
    route_default = {'E':[1,0],'W':[-1,0],'S':[0,-1],'N':[0,1]}
    #route = initial_point + route_plan[routes[0]]*int(routes[2]) 

    # park searching
    for w in range(len(park)):
        for n in range(len(park[w])):
            if park[w][n] == "S" :
                # 1. 시작 지점
                initial_point = [w,n]
    now_position[0] = initial_point[0]
    now_position[1] = initial_point[1]
    
    route_plan = {}
    for r in routes :
        direction, times = r.split()
        route_plan[direction] = int(times)           
        now_position[0] += route_default[direction] * route_plan[direction][0] 
        now_position[1] += route_default[direction] * route_plan[direction][1]  
        print(now_position)
    
    #     if now_position in "X" :        
    #             continue    # 장애물
    #     else :
    #         now_position  += route_default[routes[0]]*int(routes[2])
    # return now_position


#park	routes	result
print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))	#[2,1]
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))	#[0,1]
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))	#[0,0]

# 실행 결과 
'''
haesoocho@johaesuui-noteubug chs-level-4 % /usr/local/bin/python3 /Users/haesoocho/Documents/chs-level-4/73_in-the-park.p
y
[0, 0, 1, 0, 1, 0]
[0, 0, 1, 0, 1, 0, 0, -1, 0, -1]
[0, 0, 1, 0, 1, 0, 0, -1, 0, -1, -1, 0]
None
[0, 0, 1, 0, 1, 0]
[0, 0, 1, 0, 1, 0, 0, -1, 0, -1]
[0, 0, 1, 0, 1, 0, 0, -1, 0, -1, -1, 0]
None
[0, 1, 1, 0, 1, 0]
[0, 1, 1, 0, 1, 0, 0, -1, 0, -1, 0, -1]
[0, 1, 1, 0, 1, 0, 0, -1, 0, -1, 0, -1, -1, 0]
None
haesoocho@johaesuui-noteubug chs-level-4 % '''