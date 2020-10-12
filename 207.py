class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        ind = collections.defaultdict(int)
        
        for u, v in prerequisites:
            g[v].append(u)
            ind[u] += 1
        for i in range(numCourses):
            zero = False
            for j in range(numCourses):
                if ind[j] == 0:
                    zero = True
                    break
            if not zero : return False
            ind[j] = -1
            for node in g[j]:
                ind[node] -= 1
        return True
