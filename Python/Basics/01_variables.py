#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파이썬 변수와 데이터 타입 실습 파일
실행 방법: python 01_variables.py
"""

# ==========================================================
# 변수와 데이터 타입
# ==========================================================

# 정수형 변수 - 여기에 나이를 저장해보세요
age = 25  # 이 값을 변경해보세요
print("나이:", age)

# 실수형 변수 - 여기에 키를 저장해보세요
height = 175.5  # 이 값을 변경해보세요
print("키:", height)

# 문자열 변수 - 여기에 이름을 저장해보세요
name = "홍길동"  # 이 값을 변경해보세요
print("이름:", name)

# 불리언(Boolean) 변수 - 학생 여부를 저장해보세요
is_student = True  # True 또는 False로 변경해보세요
print("학생 여부:", is_student)

# 타입 확인
print("age의 타입:", type(age))
print("name의 타입:", type(name))

# ==========================================================
# 연습 1: 자신의 정보로 변수 업데이트하기
# ==========================================================
# TODO: 아래 변수들을 자신의 정보로 업데이트하세요
my_name = ""
my_age = 0
my_height = 0.0
my_hobby = ""

# TODO: 위 정보를 출력하는 코드를 작성하세요
# print(...)

# ==========================================================
# 연습 2: 변수 값 교환하기
# ==========================================================
# 두 변수의 값을 교환해봅시다
x = 10
y = 20

print("교환 전 - x:", x, "y:", y)

# TODO: x와 y의 값을 교환하는 코드를 작성하세요
# 힌트: 임시 변수를 사용하거나, 파이썬의 특별한 방법을 찾아보세요

print("교환 후 - x:", x, "y:", y)

# ==========================================================
# 연습 3: 형변환 실습
# ==========================================================
# 문자열에서 숫자로 변환
num_str = "123"
# TODO: num_str을 정수로 변환해보세요
# num_int = ...

# 숫자에서 문자열로 변환
num = 456
# TODO: num을 문자열로 변환해보세요
# str_num = ...

# ==========================================================
# 도전 과제: BMI 계산기
# ==========================================================
# BMI(체질량지수)는 체중(kg)을 키(m)의 제곱으로 나눈 값입니다.
# BMI = 체중(kg) / 키(m)²

# TODO: 자신의 키(cm)와 체중(kg)을 입력하세요
# 키는 cm 단위로 입력 후 m로 변환해야 합니다
my_height_cm = 0  # 예: 175
my_weight_kg = 0  # 예: 70

# TODO: BMI를 계산하는 코드를 작성하세요
# 힌트: 키는 cm에서 m로 변환해야 합니다 (나누기 100)
# my_height_m = my_height_cm / 100
# my_bmi = ...

# TODO: 계산된 BMI 값을 출력하세요
# print(f"BMI: {my_bmi:.2f}")