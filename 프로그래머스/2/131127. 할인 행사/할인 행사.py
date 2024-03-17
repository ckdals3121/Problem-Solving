from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9) :
        counter = Counter(discount[i: i + 10])
        if all(counter[want[j]] >= number[j] for j in range(len(want))) :
            answer += 1
    return answer