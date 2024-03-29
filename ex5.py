class Person:
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender

    def __str__(self):
        return "{}년 {}월 {}일 태어난 {}입니다.".format(self.year,self.month,self.day,self.gender)

id_number1 = "010101-4110212"
id_number2 = "100202-1123234"

def id_process(id):
    first, second = id.split('-')
    gender = second[0]

    if gender == '1' or gender == '2':
        year = '19' + first[:2]
    else:
        year = '20' + first[:2]

    if (int(gender)) % 2 == 0:
        gender = "여성"
    else:
        gender = "남성"

    month = first[2:4]
    day = first[4:6]

    return year, month, day, gender

person1 = Person(*id_process(id_number1))

print(person1)

person2 = Person(*id_process(id_number2))
print(person2)