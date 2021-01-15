class Employee:
    empCount = 0

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee:", Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, ",Salary:", self.salary, "Department:", self.department)


emp = Employee("Anna", 10000, "sales")
emp.displayEmployee()
