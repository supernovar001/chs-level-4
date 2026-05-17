def solution(keymap, targets):
    press_count = {}
    # check key map
    for i, key in enumerate(keymap):
        for j, char in enumerate(key) :
            if char in press_count :
                press_count[char] = min(j+1, press_count[char])
            else :
                press_count[char] = j+1
    
    result = []
    
    for i, target in enumerate(targets):
        total_press_count = 0
        for j , char in enumerate(target):
            if char in press_count :
                total_press_count += press_count[char]
                
            else: 
                total_press_count = -1
        result.append(total_press_count)
    return result 

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))	#[9, 4]
print(solution(["AA"],["B"]))	#[-1]
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]))	#[4, 6]