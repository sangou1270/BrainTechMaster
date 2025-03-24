#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파이썬 반복문 실습 파일
실행 방법: python 06_loops.py
"""

# ==========================================================
# for 반복문 기본
# ==========================================================
print("=== 기본 for 반복문 ===")
# 범위(range)를 이용한 반복
print("1부터 5까지 출력:")
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i, end=" ")
print()  # 줄바꿈

# 리스트를 이용한 반복
fruits = ["사과", "바나나", "딸기", "오렌지"]
print("\n과일 목록 출력:")
for fruit in fruits:
    print(fruit, end=" ")
print()

# 문자열을 이용한 반복
message = "Python"
print("\n문자열 한 글자씩 출력:")
for char in message:
    print(char, end=" ")
print()

# ==========================================================
# while 반복문 기본
# ==========================================================
print("\n=== 기본 while 반복문 ===")
# 조건이 참인 동안 반복
count = 1
print("while 사용하여 1부터 5까지 출력:")
while count <= 5:
    print(count, end=" ")
    count += 1
print()

# 사용자 입력에 따른 반복
# 실제 실행 시 주석 해제
"""
print("\n'quit'을 입력할 때까지 메시지 출력:")
message = ""
while message != "quit":
    message = input("메시지를 입력하세요 (종료하려면 'quit' 입력): ")
    if message != "quit":
        print("입력한 메시지:", message)
"""

# ==========================================================
# 루프 제어: break, continue
# ==========================================================
print("\n=== 루프 제어: break, continue ===")
# break - 반복문 완전히 종료
print("break 예제 - 3에서 중단:")
for i in range(1, 6):
    if i == 4:
        break
    print(i, end=" ")
print(" (반복문 종료)")

# continue - 현재 반복을 건너뛰고 다음 반복으로
print("\ncontinue 예제 - 3만 건너뛰기:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print()

# ==========================================================
# 중첩 반복문
# ==========================================================
print("\n=== 중첩 반복문 ===")
# 구구단 예제 (2~4단)
print("구구단 2~4단:")
for i in range(2, 5):
    print(f"\n{i}단:")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}", end="  ")
print()

# ==========================================================
# 반복문과 else
# ==========================================================
print("\n=== 반복문과 else ===")
# for문이 완전히 끝났을 때만 else 실행
print("break 없이 정상 종료:")
for i in range(1, 4):
    print(i, end=" ")
else:
    print("- 반복 완료!")

print("\nbreak로 중간 종료:")
for i in range(1, 4):
    print(i, end=" ")
    if i == 2:
        break
else:
    print("- 반복 완료!")  # break로 중단되면 실행되지 않음
print("- 반복 중단됨")

# ==========================================================
# enumerate 함수
# ==========================================================
print("\n=== enumerate 함수 ===")
colors = ["빨강", "주황", "노랑", "초록"]
print("enumerate 사용 (인덱스와 값):")
for index, color in enumerate(colors):
    print(f"색상 {index}: {color}")

# 시작 인덱스 지정
print("\n시작 인덱스 1로 지정:")
for index, color in enumerate(colors, start=1):
    print(f"색상 {index}: {color}")

# ==========================================================
# 여러 시퀀스 동시 반복 (zip)
# ==========================================================
print("\n=== zip 함수 ===")
names = ["홍길동", "김영희", "이철수"]
ages = [20, 25, 30]
cities = ["서울", "부산", "인천"]

print("zip으로 여러 시퀀스 동시 반복:")
for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}세, {city})")

# ==========================================================
# 리스트 컴프리헨션으로 반복문 간결하게 작성
# ==========================================================
print("\n=== 리스트 컴프리헨션 ===")
# 일반 for문
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("일반 for문 결과:", squares)

# 리스트 컴프리헨션
squares_comp = [i ** 2 for i in range(1, 6)]
print("리스트 컴프리헨션 결과:", squares_comp)

# 조건이 있는 리스트 컴프리헨션
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print("짝수 제곱만 (if 조건):", even_squares)

# 중첩 조건이 있는 리스트 컴프리헨션
complex_list = [f"{i}x{j}" for i in range(2, 5) for j in range(1, 4)]
print("중첩 반복 결과:", complex_list)

# ==========================================================
# 연습 1: 구구단 출력기
# ==========================================================
# TODO: 사용자로부터 출력할 단을 입력받아 해당 구구단을 출력하세요
# dan = int(input("출력할 구구단의 단을 입력하세요 (1-9): "))

# print(f"\n== {dan}단 ==")
# for i in range(1, 10):
#     print(f"{dan} x {i} = {dan * i}")

# ==========================================================
# 연습 2: 소수 찾기
# ==========================================================
# TODO: 2부터 20까지의 숫자 중 소수(prime number)만 출력하세요
# 소수는 1과 자기 자신으로만 나누어지는 1보다 큰 정수입니다

# print("\n2부터 20까지의 소수:")
# for num in range(2, 21):
#     is_prime = True
#     
#     # num이 소수인지 확인하는 코드를 작성하세요
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     
#     if is_prime:
#         print(num, end=" ")
# print()

# ==========================================================
# 연습 3: 피보나치 수열
# ==========================================================
# TODO: 사용자가 입력한 n까지의 피보나치 수열을 출력하세요
# 피보나치 수열: 0, 1, 1, 2, 3, 5, 8, 13, ...
# 각 항은 바로 앞의 두 항의 합입니다

# n = int(input("\n몇 번째 항까지 피보나치 수열을 출력할까요? "))

# fib_numbers = [0, 1]  # 피보나치 수열의 처음 두 항

# 피보나치 수열을 계산하는 코드를 작성하세요
# for i in range(2, n + 1):
#     next_fib = fib_numbers[i-1] + fib_numbers[i-2]
#     fib_numbers.append(next_fib)

# print(f"피보나치 수열 (처음부터 {n}번째 항까지):")
# for i, num in enumerate(fib_numbers[:n+1]):
#     print(f"{i}번째: {num}")

# ==========================================================
# 도전 과제: 별 찍기 패턴
# ==========================================================
# TODO: 다음과 같은 별 찍기 패턴을 출력하세요
# height = 5일 때:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# height = int(input("\n별 패턴의 높이를 입력하세요: "))

# 증가하는 부분
# for i in range(1, height + 1):
#     print("*" * i)

# 감소하는 부분
# for i in range(height - 1, 0, -1):
#     print("*" * i)