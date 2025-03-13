class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]

        for [a,b] in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        que = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                que.append(i)
        
        result = 0
        while que:
            node = que.popleft()
            result+=1

            for a in graph[node]:
                indegree[a]-=1
                if indegree[a]==0:
                    que.append(a)
                
        return result == numCourses