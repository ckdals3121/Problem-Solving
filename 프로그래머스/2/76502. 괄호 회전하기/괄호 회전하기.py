def is_good(s) :
    stack = []
    answer = {']': '[', ')': '(', '}': '{'}
    for i in range(len(s)) :
        if s[i] == '(' or s[i] == '{' or s[i] == '[' :
            stack.append(s[i])
        else :
            if len(stack) == 0 :
                return False
            elif answer[s[i]] == stack[-1] :
                stack.pop()
            else :
                return False
    
    if len(stack) == 0 :
        return True

def solution(s):
    answer = 0
    
    length = len(s)
    
    s = s + s
    print(s)
    
    for i in range(length) :
        temp = s[i: i + length]
        if is_good(temp) :
            answer += 1
            
    return answer