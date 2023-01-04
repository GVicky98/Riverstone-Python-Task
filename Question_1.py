""" 1. Create an employee object with attributes 
of employee id, department name, and salary. 
Create a list with 10 employee objects. 
Get employee count department wise"""

class Employee():
    totalEmpCount = hr_count = manager_count = TL_count = anl_count = progr_count = 0
    
    def __init__(self, eId, eDept, eSal):
        self.eId = eId
        self.eDept = eDept
        self.eSal = eSal
        Employee.totalEmpCount += 1
        
        if self.eDept.lower() == "hr":
            Employee.hr_count += 1
        
        elif self.eDept.lower() == "manager":
            Employee.manager_count += 1
        
        elif self.eDept.lower() == "tl":
            Employee.TL_count += 1
        
        elif self.eDept.lower() == "analyst":
            Employee.anl_count += 1
        
        elif self.eDept.lower() == "programmer":
            Employee.progr_count += 1

    def display(self):
        print(f"Employee Id: {self.eId}, Department: {self.eDept}, Salary: {self.eSal}")
    
    def empCount(self):
        return(Employee.hr_count, Employee.manager_count, Employee.TL_count, Employee.anl_count, Employee.progr_count)


empList = []
empList.append(Employee(101, "HR", 50000))
empList.append(Employee(102, "Analyst", 25000))
empList.append(Employee(103, "TL", 40000))
empList.append(Employee(104, "Manager", 70000))
empList.append(Employee(105, "Programmer", 30000))
empList.append(Employee(106, "TL", 45000))
empList.append(Employee(107, "Manager", 60000))
empList.append(Employee(108, "Programmer", 20000))
empList.append(Employee(109, "Programmer", 30000))
empList.append(Employee(110, "Analyst", 30000))

for x in range(len(empList)):
    empList[x].display()

totEmp = empList[len(empList) - 1].totalEmpCount
hr, mgr, tl, anl, prg = empList[len(empList) - 1].empCount()
print(f"Total no.of Employees: {totEmp}")
print(f"Total no.of HR:{hr}")
print(f"Total no.of Manager:{mgr}")
print(f"Total no.of TL:{tl}")
print(f"Total no.of Analyst:{anl}")
print(f"Total no.of Programmer:{prg}")