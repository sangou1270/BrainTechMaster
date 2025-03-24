#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제
리스트(List) 자료형
"""

# 리스트 생성
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d"]
list3 = [1, "a", 2, "b"]
list4 = [1, 2, ["a", "b", "c"]]
list5 = []  # 빈 리스트

print("리스트 생성 예제:")
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")
print(f"list4 = {list4}")
print(f"list5 = {list5}")

# TODO: 다양한 타입의 요소를 포함하는 리스트를 하나 더 만들어보세요

# 리스트 인덱싱
print("\n리스트 인덱싱:")
print(f"list1[0] = {list1[0]}")
print(f"list1[3] = {list1[3]}")
print(f"list1[-1] = {list1[-1]}")  # 마지막 요소
print(f"list4[2] = {list4[2]}")  # 리스트 안의 리스트
print(f"list4[2][1] = {list4[2][1]}")  # 리스트 안의 리스트의 요소

# TODO: 리스트 인덱싱을 사용하여 다양한 요소에 접근해보세요

# 리스트 슬라이싱
print("\n리스트 슬라이싱:")
print(f"list1[0:3] = {list1[0:3]}")  # 0번째부터 2번째까지
print(f"list1[:3] = {list1[:3]}")  # 처음부터 2번째까지
print(f"list1[2:] = {list1[2:]}")  # 2번째부터 끝까지
print(f"list1[:] = {list1[:]}")  # 전체 복사

# TODO: 다양한 슬라이싱 방법을 사용해보세요

# 리스트 연산
print("\n리스트 연산:")
print(f"list1 + list2 = {list1 + list2}")  # 리스트 연결
print(f"list2 * 3 = {list2 * 3}")  # 리스트 반복
print(f"len(list1) = {len(list1)}")  # 리스트 길이

# TODO: 리스트 연산 예제를 추가해보세요

# 리스트 수정과 삭제
print("\n리스트 수정과 삭제:")
fruits = ["apple", "banana", "cherry", "date"]
print(f"원래 리스트: {fruits}")

# 요소 수정
fruits[1] = "blueberry"
print(f"fruits[1] = 'blueberry' 적용 후: {fruits}")

# 요소 삭제
del fruits[2]
print(f"del fruits[2] 적용 후: {fruits}")

# 전체 삭제
# del fruits[:]
# print(f"del fruits[:] 적용 후: {fruits}")

# TODO: 리스트의 특정 요소를 수정하고 삭제해보세요

# 리스트 메서드
print("\n리스트 메서드:")
numbers = [1, 2, 3]
print(f"원래 리스트: {numbers}")

# 요소 추가
numbers.append(4)
print(f"numbers.append(4) 후: {numbers}")

# 정렬
mixed = [5, 2, 8, 1, 9]
print(f"정렬 전: {mixed}")
mixed.sort()
print(f"mixed.sort() 후: {mixed}")
mixed.sort(reverse=True)
print(f"mixed.sort(reverse=True) 후: {mixed}")

# 뒤집기
numbers.reverse()
print(f"numbers.reverse() 후: {numbers}")

# 인덱스 찾기
colors = ["red", "green", "blue", "green", "yellow"]
print(f"colors = {colors}")
print(f"colors.index('blue') = {colors.index('blue')}")

# 요소 삽입
colors.insert(2, "purple")
print(f"colors.insert(2, 'purple') 후: {colors}")

# 요소 제거
colors.remove("green")  # 첫 번째로 나오는 'green'을 제거
print(f"colors.remove('green') 후: {colors}")

# 마지막 요소 추출
last_color = colors.pop()
print(f"colors.pop() 반환값: {last_color}")
print(f"colors.pop() 후: {colors}")

# 특정 위치 요소 추출
second_color = colors.pop(1)
print(f"colors.pop(1) 반환값: {second_color}")
print(f"colors.pop(1) 후: {colors}")

# 요소 개수 세기
colors.append("red")
print(f"colors 추가 후: {colors}")
print(f"colors.count('red') = {colors.count('red')}")

# 리스트 확장
colors.extend(["orange", "pink"])
print(f"colors.extend(['orange', 'pink']) 후: {colors}")

# 요소 모두 지우기
# colors.clear()  # Python 3.3 이상
# print(f"colors.clear() 후: {colors}")

# TODO: 여러 리스트 메서드를 실험해보세요

# 리스트 컴프리헨션 (List Comprehension)
print("\n리스트 컴프리헨션:")
# 1부터 10까지의 제곱 리스트
squares = [x**2 for x in range(1, 11)]
print(f"[x**2 for x in range(1, 11)] = {squares}")

# 짝수만 포함하는 리스트
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"[x for x in range(1, 11) if x % 2 == 0] = {even_numbers}")

# 문자열 리스트에서 길이가 3 이상인 것만 대문자로 변환
words = ["hi", "hello", "bye", "goodbye"]
long_words_upper = [word.upper() for word in words if len(word) >= 3]
print(f"words = {words}")
print(f"[word.upper() for word in words if len(word) >= 3] = {long_words_upper}")

# 중첩 반복문으로 좌표 생성
coordinates = [(x, y) for x in range(1, 4) for y in range(1, 3)]
print(f"[(x, y) for x in range(1, 4) for y in range(1, 3)] = {coordinates}")

# TODO: 리스트 컴프리헨션을 사용하여 다양한 리스트를 생성해보세요

# 리스트 복사
print("\n리스트 복사:")
original = [1, 2, 3, [4, 5]]
copy1 = original  # 참조 복사
copy2 = original[:]  # 얕은 복사
import copy

copy3 = copy.deepcopy(original)  # 깊은 복사

print(f"original = {original}")
print(f"copy1 = {copy1}")
print(f"copy2 = {copy2}")
print(f"copy3 = {copy3}")

# 원본 리스트 수정
original[0] = 99
original[3][0] = 88

print("\n원본 리스트 수정 후:")
print(f"original = {original}")
print(f"copy1 = {copy1}")  # 참조 복사는 원본이 변경되면 같이 변경됨
print(f"copy2 = {copy2}")  # 얕은 복사는 중첩 리스트는 참조를 공유함
print(f"copy3 = {copy3}")  # 깊은 복사는 완전히 독립적인 객체

# TODO: 리스트 복사의 세 가지 방식을 테스트해보세요
