#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제
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

# TODO: 다양한 자료형을 포함하는 튜플을 만들어보세요

# 튜플 인덱싱
print("\n튜플 인덱싱:")
print(f"tuple1[0] = {tuple1[0]}")
print(f"tuple1[2] = {tuple1[2]}")
print(f"tuple1[-1] = {tuple1[-1]}")  # 마지막 요소
print(f"tuple5[2] = {tuple5[2]}")  # 중첩 튜플 접근
print(f"tuple5[2][0] = {tuple5[2][0]}")  # 중첩 튜플의 요소

# TODO: 튜플 인덱싱을 사용해 다양한 요소에 접근해보세요

# 튜플 슬라이싱
print("\n튜플 슬라이싱:")
print(f"tuple1[0:2] = {tuple1[0:2]}")
print(f"tuple3[:2] = {tuple3[:2]}")
print(f"tuple3[1:] = {tuple3[1:]}")
print(f"tuple2[:] = {tuple2[:]}")  # 전체 복사

# TODO: 다양한 슬라이싱 방법을 시도해보세요

# 튜플 연산
print("\n튜플 연산:")
print(f"tuple1 + tuple3 = {tuple1 + tuple3}")  # 튜플 연결
print(f"tuple3 * 3 = {tuple3 * 3}")  # 튜플 반복
print(f"len(tuple4) = {len(tuple4)}")  # 튜플 길이

# TODO: 튜플 연산 예제를 추가해보세요

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

# TODO: 튜플에 새 요소를 추가하여 새 튜플을 만들어보세요

# 튜플 메서드
print("\n튜플 메서드:")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"numbers = {numbers}")
print(f"numbers.count(2) = {numbers.count(2)}")  # 튜플에서 2의 개수
print(f"numbers.index(4) = {numbers.index(4)}")  # 4의 위치(인덱스)

# TODO: 다른 값으로 count와 index 메서드를 테스트해보세요

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

# TODO: 자신만의 함수를 만들어 여러 값을 반환하고 언패킹해보세요

# 2. 확장된 언패킹 (Python 3+)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"numbers = {numbers}")
print(f"first = {first}, middle = {middle}, last = {last}")

# TODO: 다른 시퀀스에 확장 언패킹을 적용해보세요

# 3. 튜플을 사용한 스왑(swap)
a, b = 10, 20
print(f"교환 전: a = {a}, b = {b}")
a, b = b, a  # 튜플 사용한 스왑
print(f"교환 후: a = {a}, b = {b}")

# TODO: 세 변수 값을 순환 교환해보세요 (a->b, b->c, c->a)

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

# TODO: 자신만의 네임드 튜플을 정의하고 사용해보세요

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

# TODO: 더 큰 크기의 리스트와 튜플을 비교해보세요
