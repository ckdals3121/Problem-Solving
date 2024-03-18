from queue import Queue

def solution(priorities, location):
    answer = 0
    
    q = Queue()
    
    for i in range(len(priorities)) :
        q.put(i)
    
    while True :
        process = q.get()
        if priorities[process] == max(priorities) :
            answer += 1
            priorities[process] = 0
            if process == location :
                return answer
        else :
            q.put(process)
            
    return answer