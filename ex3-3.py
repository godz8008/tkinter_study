class Employee():
    pass

# emp1과 emp2는 서로 다른 객체이다. 즉, 메모리상의 주소값이 서로 다르다.
emp1 = Employee()
emp2 = Employee()

print(id(emp1))
print(id(emp2))
print()
# emp1과 emp2가 서로 같은 클래스의 인스턴스 인지 확인하는 방법
emp1_class = emp1.__class__
emp2_class = emp2.__class__

print (id(emp1_class))
print (id(emp2_class))