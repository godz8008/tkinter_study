# 클래스 변수와 인스턴스 변수

# 인스턴스 변수 : 종업원의 이름, 종업원의 급여과 같이 각각의 인스턴스마다 가지고 있는 
#              고유한 데이터

# 클래스 변수 : 같은 클래스로 만들어진 모든 인스턴스가 공유하는 데이터

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def empInfo(self):
        print("Name : ", self.name, ", Salary : ", self.salary)

    def showEmpCount(self):
        print("전체 종업원 수는 %d" % Employee.empCount)

    def raise_salary(self):
        self.salary = int(self.salary * 1.1)

emp1 = Employee("김말똥", 2000)
emp2 = Employee("고길동", 3000)

emp1.empInfo()
emp1.raise_salary()
emp2.empInfo()
emp1.empInfo()
emp1.showEmpCount()
emp2.showEmpCount()