#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제 해답
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

# 자신만의 딕셔너리 생성
my_dict = {
    "movies": ["Inception", "Interstellar", "The Matrix"],
    "scores": {"math": 90, "science": 85, "history": 75},
    "is_valid": True,
    "count": 42,
}
print("\n자신만의 딕셔너리:")
print(f"my_dict = {my_dict}")

# 프로젝트 설정 정보 딕셔너리
config = {
    "version": "1.0.0",
    "debug": True,
    "paths": {
        "data": "/path/to/data",
        "logs": "/path/to/logs",
        "output": "/path/to/output",
    },
    "limits": (100, 200, 300),
}
print(f"config = {config}")

# 딕셔너리 접근
print("\n딕셔너리 접근:")
print(f"dict1['name'] = {dict1['name']}")
print(f"dict2['b'] = {dict2['b']}")
print(f"dict3['list'] = {dict3['list']}")
print(f"dict3['dict']['x'] = {dict3['dict']['x']}")  # 중첩 딕셔너리 접근

# 위에서 생성한 딕셔너리의 여러 키에 접근
print("\n다양한 키 접근:")
print(f"my_dict['movies'][1] = {my_dict['movies'][1]}")  # 리스트 요소
print(f"my_dict['scores']['math'] = {my_dict['scores']['math']}")  # 중첩 딕셔너리
print(f"my_dict['is_valid'] = {my_dict['is_valid']}")  # 불리언 값
print(f"config['paths']['logs'] = {config['paths']['logs']}")  # 중첩 딕셔너리
print(f"config['limits'][1] = {config['limits'][1]}")  # 튜플 요소

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

# 여러 키-값 쌍 추가 및 수정
person["name"] = "Kim Jr."  # 기존 값 수정
person["email"] = "kim@example.com"  # 새 키-값 추가
person["address"] = {"city": "Seoul", "country": "South Korea"}  # 중첩 딕셔너리 추가
person["hobbies"].append("gaming")  # 리스트 값 수정

print("\n여러 수정 및 추가 후:")
print(f"person = {person}")

# 딕셔너리 삭제
print("\n딕셔너리 삭제:")
print(f"삭제 전: {person}")

# 특정 키-값 쌍 삭제
del person["job"]
print(f"del person['job'] 적용 후: {person}")

# 추가 삭제 예제
del person["hobbies"]  # 리스트 값 삭제
print(f"del person['hobbies'] 적용 후: {person}")

# 중첩 딕셔너리에서 키-값 쌍 삭제
del person["address"]["city"]
print(f"del person['address']['city'] 적용 후: {person}")

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

# 추가 get() 예제
print(f"catalog.get('banana') = {catalog.get('banana')}")
print(f"catalog.get('cherry') = {catalog.get('cherry')}")
print(f"catalog.get('cherry', '재고 없음') = {catalog.get('cherry', '재고 없음')}")

# 존재하지 않는 키로 직접 접근하면 KeyError 발생
try:
    price = catalog["cherry"]
except KeyError as e:
    print(f"KeyError 발생: {e}")

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
apple_price = catalog.setdefault("apple", 0)  # 'apple'이 있으므로 그 값 반환
print(f"catalog.setdefault('apple', 0) = {apple_price}")
melon_price = catalog.setdefault("melon", 1200)  # 'melon'이 없으므로 추가 후 1200 반환
print(f"catalog.setdefault('melon', 1200) = {melon_price}")
print(f"catalog.setdefault() 후: {catalog}")

# update(): 딕셔너리 갱신 (여러 키-값 쌍 동시에 추가/수정)
catalog.update(
    {"strawberry": 2000, "apple": 600}
)  # 'apple'은 수정, 'strawberry'는 추가
print(f"catalog.update() 후: {catalog}")

# 추가 딕셔너리 메서드
# copy(): 딕셔너리 복사
catalog_copy = catalog.copy()
print(f"catalog.copy() = {catalog_copy}")

# fromkeys(): 주어진 키와 기본값으로 새 딕셔너리 생성
new_fruits = ["watermelon", "kiwi", "pineapple"]
new_catalog = dict.fromkeys(new_fruits, 0)
print(f"dict.fromkeys(new_fruits, 0) = {new_catalog}")

# 다른 딕셔너리로 여러 항목 갱신
catalog.update(new_catalog)
print(f"catalog.update(new_catalog) 후: {catalog}")

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

# 자신만의 딕셔너리 반복
print("\n사용자 정의 딕셔너리 반복:")
scores = {"Kim": [85, 90, 78], "Lee": [90, 85, 92], "Park": [78, 92, 89]}

# 각 학생의 평균 점수 계산
print("학생별 평균 점수:")
for name, score_list in scores.items():
    average = sum(score_list) / len(score_list)
    print(f"{name}: {average:.1f}")

# 중첩 딕셔너리 반복
print("\n중첩 딕셔너리 반복:")
school = {
    "grade1": {"class1": 30, "class2": 28},
    "grade2": {"class1": 32, "class2": 30},
    "grade3": {"class1": 29, "class2": 31},
}

# 학년별 총 학생 수 계산
for grade, classes in school.items():
    total_students = sum(classes.values())
    print(f"{grade} 총 학생 수: {total_students}명")

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

# 추가 딕셔너리 컴프리헨션 예제
# 문자열 길이를 값으로 가지는 딕셔너리
words = ["apple", "banana", "cherry", "date", "elderberry"]
word_lengths = {word: len(word) for word in words}
print(f"단어 길이 딕셔너리: {word_lengths}")

# 키와 값을 바꾼 딕셔너리 (단, 값이 중복되면 마지막 키-값 쌍만 남음)
inverted_dict = {v: k for k, v in word_lengths.items()}
print(f"키-값 반전 딕셔너리: {inverted_dict}")

# 여러 조건을 포함한 컴프리헨션
complex_dict = {x: "even" if x % 2 == 0 else "odd" for x in range(1, 11)}
print(f"복합 조건 딕셔너리: {complex_dict}")

# 중첩 컴프리헨션
matrix = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print(f"중첩 딕셔너리 컴프리헨션: {matrix}")

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

# 더 긴 문장으로 테스트
longer_text = """
Python is a programming language that lets you work quickly
and integrate systems more effectively. Python is powerful
and fast. Python is a programming language that is easy to learn.
"""
longer_words = longer_text.lower().replace(".", "").replace("\n", " ").split()
longer_counter = Counter(longer_words)
# 가장 흔한 단어 3개
print(f"가장 흔한 단어 3개: {longer_counter.most_common(3)}")

# 2. 학생 정보 관리
students = {
    "20210001": {"name": "Kim", "age": 20, "major": "Computer Science"},
    "20210002": {"name": "Lee", "age": 21, "major": "Mathematics"},
    "20210003": {"name": "Park", "age": 22, "major": "Physics"},
}

# 특정 학생 정보 출력
student_id = "20210002"
print(f"\n학번 {student_id}의 정보:")
print(f"이름: {students[student_id]['name']}")
print(f"나이: {students[student_id]['age']}")
print(f"전공: {students[student_id]['major']}")

# 학생 정보 추가 및 수정
# 새 학생 추가
students["20210004"] = {"name": "Choi", "age": 23, "major": "Chemistry"}
# 기존 학생 정보 수정
students["20210001"]["age"] = 21  # 나이 수정
students["20210003"]["major"] = "Astrophysics"  # 전공 수정

# 모든 학생 정보 출력
print("\n전체 학생 정보:")
for student_id, info in students.items():
    print(f"학번: {student_id}")
    print(f"  이름: {info['name']}")
    print(f"  나이: {info['age']}")
    print(f"  전공: {info['major']}")

# 여러 정보 추가
for student_id, info in students.items():
    # 새 필드 추가: 성적과 이메일
    info["grades"] = {"math": 85, "science": 90, "language": 80}
    info["email"] = f"{info['name'].lower()}@university.com"

# 특정 조건 필터링: 21세 이상 학생
print("\n21세 이상 학생:")
older_students = {id: info for id, info in students.items() if info["age"] >= 21}
for student_id, info in older_students.items():
    print(f"{info['name']} ({student_id}): {info['age']}세")

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

# 메뉴 카테고리와 항목 추가
# 1. 새 카테고리 추가: 주스
menu["juice"] = {"orange": 4500, "apple": 4000, "kiwi": 5000}

# 2. 기존 카테고리에 항목 추가
menu["coffee"]["mocha"] = 4500
menu["dessert"]["tart"] = 4800

# 3. 가격 업데이트
menu["coffee"]["latte"] = 4200

# 업데이트된 메뉴 출력
print("\n===== 업데이트된 카페 메뉴 =====")
for category, items in menu.items():
    print(f"\n[{category.upper()}]")
    for item, price in sorted(items.items()):  # 항목명 알파벳순 정렬
        print(f"{item}: {price}원")

# 메뉴 분석
print("\n메뉴 분석:")
# 1. 가장 비싼 메뉴 항목 찾기
all_items = [
    (f"{category}/{item}", price)
    for category, items in menu.items()
    for item, price in items.items()
]
max_item = max(all_items, key=lambda x: x[1])
print(f"가장 비싼 메뉴: {max_item[0]}, 가격: {max_item[1]}원")

# 2. 카테고리별 평균 가격
for category, items in menu.items():
    avg_price = sum(items.values()) / len(items)
    print(f"{category} 평균 가격: {avg_price:.1f}원")

# 3. 가격대별 메뉴 분류
price_categories = {"저가": [], "중가": [], "고가": []}

for category, items in menu.items():
    for item, price in items.items():
        if price < 3500:
            price_categories["저가"].append(f"{category}/{item} ({price}원)")
        elif price < 4500:
            price_categories["중가"].append(f"{category}/{item} ({price}원)")
        else:
            price_categories["고가"].append(f"{category}/{item} ({price}원)")

print("\n가격대별 메뉴:")
for price_category, menu_items in price_categories.items():
    print(f"{price_category}: {len(menu_items)}개 항목")
    for item in menu_items:
        print(f"  - {item}")

# 주문 시뮬레이션
print("\n주문 시뮬레이션:")
order = [
    ("coffee", "americano", 2),  # 품목, 개수
    ("dessert", "cake", 1),
    ("tea", "green", 1),
]

# 주문 내역 및 금액 계산
total = 0
print("주문 내역:")
for category, item, quantity in order:
    price = menu[category][item]
    item_total = price * quantity
    total += item_total
    print(f"{item} x {quantity}: {item_total}원")

print(f"총 금액: {total}원")
