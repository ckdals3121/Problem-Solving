import math

def solution(progresses, speeds):
    answer = []
    end_date = []
    
    for i in range(len(progresses)) :
        end_date.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    idx = 0    
    while idx < len(progresses) :
        temp = end_date[idx]
        end_date = [x - temp for x in end_date]
        print(end_date)
        cnt = 0
        while idx < len(progresses) and end_date[idx] <= 0 :
            cnt += 1
            idx += 1
        answer.append(cnt)
    return answer