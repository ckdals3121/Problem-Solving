from collections import Counter
def solution(clothes):
    answer = 1
    temp = []
    
    for clothe in clothes :
        temp.append(clothe[1])
    
    counter = Counter(temp)

    for count in counter :
        answer *= counter[count] + 1
    
    return answer - 1