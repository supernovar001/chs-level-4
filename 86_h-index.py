def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    # 6 5 3 1 0
    # 1 2 3 4 5 
    # 1 2 3 - -
    for i, citation in enumerate(citations):
        if citation >= i+1 :
            h_index = i+1
            print(citation, i+1)
        else :
            break
    
    return h_index