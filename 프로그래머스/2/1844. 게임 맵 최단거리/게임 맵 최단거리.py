from queue import Queue

def solution(maps) :
    n = len(maps) - 1
    m = len(maps[0]) - 1
    
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    q = Queue()
    q.put((0, 0))
    visited[0][0] = True
    
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    while not q.empty() :
        y, x = q.get()
        for direction in directions :
            dx = x + direction[0]
            dy = y + direction[1]
            if 0 <= dx <= m and 0 <= dy <= n and maps[dy][dx] == 1 and not visited[dy][dx]:
                visited[dy][dx] = True
                q.put((dy, dx))
                maps[dy][dx] = maps[y][x] + 1
    
    if maps[n][m] == 1 :
        return -1
    
    return maps[n][m]
                