def solution(n, words):
    answer = []
    trash = []
    trash.append(words[0])
    
    for i in range(1, len(words)) :
        if words[i - 1][-1] != words[i][0] or words[i] in trash :
            answer.append((i + 1) % n)
            answer.append((i + 1) // n + 1)
            if answer[0] == 0 :
                answer[0] = n
                answer[1] -= 1
            return answer
        trash.append(words[i])

    
    answer.append(0)
    answer.append(0)
    return answer