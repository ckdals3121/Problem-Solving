def solution(s):
    answer = []
    stripped_str = s.strip('{}')
    set_strs = stripped_str.split('},{')
    sets_list = [set(map(int, s.split(','))) for s in set_strs]
    sorted_sets = sorted(sets_list, key = len)
    
    for sset in sorted_sets :
        temp = list(sset)
        
        for item in sset :
            if item not in answer :
                answer.append(item)
                break
    return answer