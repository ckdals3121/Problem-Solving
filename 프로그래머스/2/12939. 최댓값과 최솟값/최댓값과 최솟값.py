def solution(s):
    answer = ''
    ls = list(map(int, s.split()))

    answer += str(min(ls))
    answer += " "
    answer += str(max(ls))
    return answer