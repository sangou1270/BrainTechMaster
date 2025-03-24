#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제
딕셔너리(Dictionary) 자료형
"""

# 딕셔너리 생성
dict1 = {"name": "Kim", "age": 25, "job": "programmer"}
dict2 = {"a": 1, "b": 2, "c": 3}
dict3 = {"list": [1, 2, 3], "tuple": (4, 5, 6), "dict": {"x": 10, "y": 20}}
dict4 = {}  # 빈 딕셔너리

print("딕셔너리 생성 예제:")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print(f"dict3 = {dict3}")
print(f"dict4 = {dict4}")

# 다른 방식으로 딕셔너리 생성
dict5 = dict(name="Lee", age=30, job="designer")
dict6 = dict([("a", 1), ("b", 2), ("c", 3)])
dict7 = dict(zip(["name", "age", "job"], ["Park", 35, "teacher"]))

print("\n다른 생성 방식:")
print(f"dict5 = {dict5}")
print(f"dict6 = {dict6}")
print(f"dict7 = {dict7}")

# TODO: 자신만의 딕셔너리를 생성해보세요

# 딕셔너리 접근
print("\n딕셔너리 접근:")
print(f"dict1['name'] = {dict1['name']}")
print(f"dict2['b'] = {dict2['b']}")
print(f"dict3['list'] = {dict3['list']}")
print(f"dict3['dict']['x'] = {dict3['dict']['x']}")  # 중첩 딕셔너리 접근

# TODO: 위에서 생성한 딕셔너리의 여러 키에 접근해보세요

# 딕셔너리 수정 및 추가
print("\n딕셔너리 수정 및 추가:")
person = {"name": "Kim", "age": 25}
print(f"원래 딕셔너리: {person}")

# 기존 값 수정
person["age"] = 26
print(f"person['age'] = 26 적용 후: {person}")

# 새 키-값 쌍 추가
person["job"] = "programmer"
print(f"person['job'] = 'programmer' 추가 후: {person}")
person["hobbies"] = ["reading", "hiking", "coding"]
print(f"person['hobbies'] 추가 후: {person}")

# TODO: 딕셔너리에 여러 키-값 쌍을 추가하고 기존 값을 수정해보세요

# 딕셔너리 삭제
print("\n딕셔너리 삭제:")
print(f"삭제 전: {person}")

# 특정 키-값 쌍 삭제
del person["job"]
print(f"del person['job'] 적용 후: {person}")

# TODO: 딕셔너리에서 특정 키-값 쌍을 삭제해보세요

# 딕셔너리 메서드
print("\n딕셔너리 메서드:")
catalog = {"apple": 500, "banana": 700, "orange": 1000, "grape": 1500}
print(f"catalog = {catalog}")

# keys(): 모든 키 반환
keys = catalog.keys()
print(f"catalog.keys() = {keys}")

# values(): 모든 값 반환
values = catalog.values()
print(f"catalog.values() = {values}")

# items(): 모든 키-값 쌍 반환
items = catalog.items()
print(f"catalog.items() = {items}")

# get(): 키로 값 가져오기 (키가 없으면 None 또는 기본값 반환)
print(f"catalog.get('apple') = {catalog.get('apple')}")
print(f"catalog.get('melon') = {catalog.get('melon')}")  # 없는 키
print(f"catalog.get('melon', 0) = {catalog.get('melon', 0)}")  # 기본값 지정

# TODO: get() 메서드를 사용하여 여러 키의 값을 가져와보세요

# clear(): 모든 항목 삭제
temp_dict = catalog.copy()  # 복사본 생성
temp_dict.clear()
print(f"temp_dict.clear() 후: {temp_dict}")

# pop(): 키로 값 가져오고 해당 항목 삭제
fruit = catalog.pop("banana")
print(f"catalog.pop('banana') = {fruit}")
print(f"catalog.pop('banana') 후: {catalog}")

# popitem(): 마지막 키-값 쌍 가져오고 삭제 (Python 3.7+에서는 마지막 삽입 항목)
item = catalog.popitem()
print(f"catalog.popitem() = {item}")
print(f"catalog.popitem() 후: {catalog}")

# setdefault(): 키가 있으면 값 반환, 없으면 키와 기본값 추가 후 기본값 반환
orange_price = catalog.setdefault("apple", 0)  # 'apple'이 있으므로 그 값 반환
print(f"catalog.setdefault('apple', 0) = {orange_price}")
melon_price = catalog.setdefault("melon", 1200)  # 'melon'이 없으므로 추가 후 1200 반환
print(f"catalog.setdefault('melon', 1200) = {melon_price}")
print(f"catalog.setdefault() 후: {catalog}")

# update(): 딕셔너리 갱신 (여러 키-값 쌍 동시에 추가/수정)
catalog.update(
    {"strawberry": 2000, "apple": 600}
)  # 'apple'은 수정, 'strawberry'는 추가
print(f"catalog.update() 후: {catalog}")

# TODO: 여러 딕셔너리 메서드를 사용해보세요

# 딕셔너리 반복문
print("\n딕셔너리 반복문:")
user_info = {"name": "Kim", "age": 30, "email": "kim@example.com"}

# 키로 반복
print("키로 반복:")
for key in user_info:
    print(f"key: {key}, value: {user_info[key]}")

# items()로 키-값 쌍 반복
print("\nitems()로 반복:")
for key, value in user_info.items():
    print(f"key: {key}, value: {value}")

# keys()로 키 반복
print("\nkeys()로 반복:")
for key in user_info.keys():
    print(f"key: {key}")

# values()로 값 반복
print("\nvalues()로 반복:")
for value in user_info.values():
    print(f"value: {value}")

# TODO: 자신만의 딕셔너리를 만들고 for 반복문으로 순회해보세요

# 딕셔너리 컴프리헨션
print("\n딕셔너리 컴프리헨션:")

# 숫자의 제곱 딕셔너리 생성
squares = {x: x**2 for x in range(1, 6)}
print(f"제곱 딕셔너리: {squares}")

# 조건 포함 컴프리헨션
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"짝수 제곱 딕셔너리: {even_squares}")

# 기존 딕셔너리에서 새 딕셔너리 생성
prices = {"apple": 500, "banana": 700, "orange": 1000}
discount_prices = {k: v * 0.9 for k, v in prices.items()}
print(f"할인 가격 딕셔너리: {discount_prices}")

# 두 리스트에서 딕셔너리 생성
fruits = ["apple", "banana", "orange"]
quantities = [3, 5, 2]
fruit_inventory = {f: q for f, q in zip(fruits, quantities)}
print(f"과일 재고 딕셔너리: {fruit_inventory}")

# TODO: 다양한 딕셔너리 컴프리헨션을 만들어보세요

# 딕셔너리 활용 예제
print("\n딕셔너리 활용 예제:")
# 1. 간단한 단어 빈도 카운터
text = "apple banana apple orange banana apple"
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(f"단어 빈도: {word_count}")

# 더 간단한 방법: Counter 클래스 사용
from collections import Counter

word_counter = Counter(words)
print(f"Counter 사용: {word_counter}")

# 2. 학생 정보 관리
students = {
    "20210001": {"name": "Kim", "age": 20, "major": "Computer Science"},
    "20210002": {"name": "Lee", "age": 21, "major": "Mathematics"},
    "20210003": {"name": "Park", "age": 22, "major": "Physics"},
}

# 특정 학생 정보 출력
student_id = "20210002"
print(f"학번 {student_id}의 정보:")
print(f"이름: {students[student_id]['name']}")
print(f"나이: {students[student_id]['age']}")
print(f"전공: {students[student_id]['major']}")

# TODO: 학생 정보를 추가하고 수정해보세요

# 3. 딕셔너리로 간단한 메뉴판 만들기
menu = {
    "coffee": {"americano": 3000, "latte": 4000, "espresso": 2500},
    "tea": {"black": 3500, "green": 3000, "herbal": 3500},
    "dessert": {"cake": 5000, "cookie": 2000, "muffin": 3000},
}

# 메뉴 출력
print("\n===== 카페 메뉴 =====")
for category, items in menu.items():
    print(f"\n[{category.upper()}]")
    for item, price in items.items():
        print(f"{item}: {price}원")

# TODO: 메뉴에 새로운 카테고리와 항목을 추가해보세요
