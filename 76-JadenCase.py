def solution(s):
    s_list = s.split(" ")
    z = []
    for x in s_list :
        z.append(x.capitalize())
        # z.append(x[0].upper()+x[1:].lower())
    return ' ' .join(z)

print(solution("3people unFollowed me"))	# "3people Unfollowed Me"
print(solution("for the last week"))	# "For The Last Week"
print(solution("for       the last week"))	
print(solution("  "))	
print(solution(""))	