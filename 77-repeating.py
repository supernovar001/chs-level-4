'''
s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 
이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록
solution 함수를 완성해주세요.
'''
def solution(s):
    # 이진 변환 횟수
    binary_cnt = 0
    # 변환 과정에서 제거된 0의 개수
    zero_cnt = 0
    
    while s != "1":
        x = '1' * s.count('1')
        zero_cnt += s.count('0')
        x_len = len(x)
        base = 2 
        result = ''

        while x_len > 0 :
            result = str(x_len % base) + result
            # print(x_len, result)
            x_len //= base
            # print(f"이진변환이전{s} 제거할 0의 수 {s.count('0')} 0제거후 길이{x_len} 이진변환 결과 : {result}")
            s = result  # 이진 변환의 결과
        binary_cnt += 1
    return [binary_cnt , zero_cnt]   
print(solution("110010101001")) # [3,8]
print(solution("01110")) # [3,3]
print(solution("1111111")) # [4,1]