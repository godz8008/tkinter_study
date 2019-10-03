class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

# 인스턴스 변수
emp1.name = '김말똥'
emp1.salary = 2000

emp2.name = '고길동'
emp2.salary = 3000

# 인스턴스 변수에 접근하기 위해서는 인스턴스명을 사용한다.
print(emp1.name)
print(emp1.salary)
print()
print(emp2.name)
print(emp2.salary)