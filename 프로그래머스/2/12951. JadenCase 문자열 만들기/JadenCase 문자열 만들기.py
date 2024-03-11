def solution(s):
    answer = ''
    idx = 0
    while idx < len(s) :
        if s[idx].isalnum() :
            if s[idx].isalpha() :
                answer += s[idx].upper()
            else :
                answer += s[idx]
            idx += 1
            while idx < len(s) and s[idx].isalnum() :
                answer += s[idx].lower()
                idx += 1
        else :
            answer += s[idx]
            idx += 1
            
    return answer