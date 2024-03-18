global answer
answer = 0

def DFS(k, cnt, dungeons, check) :
    global answer
    
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)) :
        if check[i] == 0 and dungeons[i][0] <= k :
            check[i] = 1
            DFS(k - dungeons[i][1], cnt + 1, dungeons, check)
            check[i] = 0

def solution(k, dungeons):
    global answer
    
    check = [0 for _ in range(len(dungeons))]
    
    DFS(k, 0, dungeons, check)
    
    return answer