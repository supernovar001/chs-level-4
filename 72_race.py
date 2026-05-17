def solution(players, callings):
    # 추월발생한 순서가 반영되지 않았음!
    # 추월 이후 순위 반영 필요
    
    rank = {} # "사람이름" : 등수
    for i, play in enumerate(players):
        rank[play] = i
    print(rank)        
    
    for j, call in enumerate(callings):
        idx = rank[call] 
        rank[call] = idx-1 
        rank[callings[j-1]] =idx + 1
        players[idx-1], players[idx] = players[idx], players[idx-1] 
    print(rank)
    #return list(rank.keys())
    return players
                                #players                	callings                	result
print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))
#      (["mumu", "kai", "mine", "soe", "poe"]))

#{'mumu': 0, 'soe': 3, 'poe': 4, 'kai': 1, 'mine': 2}