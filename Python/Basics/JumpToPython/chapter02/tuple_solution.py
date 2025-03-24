#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제 해답
튜플(Tuple) 자료형
"""

# 튜플 생성
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3  # 괄호 생략 가능
tuple3 = ("a", "b", "c")
tuple4 = (1, "a", True)
tuple5 = (1, 2, (3, 4))  # 중첩 튜플
tuple6 = ()  # 빈 튜플
tuple7 = (1,)  # 요소가 하나인 튜플은 반드시 쉼표가 필요
not_tuple = 1  # 튜플이 아님 (그냥 정수)

print("튜플 생성 예제:")
print(f"tuple1 = {tuple1}")
print(f"tuple2 = {tuple2}")
print(f"tuple3 = {tuple3}")
print(f"tuple4 = {tuple4}")
print(f"tuple5 = {tuple5}")
print(f"tuple6 = {tuple6}")
print(f"tuple7 = {tuple7}, 타입: {type(tuple7)}")
print(f"not_tuple = {not_tuple}, 타입: {type(not_tuple)}")

# 다양한 자료형을 포함하는 튜플
mixed_tuple = (1, 3.14, "python", True, (1, 2), {"name": "Kim"})
print(f"mixed_tuple = {mixed_tuple}, 타입: {type(mixed_tuple)}")

# 튜플 인덱싱
print("\n튜플 인덱싱:")
print(f"tuple1[0] = {tuple1[0]}")
print(f"tuple1[2] = {tuple1[2]}")
print(f"tuple1[-1] = {tuple1[-1]}")  # 마지막 요소
print(f"tuple5[2] = {tuple5[2]}")  # 중첩 튜플 접근
print(f"tuple5[2][0] = {tuple5[2][0]}")  # 중첩 튜플의 요소

# 추가 인덱싱 예제
print(f"tuple3[-2] = {tuple3[-2]}")  # 뒤에서 두 번째 요소
print(
    f"tuple4[0] + tuple4[1] = {tuple4[0]} + {tuple4[1]} = {str(tuple4[0]) + tuple4[1]}"
)  # 정수와 문자열
print(f"mixed_tuple[4][1] = {mixed_tuple[4][1]}")  # 중첩 튜플 접근
print(f"mixed_tuple[5]['name'] = {mixed_tuple[5]['name']}")  # 딕셔너리 요소 접근

# 튜플 슬라이싱
print("\n튜플 슬라이싱:")
print(f"tuple1[0:2] = {tuple1[0:2]}")
print(f"tuple3[:2] = {tuple3[:2]}")
print(f"tuple3[1:] = {tuple3[1:]}")
print(f"tuple2[:] = {tuple2[:]}")  # 전체 복사

# 추가 슬라이싱 예제
print(f"tuple1[1:3] = {tuple1[1:3]}")  # 1번째부터 2번째까지
print(f"tuple3[::2] = {tuple3[::2]}")  # 처음부터 끝까지 2칸씩 건너뛰기
print(f"tuple2[::-1] = {tuple2[::-1]}")  # 역순으로 전체 요소
print(f"tuple2[:-1] = {tuple2[:-1]}")  # 마지막 요소를 제외한 모든 요소

# 튜플 연산
print("\n튜플 연산:")
print(f"tuple1 + tuple3 = {tuple1 + tuple3}")  # 튜플 연결
print(f"tuple3 * 3 = {tuple3 * 3}")  # 튜플 반복
print(f"len(tuple4) = {len(tuple4)}")  # 튜플 길이

# 추가 연산 예제
joined_tuple = tuple4 + tuple5
print(f"tuple4 + tuple5 = {joined_tuple}")
multiplied_tuple = tuple1 * 4
print(f"tuple1 * 4 = {multiplied_tuple}")
print(f"len(joined_tuple) = {len(joined_tuple)}")

# 튜플 비교 연산
print(f"(1, 2, 3) == (1, 2, 3): {(1, 2, 3) == (1, 2, 3)}")
print(f"(1, 2, 3) != (1, 3, 2): {(1, 2, 3) != (1, 3, 2)}")
print(f"(1, 2, 3) < (1, 3, 0): {(1, 2, 3) < (1, 3, 0)}")  # 사전식 비교
print(f"(1, 2, 3) > (1, 1, 3): {(1, 2, 3) > (1, 1, 3)}")  # 사전식 비교

# 튜플의 요소는 변경 불가능
# 다음 코드는 오류를 발생시킵니다.
# tuple1[0] = 5  # TypeError: 'tuple' object does not support item assignment

# 튜플 = 불변(immutable) 자료형
original_id = id(tuple1)
tuple1 = tuple1 + (4,)  # 새로운 튜플이 생성됨
new_id = id(tuple1)

print("\n튜플 불변성 테스트:")
print(f"원래 튜플 ID: {original_id}")
print(f"새 튜플 ID: {new_id}")
print(f"ID가 같은가?: {original_id == new_id}")  # False: 새로운 객체가 생성됨
print(f"새 튜플: {tuple1}")

# 튜플에 새 요소를 추가하여 새 튜플 만들기
tuple2 = tuple2 + (4, 5)
print(f"tuple2 + (4, 5) = {tuple2}")

# 튜플을 리스트로 변환 후 수정하고 다시 튜플로 변환
temp_list = list(tuple3)
temp_list.append("d")
tuple3 = tuple(temp_list)
print(f"list로 변환 후 수정하여 튜플 만들기: {tuple3}")

# 튜플 메서드
print("\n튜플 메서드:")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"numbers = {numbers}")
print(f"numbers.count(2) = {numbers.count(2)}")  # 튜플에서 2의 개수
print(f"numbers.index(4) = {numbers.index(4)}")  # 4의 위치(인덱스)

# 추가 메서드 테스트
print(f"numbers.count(1) = {numbers.count(1)}")
print(f"numbers.count(10) = {numbers.count(10)}")  # 없는 요소는 0 반환
print(f"numbers.index(5) = {numbers.index(5)}")  # 마지막 요소 위치

# 두 번째 인수로 검색 시작 위치 지정
print(f"numbers.index(2, 2) = {numbers.index(2, 2)}")  # 인덱스 2 이후의 첫번째 2 위치

try:
    print(numbers.index(10))  # 없는 요소의 인덱스를 찾으면 ValueError 발생
except ValueError as e:
    print(f"ValueError 발생: {e}")

# 튜플 응용
print("\n튜플 응용:")

# 1. 튜플 언패킹(unpacking)
coordinates = (10, 20)
x, y = coordinates
print(f"coordinates = {coordinates}")
print(f"x = {x}, y = {y}")


# 여러 값 반환하는 함수 (사실은 튜플 반환)
def calculate(a, b):
    return a + b, a - b, a * b, a / b  # 튜플 반환


result = calculate(10, 3)
print(f"calculate(10, 3) = {result}")

# 반환값 직접 언패킹
add, sub, mul, div = calculate(10, 3)
print(f"add = {add}, sub = {sub}, mul = {mul}, div = {div}")


# 자신만의 함수 만들어 여러 값 반환하고 언패킹
def circle_info(radius):
    import math

    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter


# 원의 넓이, 둘레, 지름 계산 및 언패킹
circle_radius = 5
area, circumference, diameter = circle_info(circle_radius)
print(f"\n반지름이 {circle_radius}인 원:")
print(f"넓이 = {area:.2f}, 둘레 = {circumference:.2f}, 지름 = {diameter}")

# 2. 확장된 언패킹 (Python 3+)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"\n확장된 언패킹:")
print(f"numbers = {numbers}")
print(f"first = {first}, middle = {middle}, last = {last}")

# 다른 시퀀스에 확장 언패킹 적용
letters = ["a", "b", "c", "d", "e", "f"]
first, *middle, last = letters
print(f"letters = {letters}")
print(f"first = {first}, middle = {middle}, last = {last}")

string = "Python"
first, *middle, last = string
print(f"string = {string}")
print(f"first = {first}, middle = {middle}, last = {last}")

# 앞쪽 요소만 가져오기
first, second, *rest = (1, 2, 3, 4, 5)
print(f"first = {first}, second = {second}, rest = {rest}")

# 뒤쪽 요소만 가져오기
*beginning, last_two, last_one = (1, 2, 3, 4, 5)
print(f"beginning = {beginning}, last_two = {last_two}, last_one = {last_one}")

# 3. 튜플을 사용한 스왑(swap)
a, b = 10, 20
print(f"\n스왑 예제:")
print(f"교환 전: a = {a}, b = {b}")
a, b = b, a  # 튜플 사용한 스왑
print(f"교환 후: a = {a}, b = {b}")

# 세 변수 값 순환 교환 (a->b, b->c, c->a)
a, b, c = 10, 20, 30
print(f"\n순환 교환 전: a = {a}, b = {b}, c = {c}")
a, b, c = c, a, b
print(f"순환 교환 후: a = {a}, b = {b}, c = {c}")

# 4. 네임드 튜플(Named Tuple) - 이름으로 접근 가능한 튜플
from collections import namedtuple

# Point 네임드 튜플 정의
Point = namedtuple("Point", ["x", "y"])
p1 = Point(11, 22)
p2 = Point(x=33, y=44)

print("\n네임드 튜플:")
print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1.x = {p1.x}, p1.y = {p1.y}")  # 속성으로 접근
print(f"p2[0] = {p2[0]}, p2[1] = {p2[1]}")  # 인덱스로 접근
print(f"x좌표들: {p1.x}, {p2.x}")  # 특정 필드만 접근

# 자신만의 네임드 튜플 정의와 사용
Person = namedtuple("Person", "name age gender")
person1 = Person("Kim", 30, "Male")
person2 = Person(name="Lee", age=25, gender="Female")

print("\n사용자 정의 네임드 튜플:")
print(f"person1 = {person1}")
print(f"person2 = {person2}")

# 필드 이름으로 접근
print(f"person1.name = {person1.name}, person1.age = {person1.age}")

# 인덱스로 접근
print(f"person2[0] = {person2[0]}, person2[1] = {person2[1]}")

# 언패킹
name, age, gender = person1
print(f"언패킹: name = {name}, age = {age}, gender = {gender}")

# getattr 함수 사용
print(f"getattr(person1, 'name') = {getattr(person1, 'name')}")

# _asdict() 메서드로 딕셔너리 변환
person_dict = person1._asdict()
print(f"person1._asdict() = {person_dict}")

# _replace() 메서드로 필드 값 변경 (새 객체 생성)
person3 = person1._replace(age=40)
print(f"person1 = {person1}")
print(f"person3 = person1._replace(age=40) = {person3}")

# 튜플 vs 리스트
print("\n튜플과 리스트 비교:")
import sys

list_ex = [1, 2, 3, 4, 5]
tuple_ex = (1, 2, 3, 4, 5)

print(f"리스트 크기: {sys.getsizeof(list_ex)} 바이트")
print(f"튜플 크기: {sys.getsizeof(tuple_ex)} 바이트")

import timeit

list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print(f"리스트 생성 시간: {list_time:.6f}초")
print(f"튜플 생성 시간: {tuple_time:.6f}초")

# 더 큰 크기 비교
big_list = list(range(1000))
big_tuple = tuple(range(1000))

print(f"\n1000개 요소:")
print(f"큰 리스트 크기: {sys.getsizeof(big_list)} 바이트")
print(f"큰 튜플 크기: {sys.getsizeof(big_tuple)} 바이트")

# 접근 시간 비교
list_access = timeit.timeit(stmt="big_list[500]", globals=locals(), number=1000000)
tuple_access = timeit.timeit(stmt="big_tuple[500]", globals=locals(), number=1000000)

print(f"리스트 요소 접근 시간: {list_access:.6f}초")
print(f"튜플 요소 접근 시간: {tuple_access:.6f}초")

# 인덱스 검색 시간 비교
list_index = timeit.timeit(stmt="big_list.index(500)", globals=locals(), number=1000)
tuple_index = timeit.timeit(stmt="big_tuple.index(500)", globals=locals(), number=1000)

print(f"리스트 인덱스 검색 시간: {list_index:.6f}초")
print(f"튜플 인덱스 검색 시간: {tuple_index:.6f}초")
