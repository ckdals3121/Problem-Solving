def solution(citations):
    answer = 0
    
    citations.sort()
    
    for i in range(len(citations)) :
        H = len(citations) - i
        
        if citations[i] >= H :
            return H
    
    return answer