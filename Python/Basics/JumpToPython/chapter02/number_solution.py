#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제 - 해답
숫자형(Number) 자료형
"""

# 정수형(Integer)
a = 123
b = -178
c = 0

print("정수형 예제:")
print(f"a = {a}, b = {b}, c = {c}")

# 다양한 진수 표현
binary = 0b1010  # 2진수 (10)
octal = 0o12  # 8진수 (10)
hexadecimal = 0xA  # 16진수 (10)

print(f"binary(0b1010) = {binary}")
print(f"octal(0o12) = {octal}")
print(f"hexadecimal(0xA) = {hexadecimal}")
print(f"모두 10진수로 10: {binary == octal == hexadecimal}")

# 실수형(Floating-point)
a = 1.2
b = -3.45
c = 4.24e10  # 4.24 * 10^10
d = 4.24e-10  # 4.24 * 10^-10

print("\n실수형 예제:")
print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# 원하는 실수 값 추가
my_float = 3.14159265359  # 원주율(π)
print(f"my_float(π) = {my_float}")

# 복소수형(Complex Number)
a = 1 + 2j
b = 3 - 4j
c = complex(5, 6)  # 5 + 6j

print("\n복소수형 예제:")
print(f"a = {a}, b = {b}, c = {c}")
print(f"a의 실수부: {a.real}, a의 허수부: {a.imag}")
print(f"a의 켤레복소수: {a.conjugate()}")

# 두 복소수의 덧셈과 곱셈
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")

# 숫자형 연산
print("\n기본 연산:")
print(f"덧셈: 5 + 2 = {5 + 2}")
print(f"뺄셈: 5 - 2 = {5 - 2}")
print(f"곱셈: 5 * 2 = {5 * 2}")
print(f"나눗셈: 5 / 2 = {5 / 2}")  # 나눗셈 결과는 항상 실수
print(f"몫: 5 // 2 = {5 // 2}")  # 소수점 이하를 버린 몫
print(f"나머지: 5 % 2 = {5 % 2}")  # 나머지
print(f"거듭제곱: 5 ** 2 = {5 ** 2}")  # 5의 2제곱

# 세 자리 숫자로 나눗셈과 나머지 연산
num = 1234
divisor = 123
quotient = num // divisor
remainder = num % divisor
print(f"\n{num}을 {divisor}으로 나눈 몫: {quotient}, 나머지: {remainder}")
print(f"검증: {divisor} * {quotient} + {remainder} = {divisor * quotient + remainder}")

# 타입 변환
print("\n타입 변환:")
print(f"int('123') = {int('123')}")
print(f"float('3.14') = {float('3.14')}")
print(f"int(3.14) = {int(3.14)}")  # 소수점 이하는 버림
print(f"float(42) = {float(42)}")
print(f"complex(1, 2) = {complex(1, 2)}")

# 추가적인 형변환 예제
print(f"int('1010', 2) = {int('1010', 2)}")  # 2진수 문자열을 10진수로 변환
print(f"int('12', 8) = {int('12', 8)}")  # 8진수 문자열을 10진수로 변환
print(f"int('A', 16) = {int('A', 16)}")  # 16진수 문자열을 10진수로 변환
print(f"hex(42) = {hex(42)}")  # 10진수를 16진수 문자열로 변환
print(f"oct(42) = {oct(42)}")  # 10진수를 8진수 문자열로 변환
print(f"bin(42) = {bin(42)}")  # 10진수를 2진수 문자열로 변환

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

# 삼각함수 계산
# 각도를 라디안으로 변환: degree * (math.pi / 180)
sin_30 = math.sin(30 * math.pi / 180)
cos_60 = math.cos(60 * math.pi / 180)
tan_45 = math.tan(45 * math.pi / 180)

print("\n삼각함수:")
print(f"sin(30°) = {sin_30:.6f}")
print(f"cos(60°) = {cos_60:.6f}")
print(f"tan(45°) = {tan_45:.6f}")

# 삼각함수 검증
print(f"sin(30°)의 정확한 값은 0.5, 계산값과의 차이: {abs(sin_30 - 0.5)}")
print(f"cos(60°)의 정확한 값은 0.5, 계산값과의 차이: {abs(cos_60 - 0.5)}")
print(f"tan(45°)의 정확한 값은 1.0, 계산값과의 차이: {abs(tan_45 - 1.0)}")

# 추가 예제: 원의 넓이와 둘레 계산
radius = 5
area = math.pi * radius**2
circumference = 2 * math.pi * radius

print("\n반지름이 5인 원:")
print(f"넓이: {area:.2f}")
print(f"둘레: {circumference:.2f}")
