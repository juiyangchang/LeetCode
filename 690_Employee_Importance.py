"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

from collections import deque

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        
        employee_dict = {emp.id: emp for emp in employees}
        res = 0
        queue = deque([id])
        
        while queue:
            current = queue.popleft()
            res += employee_dict[current].importance
            
            queue += employee_dict[current].subordinates
            
        return res