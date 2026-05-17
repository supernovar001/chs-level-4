# From "20220519" To 
def day_calculator(date_str):
    year = int(date_str[:4])
    month = int(date_str[4:6])
    date = int(date_str[6:8])
    return year * 12 * 28 + month * 28 + date


def solution(today, terms, privacies):
    result = []
    # today를 숫자로 변경
    today_num = day_calculator(today.replace('.',''))

    term_month = {}
    for term in terms :
        alpha, month = term.split()
        term_month[alpha] = int(month)

    for i, p in enumerate(privacies) :
        pri_date = day_calculator(p[:10].replace('.',''))
        expired_date = pri_date + term_month[p[11]]*28

        if today_num >= expired_date :
            result.append(i+1)
    return result
                #today,          terms,              privacies)
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) #[1, 3]


