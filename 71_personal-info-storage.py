def solution(today, terms, privacies):
    # day_calculator helper function 사용
    # 모든 달은 28일까지 있다고 가정합니다.
    # 이때 파기해야 할 개인정보의 번호를 오름차순으로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요
    #  유효기간이 지났다면 반드시 파기해야 합니다.
    # convert date  #2022.05.19 >> 20220519
    result = []
    # privacies
    for x in privacies:  
        # print(day_calculator(x[:10].replace('.','')))
        # find each month + privacy
        for y in terms :
            if x[11] in y : # "A"
                month = int(y[2:]) # "6"
                #print(month)
            if month*28 + day_calculator(x[:10].replace('.','')) < day_calculator(today.replace('.','')) :
                continue
            else :
                result.append(month*28 + day_calculator(x[:10].replace('.','')))
                print(result)
            
    return result.sort()
            
def day_calculator(date_str):   #20210101
    # converts a date (YYMMDD format) into a numerical value for comparison
    #print(f"{int(date_str[:4])} * 12 * 28 + {int(date_str[4:6])} * 28 + {int(date_str[6:8])}")
    year, month, day = int(date_str[:4]), int(date_str[4:6]), int(date_str[6:8])
    return year * 12 * 28 + month * 28 + day
    
                # today	terms	                    privacies	result
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) #[1, 3]