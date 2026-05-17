def solution(s):
    s_list = list(map(int,s.split()))
    print(s_list)
    return str(min(s_list))+" "+str(max(s_list))

print(solution("1 2 3 4"))      # "1 4"
print(solution("-1 -2 -3 -4"))  # "-4 -1"
print(solution("-1 -1"))      # "-1 -1"