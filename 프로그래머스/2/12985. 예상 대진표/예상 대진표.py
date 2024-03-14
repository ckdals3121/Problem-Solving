def solution(n,a,b):
    answer = 0

    if a > b :
        a, b = b, a
    
    while True :
        if b - a == 1 and b % 2 == 0 :
            answer += 1
            return answer
        else :
            a = (a + 1) // 2
            b = (b + 1) // 2
            answer += 1

    return answer