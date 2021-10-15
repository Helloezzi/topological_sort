from collections import deque

num = 7
input = [[1, 2], [1, 5], [2, 3], [2, 6], [5, 6], [3, 4], [6, 4], [4, 7]]

def topology_sort():
    result = []
    q = deque()

    indegree = [0] * num

    # 진입 차수를 입력
    for i in input:
        temp = i[1] - 1
        indegree[temp] += 1

    for j in indegree:
        if j == 0:
            q.append(j)

    while q:
        now = q.popleft()
        result.append(now)        
        for i in input[now]:
            temp = i[1] - 1
            indegree[temp] -= 1
            
            if indegree[temp] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()