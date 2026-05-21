def solution(n,a,b):
    count = 0
    while (a>0 and b>0):
        count +=1 
        if ((a+1)//2*2)+1 == ((b+1)//2*2)  :
            count +=1
            return count
        a = (a+1)//2
        b = (b+1)//2
# 2k 2k-1 : k번째 경기
# 4 7 cnt= 1
# 2 4 cnt =2
# 1 2 cnt= 3. <<< [1,2] 2k-1, 2k

print(solution(8,4,7))#3