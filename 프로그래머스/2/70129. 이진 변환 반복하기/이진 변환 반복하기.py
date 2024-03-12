def solution(s):
    answer = [0 for _ in range(2)]
    
    while len(s) != 1 :
        answer[1] += s.count('0')
        
        s = format(s.count('1'), 'b')
        answer[0] += 1
    
    return answer