class Person:
    # 클래스 변수 (모든 인스턴스가 공유)
    species = "Homo sapiens"

    def __init__(self, name, age):
        # 인스턴스 변수 (각 인스턴스가 개별적으로 가짐)
        self.name = name
        self.age = age

    def greet(self):
        # 인스턴스 메서드
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    @classmethod
    def species_info(cls):
        # 클래스 메서드 (cls를 첫 번째 인수로 받음)
        print(f"Humans are species of {cls.species}.")

    @staticmethod
    def is_adult(age):
        # 정적 메서드 (self나 cls를 받지 않음)
        return age >= 18

# 인스턴스 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 17)

print(person1.species)
person1.species = "change"
print(person1.species)
print(person2.species)
# 인스턴스 메서드 호출
person1.greet()  # Hello, my name is Alice and I am 30 years old.
person2.greet()  # Hello, my name is Bob and I am 17 years old.

# 클래스 메서드 호출
Person.species_info()  # Humans are species of Homo sapiens.

# 정적 메서드 호출
print(Person.is_adult(30))  # True
print(Person.is_adult(17))  # False
