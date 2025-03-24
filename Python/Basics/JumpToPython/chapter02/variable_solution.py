#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제 해답
변수(Variable)
"""

# 1. 변수 선언과 할당
print("1. 변수 선언과 할당")
a = 10
b = 3.14
c = "Hello"
d = True
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")

# 2. 변수의 타입
print("\n2. 변수의 타입")
print(f"a의 타입: {type(a)}")  # <class 'int'>
print(f"b의 타입: {type(b)}")  # <class 'float'>
print(f"c의 타입: {type(c)}")  # <class 'str'>
print(f"d의 타입: {type(d)}")  # <class 'bool'>

# 3. 변수 재할당
print("\n3. 변수 재할당")
a = 20
print(f"재할당 후 a = {a}")

# 다른 타입으로 재할당 가능 (동적 타이핑)
a = "Python"
print(f"문자열로 재할당 후 a = {a}")
print(f"재할당 후 a의 타입: {type(a)}")

# 4. 여러 변수 동시 할당
print("\n4. 여러 변수 동시 할당")
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

# 값 교환하기
print("\n값 교환하기")
print(f"교환 전: x = {x}, y = {y}")
x, y = y, x
print(f"교환 후: x = {x}, y = {y}")

# 5. 변수 참조와 객체
print("\n5. 변수 참조와 객체")
# 변수는 객체를 참조함
a = [1, 2, 3]
b = a  # b는 a와 같은 객체를 참조
print(f"a = {a}")
print(f"b = {b}")

# a를 변경하면 b도 변경됨
a.append(4)
print(f"a.append(4) 후 a = {a}")
print(f"a.append(4) 후 b = {b}")

# 6. 복사와 참조
print("\n6. 복사와 참조")
# 다른 객체로 복사
a = [1, 2, 3]
b = a.copy()  # 새로운 리스트 객체를 생성하여 b에 할당
print(f"a = {a}")
print(f"b = {b}")

# a를 변경해도 b는 변경되지 않음
a.append(4)
print(f"a.append(4) 후 a = {a}")
print(f"a.append(4) 후 b = {b}")

# 7. 변수의 식별자 (ID)
print("\n7. 변수의 식별자 (ID)")
a = 10
b = 10
c = a
print(f"a의 ID: {id(a)}")
print(f"b의 ID: {id(b)}")
print(f"c의 ID: {id(c)}")
print(f"a와 b는 같은 객체인가? {a is b}")
print(f"a와 c는 같은 객체인가? {a is c}")

# 불변 객체와 가변 객체
print("\n불변 객체와 가변 객체")
# 불변 객체 (int, float, str, tuple)
a = 10
print(f"a = {a}, ID: {id(a)}")
a = a + 1
print(f"a = {a}, ID: {id(a)}")  # ID가 변경됨 (새로운 객체가 생성됨)

# 가변 객체 (list, dict, set)
b = [1, 2, 3]
print(f"b = {b}, ID: {id(b)}")
b.append(4)
print(f"b = {b}, ID: {id(b)}")  # ID가 같음 (같은 객체가 수정됨)

# 8. 변수의 범위 (Scope)
print("\n8. 변수의 범위 (Scope)")

# 전역 변수
global_var = "나는 전역 변수입니다"


def function1():
    # 지역 변수
    local_var = "나는 지역 변수입니다"
    print(f"함수 내부에서 전역 변수 접근: {global_var}")
    print(f"함수 내부에서 지역 변수 접근: {local_var}")


function1()
print(f"함수 외부에서 전역 변수 접근: {global_var}")
# print(f"함수 외부에서 지역 변수 접근: {local_var}")  # 오류 발생! 지역 변수는 함수 외부에서 접근 불가

# 지역 변수가 전역 변수와 이름이 같은 경우
print("\n지역 변수가 전역 변수와 이름이 같은 경우")
x = 10


def function2():
    x = 20  # 전역 변수 x와 다른 지역 변수 x
    print(f"함수 내부에서 x = {x}")


function2()
print(f"함수 외부에서 x = {x}")

# global 키워드 사용
print("\nglobal 키워드 사용")
y = 10


def function3():
    global y  # 전역 변수 y를 사용하겠다고 선언
    y = 20  # 전역 변수 y의 값을 변경
    print(f"함수 내부에서 y = {y}")


function3()
print(f"함수 외부에서 y = {y}")  # 함수에서 변경한 값이 유지됨

# 9. 네임스페이스 (Namespace)
print("\n9. 네임스페이스 (Namespace)")
# 빌트인 네임스페이스
print(f"빌트인 함수 예: len([1, 2, 3]) = {len([1, 2, 3])}")

# 모듈 네임스페이스
import math

print(f"math 모듈의 pi = {math.pi}")


# 지역 네임스페이스
def outer_function():
    outer_var = "외부 함수 변수"

    def inner_function():
        inner_var = "내부 함수 변수"
        print(f"내부 함수에서 outer_var: {outer_var}")  # 외부 함수의 변수에 접근 가능
        print(f"내부 함수에서 inner_var: {inner_var}")

    inner_function()
    print(f"외부 함수에서 outer_var: {outer_var}")
    # print(f"외부 함수에서 inner_var: {inner_var}")  # 오류 발생! 내부 함수의 변수에 접근 불가


outer_function()

# 10. 변수 생명 주기 (Lifetime)
print("\n10. 변수 생명 주기 (Lifetime)")


def lifetime_example():
    local_var = "함수 호출 시 생성됨"
    print(local_var)
    # 함수가 종료되면 local_var는 소멸됨


lifetime_example()
# print(local_var)  # 오류 발생! 함수가 종료되어 변수가 소멸됨

# 11. 변수 이름 규칙
print("\n11. 변수 이름 규칙")
# 올바른 변수명
valid_name = 10
my_var = 20
myVar = 30
_private = 40
number1 = 50


# 파이썬 네이밍 컨벤션 예시
class MyClass:  # 클래스는 CamelCase
    class_variable = 100  # 클래스 변수는 snake_case

    def __init__(self):
        self.instance_variable = 200  # 인스턴스 변수는 snake_case

    def method_name(self):  # 메서드는 snake_case
        local_variable = 300  # 지역 변수는 snake_case
        return local_variable


CONSTANT = 500  # 상수는 대문자 SNAKE_CASE

instance = MyClass()
print(f"클래스 변수: {MyClass.class_variable}")
print(f"인스턴스 변수: {instance.instance_variable}")
print(f"메서드 호출 결과: {instance.method_name()}")
print(f"상수: {CONSTANT}")

# 12. del 키워드로 변수 삭제
print("\n12. del 키워드로 변수 삭제")
a = 10
print(f"삭제 전 a = {a}")
del a
# print(f"삭제 후 a = {a}")  # 오류 발생! 변수가 삭제됨

# del을 활용한 리스트 요소 삭제
my_list = [1, 2, 3, 4, 5]
print(f"원래 리스트: {my_list}")
del my_list[2]  # 인덱스 2(값 3)를 삭제
print(f"del my_list[2] 후: {my_list}")

# del을 활용한 딕셔너리 항목 삭제
my_dict = {"a": 1, "b": 2, "c": 3}
print(f"원래 딕셔너리: {my_dict}")
del my_dict["b"]  # 키 'b'를 삭제
print(f"del my_dict['b'] 후: {my_dict}")

# 13. 변수와 메모리
print("\n13. 변수와 메모리")
import sys

# 다양한 타입의 객체 크기
int_var = 10
float_var = 3.14
str_var = "Hello"
list_var = [1, 2, 3]
dict_var = {"a": 1, "b": 2}

print(f"int_var의 크기: {sys.getsizeof(int_var)} 바이트")
print(f"float_var의 크기: {sys.getsizeof(float_var)} 바이트")
print(f"str_var의 크기: {sys.getsizeof(str_var)} 바이트")
print(f"list_var의 크기: {sys.getsizeof(list_var)} 바이트")
print(f"dict_var의 크기: {sys.getsizeof(dict_var)} 바이트")

# 문자열의 길이에 따른 메모리 사용량
str1 = "a"
str2 = "a" * 10
str3 = "a" * 100
print(f"str1(길이 1)의 크기: {sys.getsizeof(str1)} 바이트")
print(f"str2(길이 10)의 크기: {sys.getsizeof(str2)} 바이트")
print(f"str3(길이 100)의 크기: {sys.getsizeof(str3)} 바이트")

# 리스트의 길이에 따른 메모리 사용량
list1 = []
list2 = [0] * 10
list3 = [0] * 100
print(f"list1(길이 0)의 크기: {sys.getsizeof(list1)} 바이트")
print(f"list2(길이 10)의 크기: {sys.getsizeof(list2)} 바이트")
print(f"list3(길이 100)의 크기: {sys.getsizeof(list3)} 바이트")

# 14. 변수 타입 변환
print("\n14. 변수 타입 변환")
a = 10
b = "20"
# 두 변수를 더하려면 타입 변환이 필요합니다.
print(f"a + int(b) = {a + int(b)}")  # 숫자로 변환하여 더하기
print(f"str(a) + b = {str(a) + b}")  # 문자열로 변환하여 연결하기

# 다양한 타입 변환 예제
print("\n다양한 타입 변환 예제:")
# 정수로 변환
print(f"int(3.14) = {int(3.14)}")  # 소수점 버림
print(f"int('100') = {int('100')}")  # 문자열 -> 정수
print(f"int('0x1F', 16) = {int('0x1F', 16)}")  # 16진수 문자열 -> 정수
print(f"int(True) = {int(True)}")  # 불린 -> 정수
print(f"int(False) = {int(False)}")  # 불린 -> 정수

# 실수로 변환
print(f"float(10) = {float(10)}")  # 정수 -> 실수
print(f"float('3.14') = {float('3.14')}")  # 문자열 -> 실수
print(f"float('1e3') = {float('1e3')}")  # 지수 표기법 문자열 -> 실수

# 문자열로 변환
print(f"str(10) = {str(10)}")  # 정수 -> 문자열
print(f"str(3.14) = {str(3.14)}")  # 실수 -> 문자열
print(f"str([1, 2, 3]) = {str([1, 2, 3])}")  # 리스트 -> 문자열

# 불린으로 변환
print(f"bool(0) = {bool(0)}")  # 0 -> False
print(f"bool(1) = {bool(1)}")  # 0이 아닌 숫자 -> True
print(f"bool('') = {bool('')}")  # 빈 문자열 -> False
print(f"bool('hello') = {bool('hello')}")  # 비어있지 않은 문자열 -> True
print(f"bool([]) = {bool([])}")  # 빈 리스트 -> False
print(f"bool([1, 2]) = {bool([1, 2])}")  # 비어있지 않은 리스트 -> True

# 15. 변수의 참조와 복사 실험
print("\n15. 변수의 참조와 복사 실험")
original = [1, 2, 3]
reference = original  # 참조 복사 (같은 객체를 가리킴)
shallow_copy = original.copy()  # 얕은 복사 (새로운 객체를 생성하지만 내부 객체는 동일)
import copy

deep_copy = copy.deepcopy(original)  # 깊은 복사 (내부 객체도 모두 새로 생성)

print(f"원본: {original}")
print(f"참조: {reference}")
print(f"얕은 복사: {shallow_copy}")
print(f"깊은 복사: {deep_copy}")

# original 수정
original.append(4)
print("\n원본에 4 추가 후:")
print(f"원본: {original}")
print(f"참조: {reference}")  # reference도 변경됨
print(f"얕은 복사: {shallow_copy}")  # shallow_copy는 변경되지 않음
print(f"깊은 복사: {deep_copy}")  # deep_copy도 변경되지 않음

# 중첩 리스트로 테스트
print("\n중첩 리스트 테스트:")
nested_original = [1, 2, [3, 4]]
nested_reference = nested_original  # 참조
nested_shallow = nested_original.copy()  # 얕은 복사
nested_deep = copy.deepcopy(nested_original)  # 깊은 복사

print(f"중첩 원본: {nested_original}")
print(f"중첩 참조: {nested_reference}")
print(f"중첩 얕은 복사: {nested_shallow}")
print(f"중첩 깊은 복사: {nested_deep}")

# 내부 리스트 수정
nested_original[2].append(5)
print("\n중첩 원본 내부 리스트에 5 추가 후:")
print(f"중첩 원본: {nested_original}")
print(f"중첩 참조: {nested_reference}")  # 참조도 변경됨
print(f"중첩 얕은 복사: {nested_shallow}")  # 얕은 복사의 내부 리스트도 변경됨
print(f"중첩 깊은 복사: {nested_deep}")  # 깊은 복사는 변경되지 않음

# 16. 변수를 활용한 간단한 예제
print("\n16. 변수를 활용한 간단한 예제")


# 온도 변환 (섭씨 -> 화씨)
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# 온도 변환 (화씨 -> 섭씨)
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# 다양한 온도 변환 테스트
celsius_temps = [0, 25, 100]
for temp in celsius_temps:
    fahrenheit = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {fahrenheit:.1f}°F")

print()
fahrenheit_temps = [32, 77, 212]
for temp in fahrenheit_temps:
    celsius = fahrenheit_to_celsius(temp)
    print(f"{temp}°F = {celsius:.1f}°C")


# 변수를 사용한 계산: 원의 둘레와 면적
def circle_calculations(radius):
    import math

    circumference = 2 * math.pi * radius
    area = math.pi * radius**2
    return circumference, area  # 여러 값을 반환


r = 5
circumference, area = circle_calculations(r)
print(f"\n반지름이 {r}인 원:")
print(f"둘레: {circumference:.2f}")
print(f"면적: {area:.2f}")

# 17. 변수의 교환 방식
print("\n17. 변수의 교환 방식")

# 1. 파이썬의 특별한 방식
a, b = 10, 20
print(f"교환 전: a = {a}, b = {b}")
a, b = b, a
print(f"방법 1 - 파이썬 기본 교환 후: a = {a}, b = {b}")

# 2. 임시 변수 사용
a, b = 10, 20
print(f"교환 전: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"방법 2 - 임시 변수 사용 후: a = {a}, b = {b}")

# 3. 덧셈과 뺄셈 (정수, 실수만 가능)
a, b = 10, 20
print(f"교환 전: a = {a}, b = {b}")
a = a + b  # a = 30, b = 20
b = a - b  # a = 30, b = 10
a = a - b  # a = 20, b = 10
print(f"방법 3 - 덧셈과 뺄셈 후: a = {a}, b = {b}")

# 4. XOR 연산자 (정수만 가능)
a, b = 10, 20
print(f"교환 전: a = {a}, b = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"방법 4 - XOR 연산 후: a = {a}, b = {b}")

# 18. 언패킹(Unpacking)
print("\n18. 언패킹(Unpacking)")

# 리스트 언패킹
numbers = [1, 2, 3]
a, b, c = numbers  # 리스트 언패킹
print(f"numbers = {numbers}")
print(f"a = {a}, b = {b}, c = {c}")

# 튜플 언패킹
coordinates = (10, 20, 30)
x, y, z = coordinates  # 튜플 언패킹
print(f"coordinates = {coordinates}")
print(f"x = {x}, y = {y}, z = {z}")

# 문자열 언패킹
greeting = "ABC"
first, second, third = greeting  # 문자열 언패킹
print(f"greeting = {greeting}")
print(f"first = {first}, second = {second}, third = {third}")

# 확장된 언패킹 (Python 3.x)
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers  # 확장된 언패킹
print(f"numbers = {numbers}")
print(f"first = {first}, middle = {middle}, last = {last}")


# 함수 반환값 언패킹
def get_person_info():
    return "김철수", 30, "서울"


name, age, city = get_person_info()  # 함수 반환값 언패킹
print(f"이름: {name}, 나이: {age}, 도시: {city}")

# 딕셔너리 언패킹
person = {"name": "박영희", "age": 25, "city": "부산"}
# 딕셔너리 키 언패킹
keys = person.keys()
values = person.values()
items = person.items()
print(f"keys = {keys}")
print(f"values = {values}")
print(f"items = {items}")

# 딕셔너리 items() 언패킹
for key, value in person.items():
    print(f"{key}: {value}")

# 19. 변수와 함수
print("\n19. 변수와 함수")


# 1. 기본 매개변수
def greet(name, greeting="안녕하세요"):
    return f"{greeting}, {name}님!"


print(greet("철수"))  # 기본 인사말 사용
print(greet("영희", "반갑습니다"))  # 사용자 지정 인사말 사용


# 2. 가변 인자 (*args)
def sum_all(*numbers):
    return sum(numbers)


print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10, 20) = {sum_all(10, 20)}")


# 3. 키워드 가변 인자 (**kwargs)
def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("\n사람 정보 출력:")
print_person_info(name="김철수", age=30, job="개발자", city="서울")

# 4. 변수 범위와 함수
counter = 0


def increment():
    global counter
    counter += 1
    return counter


print(f"초기 counter: {counter}")
print(f"첫 번째 호출: {increment()}")
print(f"두 번째 호출: {increment()}")
print(f"세 번째 호출: {increment()}")


# 5. 함수 내 함수 (클로저)
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


add_five = outer_function(5)
print(f"add_five(10) = {add_five(10)}")
print(f"add_five(20) = {add_five(20)}")

# 20. 컴프리헨션(Comprehension)과 변수
print("\n20. 컴프리헨션(Comprehension)과 변수")

# 1. 리스트 컴프리헨션
numbers = list(range(1, 11))
squares = [x**2 for x in numbers]
even_squares = [x**2 for x in numbers if x % 2 == 0]

print(f"numbers = {numbers}")
print(f"squares = {squares}")
print(f"even_squares = {even_squares}")

# 2. 딕셔너리 컴프리헨션
square_dict = {x: x**2 for x in range(1, 6)}
print(f"square_dict = {square_dict}")

# 이름과 점수를 연결한 딕셔너리
names = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]
score_dict = {name: score for name, score in zip(names, scores)}
print(f"score_dict = {score_dict}")

# 3. 집합 컴프리헨션
vowels = {"a", "e", "i", "o", "u"}
text = "hello world"
text_vowels = {char for char in text if char in vowels}
print(f"text_vowels = {text_vowels}")

# 21. 변수와 함수형 프로그래밍
print("\n21. 변수와 함수형 프로그래밍")

# 1. map 함수
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"numbers = {numbers}")
print(f"doubled = {doubled}")

# 2. filter 함수
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"even_numbers = {even_numbers}")

# 3. reduce 함수
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print(f"product = {product}")  # 1 * 2 * 3 * 4 * 5 = 120
