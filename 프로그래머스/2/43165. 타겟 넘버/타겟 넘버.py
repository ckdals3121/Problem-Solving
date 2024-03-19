from itertools import combinations

def solution(numbers, target):
    answer = 0
    
    all_positive = sum(numbers)
    if (all_positive - target) % 2 != 0 :
        return 0
    negative = (all_positive - target) // 2
    
    if all_positive == target :
        return 1
    
    for i in range(1, len(numbers) + 1) :
        temps = list(combinations(numbers, i))
        
        for temp in temps :
            if sum(temp) == negative :
                answer += 1
    
    return answer