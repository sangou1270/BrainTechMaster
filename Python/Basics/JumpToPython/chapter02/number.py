#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제
숫자형(Number) 자료형
"""

# 정수형(Integer)
a = 123
b = -178
c = 0

print("정수형 예제:")
print(f"a = {a}, b = {b}, c = {c}")

# TODO: 다양한 진수 표현을 사용하여 정수 변수를 선언하고 출력해보세요
# 2진수(0b), 8진수(0o), 16진수(0x)
binary = None
octal = None
hexadecimal = None

# 실수형(Floating-point)
a = 1.2
b = -3.45
c = 4.24e10  # 4.24 * 10^10
d = 4.24e-10  # 4.24 * 10^-10

print("\n실수형 예제:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# TODO: 원하는 실수 값을 변수에 할당하고 출력해보세요
my_float = None

# 복소수형(Complex Number)
a = 1 + 2j
b = 3 - 4j
c = complex(5, 6)  # 5 + 6j

print("\n복소수형 예제:")
print(f"a = {a}, b = {b}, c = {c}")
print(f"a의 실수부: {a.real}, a의 허수부: {a.imag}")
print(f"a의 켤레복소수: {a.conjugate()}")

# TODO: 두 복소수의 덧셈과 곱셈 결과를 출력해보세요
# a + b와 a * b의 결과

# 숫자형 연산
print("\n기본 연산:")
print(f"덧셈: 5 + 2 = {5 + 2}")
print(f"뺄셈: 5 - 2 = {5 - 2}")
print(f"곱셈: 5 * 2 = {5 * 2}")
print(f"나눗셈: 5 / 2 = {5 / 2}")  # 나눗셈 결과는 항상 실수
print(f"몫: 5 // 2 = {5 // 2}")  # 소수점 이하를 버린 몫
print(f"나머지: 5 % 2 = {5 % 2}")  # 나머지
print(f"거듭제곱: 5 ** 2 = {5 ** 2}")  # 5의 2제곱

# TODO: 세 자리 숫자로 나눗셈과 나머지 연산을 수행해보세요
# 예: 1234를 123으로 나눈 몫과 나머지

# 타입 변환
print("\n타입 변환:")
print(f"int('123') = {int('123')}")
print(f"float('3.14') = {float('3.14')}")
print(f"int(3.14) = {int(3.14)}")  # 소수점 이하는 버림
print(f"float(42) = {float(42)}")
print(f"complex(1, 2) = {complex(1, 2)}")

# TODO: 다양한 형변환 예제를 추가해보세요

# 수학 함수 활용 (모듈 사용)
import math

print("\n수학 함수:")
print(f"절대값: abs(-5) = {abs(-5)}")
print(f"최대값: max(1, 2, 3, 4, 5) = {max(1, 2, 3, 4, 5)}")
print(f"최소값: min(1, 2, 3, 4, 5) = {min(1, 2, 3, 4, 5)}")
print(
    f"반올림: round(4.6) = {round(4.6)}, round(4.5) = {round(4.5)}, round(4.4) = {round(4.4)}"
)
print(f"버림: math.floor(4.9) = {math.floor(4.9)}")
print(f"올림: math.ceil(4.1) = {math.ceil(4.1)}")
print(f"팩토리얼: math.factorial(5) = {math.factorial(5)}")
print(f"제곱근: math.sqrt(25) = {math.sqrt(25)}")
print(f"파이(π): math.pi = {math.pi}")

# TODO: 삼각함수를 사용하여 sin(30°), cos(60°), tan(45°)의 값을 계산하고 출력해보세요
# 참고: math 함수는 라디안을 사용합니다 (1° = π/180 라디안)
