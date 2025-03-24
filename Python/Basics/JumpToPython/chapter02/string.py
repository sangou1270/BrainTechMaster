#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제
문자열(String) 자료형
"""

# 문자열 생성
str1 = "Hello, Python!"
str2 = "Hello, Python!"
str3 = """여러 줄로
작성된
문자열입니다."""
str4 = """이것도
여러 줄
문자열입니다."""

print("문자열 생성 예제:")
print(f"str1 = {str1}")
print(f"str2 = {str2}")
print(f"str1 == str2: {str1 == str2}")
print(f"str3 = {str3}")
print(f"str4 = {str4}")

# 이스케이프 문자
print("\n이스케이프 문자:")
print("줄바꿈: 첫째 줄\n둘째 줄")
print("탭: 첫째 열\t둘째 열")
print("작은따옴표: '작은따옴표'")
print('큰따옴표: "큰따옴표"')
print("백슬래시: \\")

# TODO: 다양한 이스케이프 문자를 사용하여 출력해보세요

# 문자열 인덱싱
str5 = "Python은 강력합니다."
print("\n문자열 인덱싱:")
print(f"str5 = {str5}")
print(f"str5[0] = {str5[0]}")
print(f"str5[6] = {str5[6]}")
print(f"str5[-1] = {str5[-1]}")  # 뒤에서부터 첫 번째 문자

# TODO: 다양한 인덱스로 문자열의 문자를 출력해보세요

# 문자열 슬라이싱
print("\n문자열 슬라이싱:")
print(f"str5[0:6] = {str5[0:6]}")  # 0번째부터 5번째까지
print(f"str5[7:] = {str5[7:]}")  # 7번째부터 끝까지
print(f"str5[:6] = {str5[:6]}")  # 처음부터 5번째까지
print(f"str5[-3:] = {str5[-3:]}")  # 뒤에서 3번째부터 끝까지

# TODO: 다양한 방식으로 문자열을 슬라이싱하고 결과를 출력해보세요

# 문자열 연산
print("\n문자열 연산:")
str_a = "Python"
str_b = "은 훌륭한 언어입니다"

# 문자열 연결
print(f"str_a + str_b = {str_a + str_b}")

# 문자열 반복
print(f"str_a * 3 = {str_a * 3}")

# 문자열 길이
print(f"len(str_a) = {len(str_a)}")

# TODO: 두 개의 문자열을 정의하고, 연결 및 반복 연산을 수행해보세요

# 문자열 포매팅
print("\n문자열 포매팅:")

# % 연산자 사용
print("내 이름은 %s입니다." % "홍길동")
print("나이는 %d세이고, 키는 %.1f입니다." % (20, 175.5))

# format() 메서드 사용
print("내 이름은 {}입니다.".format("홍길동"))
print("나이는 {}세이고, 키는 {:.1f}입니다.".format(20, 175.5))
print("{0}은 {1}보다 {2}배 더 크다".format("지구", "달", 4))

# f-string 사용 (Python 3.6 이상)
name = "홍길동"
age = 20
height = 175.5
print(f"내 이름은 {name}입니다.")
print(f"나이는 {age}세이고, 키는 {height:.1f}입니다.")
print(f"내년에는 {age + 1}세가 됩니다.")

# TODO: 세 가지 포매팅 방식을 모두 사용하여 자기소개 문장을 출력해보세요

# 문자열 메서드
print("\n문자열 메서드:")
str_c = "python is awesome"

print(f"str_c = {str_c}")
print(f"str_c.upper() = {str_c.upper()}")  # 모두 대문자로
print(f"str_c.capitalize() = {str_c.capitalize()}")  # 첫 글자만 대문자로
print(f"str_c.title() = {str_c.title()}")  # 각 단어의 첫 글자를 대문자로
print(f"str_c.count('o') = {str_c.count('o')}")  # 'o'의 개수
print(f"str_c.find('is') = {str_c.find('is')}")  # 'is'의 위치
print(
    f"str_c.replace('is', 'was') = {str_c.replace('is', 'was')}"
)  # 'is'를 'was'로 대체

# 문자열 분할 및 결합
str_d = "apple,banana,orange,grape"
fruits = str_d.split(",")  # 쉼표로 분할
print(f"str_d = {str_d}")
print(f"str_d.split(',') = {fruits}")
print(f"'-'.join(fruits) = {'-'.join(fruits)}")  # 하이픈으로 결합

# 공백 제거
str_e = "  Hello, World!  "
print(f"str_e = '{str_e}'")
print(f"str_e.strip() = '{str_e.strip()}'")  # 양쪽 공백 제거
print(f"str_e.lstrip() = '{str_e.lstrip()}'")  # 왼쪽 공백 제거
print(f"str_e.rstrip() = '{str_e.rstrip()}'")  # 오른쪽 공백 제거

# TODO: 다양한 문자열 메서드를 사용해보고 결과를 출력해보세요

# 문자열 검사
str_f = "Python3.9"
print("\n문자열 검사:")
print(f"str_f = {str_f}")
print(f"str_f.isalpha() = {str_f.isalpha()}")  # 모두 알파벳인지
print(f"str_f.isalnum() = {str_f.isalnum()}")  # 알파벳 또는 숫자인지
print(f"str_f.isdigit() = {str_f.isdigit()}")  # It's all digits ?
print(f"'3.9'.isdigit() = {'3.9'.isdigit()}")  # 3.9는 숫자일까?
print(f"'39'.isdigit() = {'39'.isdigit()}")  # 39는 숫자일까?

# 문자열 정렬
str_g = "center"
print("\n문자열 정렬:")
print(f"str_g = {str_g}")
print(f"str_g.center(20) = '{str_g.center(20)}'")  # 20칸 중앙 정렬
print(f"str_g.ljust(20) = '{str_g.ljust(20)}'")  # 20칸 왼쪽 정렬
print(f"str_g.rjust(20) = '{str_g.rjust(20)}'")  # 20칸 오른쪽 정렬
print(f"str_g.zfill(10) = '{str_g.zfill(10)}'")  # 10칸 0으로 채우기

# TODO: 다양한 문자열을 정의하고 정렬 메서드를 사용해보세요
