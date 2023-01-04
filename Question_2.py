""" 2. Define an employee object. Create 2 employee objects - 
one is a Teacher employee object and another one is a Clerk employee object. 
Define appropriate functionalities for the teacher & clerk and execute them. """

class Employee():
    def __init__(self, eName, eExp):
        self.eName = eName
        self.eExp = eExp
        self.salary = 0

class Teacher(Employee):
    def __init__(self, eName, eExp, basicPay):
        super().__init__(eName, eExp)
        self.basicPay = basicPay
        self.eExp = int(self.eExp)
    
    def calc_salary(self):
        if self.eExp >= 7:
            self.salary = int(self.basicPay) + 10000
        elif self.eExp >= 5:
            self.salary = int(self.basicPay) + 7000
        elif self.eExp >= 3:
            self.salary = int(self.basicPay) + 5000
        elif self.eExp >= 1:
            self.salary = int(self.basicPay) + 3000
        elif self.eExp <= 1:
            self.salary = int(self.basicPay) + 1000
        return self.salary
    

class Clerk(Employee):
    def __init__(self, eName, eExp, basicPay):
        super().__init__(eName, eExp)
        self.basicPay = basicPay
        self.eExp = int(self.eExp)
        
    def calc_salary(self):
        if self.eExp >= 7:
            self.salary = int(self.basicPay) + 7000
        elif self.eExp >= 5:
            self.salary = int(self.basicPay) + 5000
        elif self.eExp >= 3:
            self.salary = int(self.basicPay) + 3000
        elif self.eExp >= 1:
            self.salary = int(self.basicPay) + 1000
        elif self.eExp <= 1:
            self.salary = int(self.basicPay) + 0
        
        return self.salary

print("Choose the employee type from below: \n"
      "1 => Teacher \n"
      "2 => Clerk")
choice = input("Enter the choice: ")
try:
    int(choice)
except (TypeError, ValueError):
    print("Please enter a valid option!")
else:
    match int(choice):
        case 1:
            ename = input("Enter the Teacher's name: ")
            exp = input("Enter the no. of experience: ")
            try:
                int(exp)
            except (ValueError, TypeError):
                print("Please enter the valid no. of experience!")
            else:
                basicpay = input("Enter the basic pay of the Teacher: ")
                try:
                    int(basicpay)
                except (ValueError, TypeError):
                    print("Please enter the valid Basic Pay!")
                else:
                    salary_Teacher = Teacher(ename,exp,basicpay).calc_salary()
                    print(f"The salary of employee ({ename}) with {exp} years experience is Rs.{salary_Teacher}")
        case 2:
            ename = input("Enter the Clerk's name: ")
            exp = input("Enter the no. of experience: ")
            try:
                int(exp)
            except (ValueError, TypeError):
                print("Please enter the valid no. of experience!")
            else:
                basicpay = input("Enter the basic pay of the Clerk: ")
                try:
                    int(basicpay)
                except (ValueError, TypeError):
                    print("Please enter the valid Basic Pay!")
                else:
                    salary_Clerk = Clerk(ename,exp,basicpay).calc_salary()
                    print(f"The salary of employee ({ename}) with {exp} years experience is Rs.{salary_Clerk}")