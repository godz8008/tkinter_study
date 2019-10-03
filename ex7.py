# 스태틱 메소드

# 인스턴스 메소드, 클래스 매소드, 스태틱 메소드는 이세개의 메소드는
# 모두 클래스 안에서 정의 된다.

# 인스턴스 메소드는 인스턴스를 통해 호출되고, 인자로 인스턴스 자신을 자동으로 전달하는
# self를 첫번째 인자로 사용한다.

# 클래스 메소는 클래스를 통해 호출되고, @classmethod 데코레이터로 정의하고,
# 클래스 자신을 자동으로 전달하는 인자 cls를 첫번째 인자로 사용한다.

# 스태틱 메소드는 인스턴스 메소드나, 클래스 메소드와는 다르게 첫번째 인자를 받지 않는다.
# 스태틱 메소드는 일반 함수와 거의 같다고 볼 수 있다.
# 다만, 클래스와 연관성이 있는 함수를 클래스 안에 정의하여 클래스나 인스턴스를 통해서
# 호출하여 편하게 사용할 수 있는 특징이 있다.
# @staticmethod 데코레이터를 사용하여 정의한다.

class Demon:
    num = 0

    @staticmethod
    def add(x,y):
        return x+y

d = Demon()
print(d.add(1,1))
print(Demon.add(2,2))