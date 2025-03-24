#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제
집합(Set) 자료형
"""

# 집합 생성
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {1, 2, 3, 3, 4, 4, 5}  # 중복 요소는 제거됨
set4 = set()  # 빈 집합 (주의: {}는 빈 딕셔너리)
set5 = set([1, 2, 3, 4, 5])  # 리스트로부터 집합 생성
set6 = set("Hello")  # 문자열로부터 집합 생성 (중복 문자 제거)

print("집합 생성 예제:")
print(f"set1 = {set1}")
print(f"set2 = {set2}")
print(f"set3 = {set3}")  # 중복이 제거됨
print(f"set4 = {set4}")
print(f"set5 = {set5}")
print(f"set6 = {set6}")  # 순서가 보장되지 않음

# TODO: 다양한 방식으로 집합을 생성해보세요

# 집합의 특징
# 1. 중복 제거
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("\n중복 제거 예제:")
print(f"numbers = {numbers}")
print(f"set(numbers) = {unique_numbers}")
print(f"다시 리스트로: {list(unique_numbers)}")

# 2. 순서가 없음 (인덱싱 불가)
# print(set1[0])  # TypeError: 'set' object is not subscriptable

# 3. 집합 연산
print("\n집합 연산:")
print(f"set1 = {set1}")
print(f"set2 = {set2}")

# 합집합
union1 = set1 | set2  # 연산자 사용
union2 = set1.union(set2)  # 메서드 사용
print(f"set1 | set2 = {union1}")
print(f"set1.union(set2) = {union2}")

# 교집합
intersection1 = set1 & set2  # 연산자 사용
intersection2 = set1.intersection(set2)  # 메서드 사용
print(f"set1 & set2 = {intersection1}")
print(f"set1.intersection(set2) = {intersection2}")

# 차집합
difference1 = set1 - set2  # 연산자 사용
difference2 = set1.difference(set2)  # 메서드 사용
print(f"set1 - set2 = {difference1}")
print(f"set1.difference(set2) = {difference2}")

# 대칭 차집합 (합집합 - 교집합)
symmetric_diff1 = set1 ^ set2  # 연산자 사용
symmetric_diff2 = set1.symmetric_difference(set2)  # 메서드 사용
print(f"set1 ^ set2 = {symmetric_diff1}")
print(f"set1.symmetric_difference(set2) = {symmetric_diff2}")

# TODO: 집합 연산을 사용하여 다양한 집합을 만들어보세요

# 집합 메서드
print("\n집합 메서드:")
s = {1, 2, 3}
print(f"s = {s}")

# add(): 요소 추가
s.add(4)
print(f"s.add(4) 후: {s}")

# update(): 여러 요소 추가
s.update([5, 6, 7])
print(f"s.update([5, 6, 7]) 후: {s}")

# remove(): 요소 제거 (요소가 없으면 KeyError)
s.remove(2)
print(f"s.remove(2) 후: {s}")

# discard(): 요소 제거 (요소가 없어도 에러 없음)
s.discard(10)  # 10은 없지만 에러 발생 안 함
print(f"s.discard(10) 후: {s}")

# pop(): 임의의 요소 제거 및 반환
popped = s.pop()
print(f"s.pop() = {popped}")
print(f"s.pop() 후: {s}")

# clear(): 모든 요소 제거
s_copy = s.copy()  # 복사본 생성
s_copy.clear()
print(f"s_copy.clear() 후: {s_copy}")

# TODO: 다양한 집합 메서드를 사용해보세요

# 집합 연산 관련 메서드
print("\n집합 연산 관련 메서드:")
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"a = {a}")
print(f"b = {b}")

# update(): 합집합 결과를 원본에 반영
a_copy = a.copy()
a_copy.update(b)
print(f"a.update(b) 후: {a_copy}")

# intersection_update(): 교집합 결과를 원본에 반영
a_copy = a.copy()
a_copy.intersection_update(b)
print(f"a.intersection_update(b) 후: {a_copy}")

# difference_update(): 차집합 결과를 원본에 반영
a_copy = a.copy()
a_copy.difference_update(b)
print(f"a.difference_update(b) 후: {a_copy}")

# symmetric_difference_update(): 대칭차집합 결과를 원본에 반영
a_copy = a.copy()
a_copy.symmetric_difference_update(b)
print(f"a.symmetric_difference_update(b) 후: {a_copy}")

# TODO: 집합 연산 메서드를 사용해보세요

# 집합 포함 관계 판단
print("\n집합 포함 관계:")
x = {1, 2, 3, 4, 5}
y = {1, 2, 3}
z = {1, 2, 3, 4, 5, 6}
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

# issubset(): 부분집합 여부
print(f"y.issubset(x) = {y.issubset(x)}")  # y가 x의 부분집합인가?
print(f"y <= x = {y <= x}")  # 연산자 사용
print(f"x.issubset(y) = {x.issubset(y)}")  # x가 y의 부분집합인가?
print(f"x <= y = {x <= y}")  # 연산자 사용

# issuperset(): 상위집합 여부
print(f"x.issuperset(y) = {x.issuperset(y)}")  # x가 y의 상위집합인가?
print(f"x >= y = {x >= y}")  # 연산자 사용
print(f"y.issuperset(x) = {y.issuperset(x)}")  # y가 x의 상위집합인가?
print(f"y >= x = {y >= x}")  # 연산자 사용

# 진부분집합/진상위집합
print(f"y < x = {y < x}")  # y가 x의 진부분집합인가?
print(f"x < z = {x < z}")  # x가 z의 진부분집합인가?
print(f"z > x = {z > x}")  # z가 x의 진상위집합인가?

# isdisjoint(): 두 집합이 공통 요소가 없는지 여부
w = {7, 8, 9}
print(f"x = {x}")
print(f"w = {w}")
print(f"x.isdisjoint(w) = {x.isdisjoint(w)}")  # x와 w가 공통 요소가 없는가?
print(f"x.isdisjoint(y) = {x.isdisjoint(y)}")  # x와 y가 공통 요소가 없는가?

# TODO: 집합 간의 포함 관계를 판단해보세요

# 집합 컴프리헨션
print("\n집합 컴프리헨션:")
# 1부터 10까지의 제곱 집합
squares = {x**2 for x in range(1, 11)}
print(f"제곱 집합: {squares}")

# 짝수만 포함하는 집합
even_numbers = {x for x in range(1, 21) if x % 2 == 0}
print(f"짝수 집합: {even_numbers}")

# 문자열에서 모음만 추출
vowels = {"a", "e", "i", "o", "u"}
text = "Hello Python Programming"
vowels_in_text = {char.lower() for char in text if char.lower() in vowels}
print(f"문장의 모음 집합: {vowels_in_text}")

# TODO: 다양한 집합 컴프리헨션을 만들어보세요

# 집합 활용 예제
print("\n집합 활용 예제:")

# 1. 중복 제거
fruits = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
unique_fruits = set(fruits)
print(f"원래 리스트: {fruits}")
print(f"중복 제거 후: {unique_fruits}")
print(f"정렬된 중복 제거 리스트: {sorted(unique_fruits)}")

# 2. 공통 요소 찾기
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"공통 요소: {common}")

# 3. 리스트 간 유일한 요소 찾기
unique_to_list1 = set(list1) - set(list2)
unique_to_list2 = set(list2) - set(list1)
print(f"list1에만 있는 요소: {unique_to_list1}")
print(f"list2에만 있는 요소: {unique_to_list2}")

# 4. 모든 유일한 요소 찾기
all_unique = set(list1) ^ set(list2)
print(f"두 리스트의 유일한 요소 모음: {all_unique}")

# TODO: 집합을 활용한 실제 문제를 해결해보세요

# 불변 집합 (frozenset)
print("\n불변 집합 (frozenset):")
normal_set = {1, 2, 3, 4}
frozen_set = frozenset([1, 2, 3, 4])

print(f"일반 집합: {normal_set}")
print(f"불변 집합: {frozen_set}")

# 일반 집합은 수정 가능
normal_set.add(5)
print(f"normal_set.add(5) 후: {normal_set}")

# 불변 집합은 수정 불가
# frozen_set.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'

# 불변 집합은 딕셔너리 키나 다른 집합의 요소로 사용 가능
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
dict_with_frozenset_keys = {
    frozenset([1, 2]): "첫 번째 집합",
    frozenset([3, 4]): "두 번째 집합",
}
print(f"집합의 집합: {set_of_sets}")
print(f"불변 집합을 키로 갖는 딕셔너리: {dict_with_frozenset_keys}")

# TODO: 불변 집합을 사용해보세요
