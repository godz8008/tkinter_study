# 클래스 메소드와 스태틱 메소드

# 인스턴스 메소드는 self인 인스턴스를 인자로 받고 인스턴스에만 한정된 데이터를
# 생성하거나 변경하거나 참조한다.

# 클래스 메소드는 cls인 클래스를 인자를 받고 모든 인스턴스가 공유하는 클래스 변수처럼
# 데이터를 생성하거나 변경하거나 참조하기 위한 메소드이다.

class Employee:

    raise_ratio = 1.1

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def empInfo(self):
        print("Name : ",self.name, ", Salary : ", self.salary)

    def raise_salary(self):
        self.salary = int(self.salary * self.raise_ratio)

    @classmethod  # 클래스 메소드 데코레이터를 이용한 클래스 메소드 정의
    def change_raise_ratio(cls, ratio):
        # 인상률이 1보다 작은 경우 재입력 요청
        while ratio < 1:
            print("인상률은 1보다 크거나 같은 값을 입력하시요!!")
            ratio = input("인상률을 다시 입력해주세요. \n")
            ratio = float(ratio)
            
        ratio = float(ratio)
        cls.raise_ratio = ratio
        print("인상율 ", round((ratio-1)*100),"% 적용 되었습니다.")


emp1 = Employee("김말똥", 2000)
emp2 = Employee("고길동", 3000)

# 인상전 급여 출력
emp1.empInfo()
emp2.empInfo()

# 인상률 변경
Employee.change_raise_ratio(0.8)

# 인상후 급여 출력
emp1.raise_salary()
emp2.raise_salary()

emp1.empInfo()
emp2.empInfo()