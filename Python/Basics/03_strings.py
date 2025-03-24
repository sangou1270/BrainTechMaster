#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파이썬 문자열 처리 실습 파일
실행 방법: python 03_strings.py
"""

# ==========================================================
# 문자열 기본
# ==========================================================
# 문자열 생성 방법
single_quotes = '작은따옴표 문자열'
double_quotes = "큰따옴표 문자열"
triple_quotes = '''여러 줄
문자열
작성'''
triple_double = """이것도
여러 줄
문자열"""

print("=== 문자열 생성 방법 ===")
print(single_quotes)
print(double_quotes)
print(triple_quotes)
print(triple_double)

# ==========================================================
# 문자열 연산
# ==========================================================
print("\n=== 문자열 연산 ===")
first_name = "길동"
last_name = "홍"

# 문자열 연결 (concatenation)
full_name = last_name + first_name
print("이름:", full_name)

# 문자열 반복
repeated = "Python " * 3
print("반복된 문자열:", repeated)

# ==========================================================
# 문자열 인덱싱과 슬라이싱
# ==========================================================
print("\n=== 문자열 인덱싱과 슬라이싱 ===")
language = "Python Programming"
print("문자열:", language)

# 인덱싱 (indexing) - 개별 문자 접근
print("첫 번째 문자:", language[0])
print("여섯 번째 문자:", language[5])
print("마지막 문자:", language[-1])  # 음수 인덱스는 뒤에서부터 접근

# 슬라이싱 (slicing) - 부분 문자열 추출
print("처음 6글자:", language[0:6])  # 시작 인덱스부터 끝 인덱스 전까지
print("7번째부터 끝까지:", language[7:])  # 끝 인덱스 생략 가능
print("처음부터 6번째까지:", language[:6])  # 시작 인덱스 생략 가능
print("전체 문자열:", language[:])  # 모든 인덱스 생략 가능

# 스텝을 사용한 슬라이싱
print("짝수 인덱스 문자만:", language[::2])  # 스텝 2로 설정
print("문자열 뒤집기:", language[::-1])  # 음수 스텝으로 뒤집기

# ==========================================================
# 문자열 메서드
# ==========================================================
print("\n=== 문자열 메서드 ===")
text = "  Python is amazing  "
print("원본 문자열:", text)

# 대소문자 변환
print("대문자로:", text.upper())
print("소문자로:", text.lower())
print("첫 글자만 대문자로:", text.capitalize())
print("단어별 첫 글자 대문자로:", text.title())

# 공백 제거
print("왼쪽 공백 제거:", text.lstrip())
print("오른쪽 공백 제거:", text.rstrip())
print("양쪽 공백 제거:", text.strip())

# 문자열 검색
print("'Python' 포함 여부:", "Python" in text)
print("'python' 포함 여부:", "python" in text)  # 대소문자 구분
print("'Python' 위치:", text.find("Python"))  # 찾지 못하면 -1 반환
print("'Java' 위치:", text.find("Java"))

# 문자열 대체
new_text = text.replace("Python", "Java")
print("'Python'을 'Java'로 대체:", new_text)

# 문자열 분할
sentence = "Python,Java,C++,JavaScript"
languages = sentence.split(",")
print("쉼표로 분할:", languages)

# 문자열 결합
joined = " | ".join(languages)
print("| 로 결합:", joined)

# ==========================================================
# 문자열 포맷팅
# ==========================================================
print("\n=== 문자열 포맷팅 ===")
name = "홍길동"
age = 30
height = 175.5

# % 연산자 사용 (구식)
old_style = "이름: %s, 나이: %d, 키: %.1f" % (name, age, height)
print("% 스타일:", old_style)

# format() 메서드 사용
format_style = "이름: {}, 나이: {}, 키: {:.1f}".format(name, age, height)
print("format() 스타일:", format_style)

# f-string 사용 (Python 3.6+, 권장)
f_style = f"이름: {name}, 나이: {age}, 키: {height:.1f}"
print("f-string 스타일:", f_style)

# ==========================================================
# 연습 1: 문자열 조작
# ==========================================================
# TODO: 아래 문자열의 모든 공백을 제거하고, 소문자로 변환한 후 출력하세요
sample = "  Python Programming is FUN!  "
# processed = ...
# print(f"처리 결과: {processed}")

# ==========================================================
# 연습 2: 사용자 입력 파싱
# ==========================================================
# TODO: 사용자로부터 쉼표로 구분된 과일 목록을 입력받아, 
# 각 과일을 대문자로 변환하여 출력하세요

# fruits_input = input("과일 목록을 쉼표로 구분하여 입력하세요: ")
# 예시 입력: 사과,바나나,딸기,포도

# fruits_list = ...

# print("입력한 과일 목록:")
# for fruit in fruits_list:
#     upper_fruit = ...
#     print(f"- {upper_fruit}")

# ==========================================================
# 도전 과제: 회문(Palindrome) 검사기
# ==========================================================
# 회문은 앞에서 읽으나 뒤에서 읽으나 같은 단어나 문장입니다.
# 예: "level", "radar", "나만 안 만나" (공백 무시)

# TODO: 사용자로부터 문자열을 입력받아 회문인지 검사하는 코드를 작성하세요
# 힌트: 공백, 대소문자, 특수문자 등을 제거하고 비교해야 합니다

# palindrome_input = input("회문인지 검사할 문자열을 입력하세요: ")
# 예시 입력: 소주 만 병만 주소
# 
# 전처리: 공백 제거, 소문자 변환
# processed_input = ...

# 회문 검사
# is_palindrome = ...

# if is_palindrome:
#     print(f"\"{palindrome_input}\"은(는) 회문입니다!")
# else:
#     print(f"\"{palindrome_input}\"은(는) 회문이 아닙니다.")