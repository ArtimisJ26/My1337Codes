class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i:[] for i in range(numCourses)}
        taken = set()
        res = True
        
        def makeAdjList():
            for crs, prereq in prerequisites:
                prereqMap[crs].append(prereq)
        
        def makeSchedule(course):
            if course in taken:
                return False
            if not prereqMap[course]:
                return True            
            
            taken.add(course)
            for neighbor in prereqMap[course]:
                if not makeSchedule(neighbor):
                    return False
            taken.remove(course)
            prereqMap[course] = []
  
            return True
        
        makeAdjList()
        for course in prereqMap:
            if course not in taken and prereqMap[course]:
                res = res and makeSchedule(course)
                
        return res