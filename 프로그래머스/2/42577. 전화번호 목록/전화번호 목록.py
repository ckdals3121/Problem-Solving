def solution(phone_book):
    answer = True
    hash = {}
    
    for number in phone_book :
        hash[number] = 1
    
    for number in phone_book :
        temp = ""
        for num in number :
            temp += num
            if temp in hash and temp != number :
                return False
            
    return answer