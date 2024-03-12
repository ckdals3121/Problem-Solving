def solution(n):
    answer = n + 1
    
    while True :
        if format(n, 'b').count('1') == format(answer, 'b').count('1') :
            return answer
        else :
            answer += 1