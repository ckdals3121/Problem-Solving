import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        temp = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, temp)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K :
            return -1
    return answer