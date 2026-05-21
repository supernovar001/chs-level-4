def solution(n):
    #  0 1 1 2 3 5 8 13 21 34 
    if n == 0 :
        return 0
    elif n == 1 or n == 2 :
        return 1
    elif n > 2 :
        return (solution(n-1) + solution(n-2))%1234567

# run time error 