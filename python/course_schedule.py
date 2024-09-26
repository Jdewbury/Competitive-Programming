class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}
        num_prereqs = [0] * numCourses

        for c, p in prerequisites:
            if p in courses:
                courses[p].append(c) 
            else:
                courses[p] = [c]
            num_prereqs[c] += 1
        
        # check for courses with no prereqs
        queue = [i for i in range(len(num_prereqs)) if num_prereqs[i] == 0]
        
        taken = 0
        while queue:
            curr = queue.pop(0)
            taken += 1
            if curr in courses:
                for neighbor in courses[curr]:
                    num_prereqs[neighbor] -= 1
                    if num_prereqs[neighbor] == 0:
                        queue.append(neighbor)
        
        return taken == numCourses