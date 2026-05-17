def solution(id_list, report, k):
    
    explain = []    # explain
    reported_user_id_k = {}
    for r in report :
        userid = r.split()[0]
        reported_user_id_list = r.split()[1:]
        
        for rr in reported_user_id_list :
            explain_each = userid +"가 " +rr +"를 신고했습니다."
            explain.append(explain_each)
            print(userid, rr, explain_each, sep= "  |  ")
        
        # (로직 추가)신고자 - 피신고자 동일 case는 continue 해야함!!!
        if rr in reported_user_id_k:
            reported_user_id_k[rr] += 1    
        else :
            reported_user_id_k[rr] = 1
    # print(reported_user_id_k)
    
    # 정지된 사람 ?
    stopped_k = [x for x in reported_user_id_k if x >= k]
    print(stopped_k)
    
    # 정지된 사람을 신고한 사람에게 메일 발송
    
    # return : 정지
#               id_list	                             report	k	result
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))	#[2,1,1,0]
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))	#[0,0]


