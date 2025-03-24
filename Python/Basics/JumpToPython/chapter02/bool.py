#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제
부울(Boolean) 자료형
"""

# 1. 부울 값: True와 False
print("1. 부울 값")
a = True
b = False
print(f"a = {a}")
print(f"b = {b}")
print(f"a의 타입: {type(a)}")
print(f"b의 타입: {type(b)}")

# 2. 비교 연산자의 결과
print("\n2. 비교 연산자")
x, y = 10, 20
print(f"x = {x}, y = {y}")
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# 문자열 비교
str1, str2 = "apple", "banana"
print(f"\nstr1 = '{str1}', str2 = '{str2}'")
print(f"str1 == str2: {str1 == str2}")
print(f"str1 != str2: {str1 != str2}")
print(f"str1 < str2: {str1 < str2}")  # 사전식 순서로 비교
print(f"str1 > str2: {str1 > str2}")

# 객체 비교
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"\nlist1 = {list1}, list2 = {list2}, list3 = list1")
print(f"list1 == list2: {list1 == list2}")  # 값이 같은지 비교
print(f"list1 is list2: {list1 is list2}")  # 동일한 객체인지 비교
print(f"list1 == list3: {list1 == list3}")  # 값이 같은지 비교
print(f"list1 is list3: {list1 is list3}")  # 동일한 객체인지 비교

# 3. 논리 연산자
print("\n3. 논리 연산자")
p, q = True, False
print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # 논리곱
print(f"p or q: {p or q}")  # 논리합
print(f"not p: {not p}")  # 부정

# 논리 연산자의 우선순위
print(f"\n논리 연산자 우선순위")
print(f"True and False or True: {True and False or True}")  # (True and False) or True
print(f"True and (False or True): {True and (False or True)}")
print(f"not True or False: {not True or False}")  # (not True) or False
print(f"not (True or False): {not (True or False)}")

# 4. 부울 값으로 변환 (bool())
print("\n4. bool() 함수")
# 숫자: 0은 False, 나머지는 True
print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f"bool(-1): {bool(-1)}")
print(f"bool(3.14): {bool(3.14)}")

# 문자열: 빈 문자열은 False, 나머지는 True
print(f"bool(''): {bool('')}")
print(f'bool("hello"): {bool("hello")}')

# 컬렉션: 비어있으면 False, 나머지는 True
print(f"bool([]): {bool([])}")
print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")
print(f"bool(()): {bool(())}")
print(f"bool((1, 2)): {bool((1, 2))}")
print(f"bool({{}}): {bool({})}")
print(f"bool({{'a': 1}}): {bool({'a': 1})}")
print(f"bool(set()): {bool(set())}")
print(f"bool({{1, 2}}): {bool({1, 2})}")

# None은 False
print(f"bool(None): {bool(None)}")

# 5. 조건문에서의 부울 값
print("\n5. 조건문에서의 부울 값")
items = []
if items:
    print("items 리스트에 요소가 있습니다.")
else:
    print("items 리스트가 비어 있습니다.")

name = "Python"
if name:
    print(f"이름: {name}")
else:
    print("이름이 지정되지 않았습니다.")

# TODO: 다양한 조건식을 작성하고 그 결과를 확인해보세요.
# 예: 숫자 비교, 문자열 비교, 컬렉션이 비어있는지 확인 등

# 6. 단락 평가 (Short-circuit evaluation)
print("\n6. 단락 평가")


# and 연산에서 첫 번째 피연산자가 False면 두 번째 피연산자는 평가하지 않음
def print_and_return_false():
    print("False 함수가 호출되었습니다.")
    return False


def print_and_return_true():
    print("True 함수가 호출되었습니다.")
    return True


print("False and True 평가:")
result = print_and_return_false() and print_and_return_true()
print(f"결과: {result}")

print("\nTrue and False 평가:")
result = print_and_return_true() and print_and_return_false()
print(f"결과: {result}")

# or 연산에서 첫 번째 피연산자가 True면 두 번째 피연산자는 평가하지 않음
print("\nTrue or False 평가:")
result = print_and_return_true() or print_and_return_false()
print(f"결과: {result}")

print("\nFalse or True 평가:")
result = print_and_return_false() or print_and_return_true()
print(f"결과: {result}")

# 단락 평가를 활용한 코드
print("\n단락 평가 활용 예제:")


# 리스트가 비어있지 않은지 확인 후 첫 번째 요소 접근
def get_first_item(items):
    return (
        items and items[0]
    )  # items가 False(빈 리스트)이면 items 반환, 아니면 items[0] 반환


print(f"get_first_item([1, 2, 3]): {get_first_item([1, 2, 3])}")
print(f"get_first_item([]): {get_first_item([])}")


# 기본값 설정
def get_name(user):
    return user.get("name") or "익명"  # name이 없거나 빈 문자열이면 '익명' 반환


user1 = {"name": "Alice", "age": 30}
user2 = {"name": "", "age": 25}
user3 = {"age": 40}
print(f"get_name(user1): {get_name(user1)}")
print(f"get_name(user2): {get_name(user2)}")
print(f"get_name(user3): {get_name(user3)}")

# 7. 부울 연산의 반환 값
print("\n7. 부울 연산의 반환 값")
# and 연산자는 첫 번째 값이 True면 두 번째 값을 반환, 아니면 첫 번째 값을 반환
print(f"'a' and 'b': {'a' and 'b'}")  # 'b' 반환
print(f"'' and 'b': {'' and 'b'}")  # '' 반환
print(f"0 and 5: {0 and 5}")  # 0 반환
print(f"1 and 5: {1 and 5}")  # 5 반환

# or 연산자는 첫 번째 값이 True면 첫 번째 값을 반환, 아니면 두 번째 값을 반환
print(f"'a' or 'b': {'a' or 'b'}")  # 'a' 반환
print(f"'' or 'b': {'' or 'b'}")  # 'b' 반환
print(f"0 or 5: {0 or 5}")  # 5 반환
print(f"1 or 5: {1 or 5}")  # 1 반환

# 8. 부울 값을 이용한 다양한 예제
print("\n8. 부울 값을 이용한 다양한 예제")

# 조건식을 활용한 리스트 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"짝수: {even_numbers}")


# 함수가 반환하는 부울 값 활용
def is_adult(age):
    return age >= 18


ages = [15, 18, 21, 16, 25, 30]
adults = [age for age in ages if is_adult(age)]
print(f"성인 나이: {adults}")

# any()와 all() 함수
# any(): 하나라도 참이면 True 반환
# all(): 모두 참이어야 True 반환
print("\nany()와 all() 함수:")
print(f"any([False, False, True]): {any([False, False, True])}")
print(f"all([True, True, True]): {all([True, True, True])}")
print(f"all([True, False, True]): {all([True, False, True])}")

# 실제 데이터로 any, all 활용
scores = [85, 92, 78, 90, 88]
print(f"점수 목록: {scores}")
print(f"한 과목이라도 90점 이상인가? {any(score >= 90 for score in scores)}")
print(f"모든 과목이 70점 이상인가? {all(score >= 70 for score in scores)}")
print(f"모든 과목이 80점 이상인가? {all(score >= 80 for score in scores)}")

# 9. 부울 값과 비트 연산자
print("\n9. 부울 값과 비트 연산자")
print(f"True & True: {True & True}")  # 비트 AND: 1 & 1 = 1
print(f"True & False: {True & False}")  # 비트 AND: 1 & 0 = 0
print(f"False & False: {False & False}")  # 비트 AND: 0 & 0 = 0

print(f"True | True: {True | True}")  # 비트 OR: 1 | 1 = 1
print(f"True | False: {True | False}")  # 비트 OR: 1 | 0 = 1
print(f"False | False: {False | False}")  # 비트 OR: 0 | 0 = 0

print(f"True ^ True: {True ^ True}")  # 비트 XOR: 1 ^ 1 = 0
print(f"True ^ False: {True ^ False}")  # 비트 XOR: 1 ^ 0 = 1
print(f"False ^ False: {False ^ False}")  # 비트 XOR: 0 ^ 0 = 0

# 논리 연산자(and, or, not)와 비트 연산자(&, |, ^)의 차이
print("\n논리 연산자와 비트 연산자의 차이:")
x, y = True, False
print(f"논리 연산자: {x and y}")  # 단락 평가 발생
print(f"비트 연산자: {x & y}")  # 단락 평가 발생하지 않음
