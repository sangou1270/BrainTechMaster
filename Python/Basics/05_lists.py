#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파이썬 리스트 실습 파일
실행 방법: python 05_lists.py
"""

# ==========================================================
# 리스트 생성 및 기본 조작
# ==========================================================
print("=== 리스트 생성 ===")
# 다양한 방식으로 리스트 생성하기
fruits = ["사과", "바나나", "딸기", "오렌지"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "파이썬", True, 3.14]
empty_list = []
range_list = list(range(1, 6))  # 1부터 5까지의 리스트

print("과일 목록:", fruits)
print("숫자 목록:", numbers)
print("혼합 목록:", mixed)
print("빈 리스트:", empty_list)
print("범위 리스트:", range_list)

# ==========================================================
# 리스트 인덱싱과 슬라이싱
# ==========================================================
print("\n=== 리스트 인덱싱과 슬라이싱 ===")
colors = ["빨강", "주황", "노랑", "초록", "파랑", "남색", "보라"]

# 인덱싱 - 개별 요소 접근
print("첫 번째 색상:", colors[0])
print("세 번째 색상:", colors[2])
print("마지막 색상:", colors[-1])
print("뒤에서 두 번째 색상:", colors[-2])

# 슬라이싱 - 부분 리스트 가져오기
print("처음 3개 색상:", colors[0:3])
print("중간 3개 색상:", colors[2:5])
print("마지막 3개 색상:", colors[-3:])
print("처음부터 끝까지, 2개씩 건너뛰며:", colors[::2])
print("리스트 뒤집기:", colors[::-1])

# ==========================================================
# 리스트 수정하기
# ==========================================================
print("\n=== 리스트 수정하기 ===")
shopping_list = ["우유", "빵", "계란", "과일"]
print("원래 쇼핑 목록:", shopping_list)

# 항목 수정
shopping_list[1] = "치즈"
print("빵을 치즈로 변경:", shopping_list)

# 항목 추가
shopping_list.append("요구르트")
print("요구르트 추가 후:", shopping_list)

# 특정 위치에 항목 삽입
shopping_list.insert(2, "초콜릿")
print("2번 인덱스에 초콜릿 삽입 후:", shopping_list)

# 여러 항목 확장
shopping_list.extend(["커피", "주스"])
print("커피와 주스 확장 후:", shopping_list)

# ==========================================================
# 리스트 항목 제거하기
# ==========================================================
print("\n=== 리스트 항목 제거하기 ===")
numbers = [10, 20, 30, 40, 50, 30, 60]
print("원래 숫자 목록:", numbers)

# 인덱스로 제거
removed_item = numbers.pop(2)  # 2번 인덱스(세 번째) 항목 제거 및 반환
print(f"제거된 항목 (numbers.pop(2)): {removed_item}")
print("pop(2) 후:", numbers)

# 마지막 항목 제거
last_item = numbers.pop()
print(f"제거된 마지막 항목: {last_item}")
print("pop() 후:", numbers)

# 값으로 제거
numbers.remove(30)  # 첫 번째로 나오는 30 제거
print("remove(30) 후:", numbers)

# 모든 항목 지우기
numbers_copy = numbers.copy()  # 원본 보존을 위한 복사
numbers_copy.clear()
print("clear() 후:", numbers_copy)

# del 키워드로 제거
del numbers[1]  # 1번 인덱스(두 번째) 항목 제거
print("del numbers[1] 후:", numbers)

# ==========================================================
# 리스트 정보 확인
# ==========================================================
print("\n=== 리스트 정보 확인 ===")
animals = ["강아지", "고양이", "토끼", "햄스터", "고양이", "거북이"]
print("동물 목록:", animals)

# 길이 확인
print("동물 수:", len(animals))

# 항목 개수 세기
print("고양이 수:", animals.count("고양이"))

# 항목 위치 찾기
print("토끼의 인덱스:", animals.index("토끼"))

# 항목 포함 여부 확인
print("'햄스터' 포함 여부:", "햄스터" in animals)
print("'사자' 포함 여부:", "사자" in animals)

# ==========================================================
# 리스트 정렬
# ==========================================================
print("\n=== 리스트 정렬 ===")
scores = [75, 92, 87, 45, 63]
print("원래 점수 목록:", scores)

# 원본 정렬
scores.sort()
print("오름차순 정렬 (sort):", scores)

scores.sort(reverse=True)
print("내림차순 정렬 (sort(reverse=True)):", scores)

# 원본 유지 정렬
names = ["홍길동", "김영희", "이철수", "박지민"]
print("원래 이름 목록:", names)

sorted_names = sorted(names)
print("정렬된 이름 (sorted):", sorted_names)
print("원래 이름 목록 (변경 없음):", names)

# 리스트 뒤집기
names.reverse()
print("뒤집힌 이름 목록 (reverse):", names)

# ==========================================================
# 리스트 복사
# ==========================================================
print("\n=== 리스트 복사 ===")
original = [1, 2, 3, 4, 5]
print("원본 리스트:", original)

# 참조 복사 (얕은 복사) - 동일한 객체를 참조
reference = original
reference[0] = 99
print("참조 복사 후 reference[0] = 99:")
print("reference:", reference)
print("original:", original)  # original도 변경됨

# 얕은 복사 - 새로운 리스트 객체를 생성하지만 내부 객체는 참조
shallow_copy = original.copy()  # list(original) 또는 original[:] 도 가능
shallow_copy[1] = 88
print("\n얕은 복사 후 shallow_copy[1] = 88:")
print("shallow_copy:", shallow_copy)
print("original:", original)  # original은 변경되지 않음

# 깊은 복사 - 모든 내부 객체도 복사
import copy
deep_copy = copy.deepcopy(original)
deep_copy[2] = 77
print("\n깊은 복사 후 deep_copy[2] = 77:")
print("deep_copy:", deep_copy)
print("original:", original)  # original은 변경되지 않음

# ==========================================================
# 리스트 컴프리헨션
# ==========================================================
print("\n=== 리스트 컴프리헨션 ===")
# 일반적인 방법
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("일반적인 방법으로 생성한 제곱 리스트:", squares)

# 리스트 컴프리헨션 사용
squares_comp = [i ** 2 for i in range(1, 6)]
print("리스트 컴프리헨션으로 생성한 제곱 리스트:", squares_comp)

# 조건이 있는 리스트 컴프리헨션
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print("짝수만 제곱한 리스트:", even_squares)

# ==========================================================
# 연습 1: 리스트 조작
# ==========================================================
# TODO: 빈 리스트를 생성한 후, 사용자로부터 5개의 숫자를 입력받아
# 리스트에 추가하고, 합계와 평균을 계산하세요

# user_numbers = []

# 5번 반복하며 숫자 입력받기
# for i in range(5):
#     num = float(input(f"{i+1}번째 숫자를 입력하세요: "))
#     user_numbers.append(num)

# print("입력한 숫자:", user_numbers)
# print(f"합계: {sum(user_numbers)}")
# print(f"평균: {sum(user_numbers) / len(user_numbers)}")

# ==========================================================
# 연습 2: 리스트 필터링
# ==========================================================
# TODO: 다음 문자열 리스트에서 길이가 5 이상인 단어만 추출하여
# 새로운 리스트를 만드세요.

# words = ["apple", "cat", "banana", "dog", "elephant", "car", "butterfly"]

# long_words = []
# 일반적인 방법
# for word in words:
#     if len(word) >= 5:
#         long_words.append(word)

# 리스트 컴프리헨션 방법
# long_words_comp = [word for word in words if len(word) >= 5]

# print("원래 단어 목록:", words)
# print("5글자 이상 단어 (일반 방법):", long_words)
# print("5글자 이상 단어 (컴프리헨션):", long_words_comp)

# ==========================================================
# 도전 과제: 리스트 변환 및 조작
# ==========================================================
# TODO: 주어진 리스트의 각 요소를 제곱하고, 짝수만 필터링하여
# 내림차순으로 정렬하세요

# numbers = [5, 2, 9, 1, 7, 4, 3, 8, 6]

# 변환된 리스트 만들기
# processed = ...

# print("원래 숫자 목록:", numbers)
# print("처리 후 리스트:", processed)
# 예상 결과: [64, 36, 16, 4]