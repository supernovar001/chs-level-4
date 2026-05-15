def solution(survey, choices):
    # -3, -2, -1, 0, 1, 2, 3 #매우비동의 ~ 매우동의
    # print(solution(["AN", "CF", "MJ", "RT", "NA"], [5,3,2,7,5]))
    # hash map
    personality_pairs = [("R","T"),("C","F"),("J","M"),("A","N")]
    score_value = {1:-3, 2:-2, 3:-1, 4:0, 5:1, 6:7}
    score_char = {}
    for x in survey :
        for pair in x :
            if pair in personality_pairs : 
            #if personality_pairs in personality : ###
            score += score_value[choices]
    
    return answer
    result = ''
print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))	#"TCMA"
print(solution(["TR", "RT", "TR"],[7,1,3]))	#"RCJA"