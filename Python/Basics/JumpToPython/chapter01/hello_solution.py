#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 1장 예제 - 해답
파이썬이란 무엇인가?
"""

# 기본 Hello World 출력
print("Hello, World!")

# 이름을 추가하여 출력
name = "파이썬 학습자"
print(f"안녕하세요, {name}님!")

# 간단한 계산 결과 출력
print("1 + 2 =", 1 + 2)
print("5 * 7 =", 5 * 7)
print("10 / 3 =", 10 / 3)
print("10 // 3 =", 10 // 3)  # 몫
print("10 % 3 =", 10 % 3)  # 나머지
print("2 ** 10 =", 2**10)  # 거듭제곱

# 다양한 출력 방법
print("파이썬은", "쉽고", "강력한", "언어입니다.")
print("파이썬은 " + "인터프리터 " + "언어입니다.")
print("=" * 50)  # 문자열 반복

# 파이썬을 배우는 이유
print(
    "파이썬을 배우는 이유: 간결하고 읽기 쉬운 문법으로 빠르게 개발할 수 있기 때문입니다."
)

"""
파이썬의 특징:
1. 인터프리터 언어
2. 객체지향 언어
3. 동적 타이핑 언어
4. 엄격한 들여쓰기 규칙
5. 풍부한 라이브러리
"""

# 추가 예제: 파이썬 버전 확인
import sys

print("\n파이썬 버전 정보:")
print(sys.version)
print("=" * 50)

# 간단한 대화형 예제
print("\n간단한 대화형 프로그램:")
user_input = input("당신의 이름은 무엇인가요? ")
print(f"반갑습니다, {user_input}님!")

# 현재 날짜와 시간 출력
import datetime

now = datetime.datetime.now()
print(f"\n현재 날짜와 시간: {now}")
print(f"오늘은 {now.year}년 {now.month}월 {now.day}일입니다.")
