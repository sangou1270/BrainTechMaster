#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제 해답
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

# 다양한 타입의 요소를 포함하는 리스트
mixed_list = [1, 3.14, "python", True, [1, 2], {"name": "Kim"}]
print(f"mixed_list = {mixed_list}")

# 리스트 인덱싱
print("\n리스트 인덱싱:")
print(f"list1[0] = {list1[0]}")
print(f"list1[3] = {list1[3]}")
print(f"list1[-1] = {list1[-1]}")  # 마지막 요소
print(f"list4[2] = {list4[2]}")  # 리스트 안의 리스트
print(f"list4[2][1] = {list4[2][1]}")  # 리스트 안의 리스트의 요소

# 추가 인덱싱 예제
print(f"list2[-2] = {list2[-2]}")  # 뒤에서 두 번째 요소
print(f"list3[1] + list3[3] = {list3[1] + list3[3]}")  # 문자열 연결
print(f"mixed_list[4][1] = {mixed_list[4][1]}")  # 중첩 리스트 접근
print(f"mixed_list[5]['name'] = {mixed_list[5]['name']}")  # 딕셔너리 요소 접근

# 리스트 슬라이싱
print("\n리스트 슬라이싱:")
print(f"list1[0:3] = {list1[0:3]}")  # 0번째부터 2번째까지
print(f"list1[:3] = {list1[:3]}")  # 처음부터 2번째까지
print(f"list1[2:] = {list1[2:]}")  # 2번째부터 끝까지
print(f"list1[:] = {list1[:]}")  # 전체 복사

# 추가 슬라이싱 예제
print(f"list1[1:4] = {list1[1:4]}")  # 1번째부터 3번째까지
print(f"list1[::2] = {list1[::2]}")  # 처음부터 끝까지 2칸씩 건너뛰기
print(f"list1[::-1] = {list1[::-1]}")  # 역순으로 전체 요소
print(f"list2[1:3] = {list2[1:3]}")  # 문자열 리스트 슬라이싱

# 리스트 연산
print("\n리스트 연산:")
print(f"list1 + list2 = {list1 + list2}")  # 리스트 연결
print(f"list2 * 3 = {list2 * 3}")  # 리스트 반복
print(f"len(list1) = {len(list1)}")  # 리스트 길이

# 추가 연산 예제
joined_list = list3 + list4
print(f"list3 + list4 = {joined_list}")
print(f"list5 + [1, 2, 3] = {list5 + [1, 2, 3]}")  # 빈 리스트에 연결
multiplied_list = ["Hello"] * 5
print(f"['Hello'] * 5 = {multiplied_list}")
print(f"len(joined_list) = {len(joined_list)}")  # 연결된 리스트 길이

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

# 추가 수정 및 삭제 예제
fruits[0] = "apricot"
print(f"fruits[0] = 'apricot' 적용 후: {fruits}")

# 슬라이싱으로 여러 요소 수정
new_fruits = ["strawberry", "grape"]
fruits[1:] = new_fruits
print(f"fruits[1:] = {new_fruits} 적용 후: {fruits}")

# 요소 삭제 (슬라이싱 사용)
del fruits[0:1]
print(f"del fruits[0:1] 적용 후: {fruits}")

# 전체 삭제
fruits_copy = fruits[:]  # 복사본 생성
del fruits_copy[:]
print(f"del fruits_copy[:] 적용 후: {fruits_copy}")

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

# 추가 메서드 예제
# 리스트 내 모든 요소 제거
numbers_copy = numbers[:]
numbers_copy.clear()  # Python 3.3 이상
print(f"numbers_copy.clear() 후: {numbers_copy}")

# 특정 값의 모든 인스턴스 제거
items = [1, 2, 3, 1, 2, 1, 4, 5]
print(f"원래 items: {items}")
while 1 in items:
    items.remove(1)
print(f"1을 모두 제거한 후: {items}")

# 리스트를 스택처럼 사용
stack = [1, 2, 3]
print(f"원래 스택: {stack}")
stack.append(4)  # 요소 추가 (push)
print(f"stack.append(4) 후: {stack}")
popped_item = stack.pop()  # 마지막 요소 제거 (pop)
print(f"stack.pop() 반환값: {popped_item}")
print(f"stack.pop() 후: {stack}")

# 리스트를 큐처럼 사용
from collections import deque

queue = deque([1, 2, 3])
print(f"원래 큐: {queue}")
queue.append(4)  # 요소 추가
print(f"queue.append(4) 후: {queue}")
first_item = queue.popleft()  # 첫 번째 요소 제거
print(f"queue.popleft() 반환값: {first_item}")
print(f"queue.popleft() 후: {queue}")

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

# 추가 리스트 컴프리헨션 예제
# 1부터 20까지의 3의 배수
multiples_of_three = [x for x in range(1, 21) if x % 3 == 0]
print(f"1부터 20까지 3의 배수: {multiples_of_three}")

# 문자열을 개별 문자 리스트로 변환
word = "Python"
chars = [char.lower() for char in word]
print(f"'{word}'의 문자 리스트: {chars}")

# 두 리스트의 모든 조합
list_a = [1, 2]
list_b = ["a", "b"]
combinations = [(a, b) for a in list_a for b in list_b]
print(f"조합: {combinations}")

# 중첩 리스트를 평탄화 (flatten)
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested_list for item in sublist]
print(f"중첩 리스트: {nested_list}")
print(f"평탄화된 리스트: {flattened}")

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

# 추가 리스트 복사 테스트
# 1. 리스트 생성자를 사용한 복사
copy4 = list(original)
# 2. copy 모듈의 copy 함수 사용
copy5 = copy.copy(original)

print("\n다른 복사 방법 사용 후:")
original[1] = 77  # 원본 리스트의 두 번째 요소 변경
original[3][1] = 66  # 원본 리스트의 중첩 리스트 변경

print(f"original = {original}")
print(f"copy4 = {copy4}")  # 얕은 복사 (중첩 리스트는 참조를 공유)
print(f"copy5 = {copy5}")  # 얕은 복사 (중첩 리스트는 참조를 공유)

# 이중 리스트에서 깊은 복사와 얕은 복사의 차이
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = copy.deepcopy(matrix1)  # 깊은 복사
matrix3 = [row[:] for row in matrix1]  # 리스트 컴프리헨션으로 깊은 복사

print("\n행렬 복사:")
print(f"matrix1 = {matrix1}")
print(f"matrix2 = {matrix2}")
print(f"matrix3 = {matrix3}")

matrix1[0][0] = 99

print("\n행렬 수정 후:")
print(f"matrix1 = {matrix1}")
print(f"matrix2 = {matrix2}")  # 깊은 복사 - 원본 변경에 영향 없음
print(f"matrix3 = {matrix3}")  # 리스트 컴프리헨션 복사 - 원본 변경에 영향 없음
