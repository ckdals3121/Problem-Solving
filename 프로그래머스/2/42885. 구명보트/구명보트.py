def solution(people, limit):
    answer = 0
    
    people.sort()
    left = 0
    right = len(people) - 1
    
    while left < right :
        if people[left] + people[right] > limit :
            right -= 1
        elif people[left] + people[right] <= limit :
            answer += 1
            left += 1
            right -= 1
    
    answer += (len(people) - 2 * answer)
        
    return answer