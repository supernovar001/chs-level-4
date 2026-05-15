def solution(keymap, targets):
    press_count = {}
    
    for i, key in enumerate(keymap):
        for j, char in enumerate(key) :
            if char in press_count :    ###
            #if press_count[char].isempty() : error
               press_count[char] = min(j+1, press_count[char])
            else : 
                press_count[char] = j+1

    # step 2 : process each target string :
    result = []
    for target in targets :
        total_presses = 0 
        for char in target :
            if char in press_count :
                total_presses += press_count[char]
            else :
                total_presses = -1
                break
        result.append(total_presses)
    return result

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))	#[9, 4]
print(solution(["AA"],["B"]))	#[-1]
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]))	#[4, 6]