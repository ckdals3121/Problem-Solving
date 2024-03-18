def solution(cacheSize, cities):
    answer = 0
    cache = []
    LRU = [0 for _ in range(cacheSize)] 
    
    if cacheSize == 0 :
        return 5 * len(cities)
    
    for i in range(len(cities)) :
        cities[i] = cities[i].lower()
    
    for idx, city in enumerate(cities) :
        if city in cache :
            answer += 1
            LRU[cache.index(city)] = idx
        else :
            if len(cache) < cacheSize :
                answer += 5
                cache.append(city)
                LRU[cache.index(city)] = idx
            else :
                answer += 5
                index = LRU.index(min(LRU))
                cache[index] = city
                LRU[index] = idx
                
    return answer