def solution(s):  
    last_s = {}
    count = 0
    
    for digit in s :
        if digit in last_s  :
            last_s[digit] += 1
            count += 1
            start = count   ### issue 
            
        else :
            last_s[digit] = 1
            print(last_s )
        
    sumdigit = 0
    for digit in s:
        if last_s[digit] > 1 :
            sumdigit += last_s[digit]
        return sumdigit - start 
    
print(solution("banana"))           #3
print(solution("abracadabra"))	    #6
print(solution("aaabbaccccabba"))	#3
