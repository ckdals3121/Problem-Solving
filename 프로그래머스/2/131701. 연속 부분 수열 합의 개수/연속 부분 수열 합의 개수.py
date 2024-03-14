def solution(elements):
    values = set()
    
    elements = elements + elements
    
    for i in range(1, len(elements) // 2 + 1) :
        for j in range(len(elements) // 2) :
            values.add(sum(elements[j: j + i]))
            

    return len(values)