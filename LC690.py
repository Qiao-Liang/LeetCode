# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.res = 0

        def recurse(employees, id):
            for employee in employees:
                if employee[0] == id:
                    self.res += employee[1]

                    if employee[2]:
                        for sub_id in employee[2]:
                            recurse(employees, sub_id)

        recurse(employees, id)

        return self.res


sol = Solution()
employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
id = 1
print sol.getImportance(employees, id)
