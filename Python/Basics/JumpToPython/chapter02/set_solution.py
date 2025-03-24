#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제 해답
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

# 다양한 방식으로 집합 생성
# 튜플로부터 집합 생성
set7 = set((10, 20, 30, 40, 50))
# 딕셔너리로부터 집합 생성 (키만 포함)
set8 = set({"a": 1, "b": 2, "c": 3})
# 제너레이터 표현식으로부터 집합 생성
set9 = set(x for x in range(1, 6))
# 다양한 자료형을 포함하는 집합
set10 = {1, "a", True, (1, 2), 3.14}

print("\n다양한 집합 생성 방식:")
print(f"set7 = {set7}")
print(f"set8 = {set8}")
print(f"set9 = {set9}")
print(f"set10 = {set10}")

# 집합의 특징
# 1. 중복 제거
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("\n중복 제거 예제:")
print(f"numbers = {numbers}")
print(f"set(numbers) = {unique_numbers}")
print(f"다시 리스트로: {list(unique_numbers)}")

# 두 번째 중복 제거 예제: 문자열에서 고유 문자 추출
sentence = "Python programming is fun and interesting"
unique_chars = set(sentence.lower().replace(" ", ""))
print(f"원래 문장: {sentence}")
print(f"고유 문자: {unique_chars}")
print(f"고유 문자 수: {len(unique_chars)}")

# 2. 순서가 없음 (인덱싱 불가)
try:
    print(set1[0])
except TypeError as e:
    print(f"집합 인덱싱 오류: {e}")

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

# 집합 연산을 사용하여 다양한 집합 만들기
# 세 집합의 연산
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {5, 6, 7, 8}

# 세 집합의 합집합
union_all = set_a | set_b | set_c
print(f"\n세 집합의 합집합: {union_all}")

# 세 집합의 교집합
intersection_all = set_a & set_b & set_c
print(f"세 집합의 교집합: {intersection_all}")  # 공통 요소가 없으면 빈 집합

# 세 집합의 교집합이 없어서 빈 집합이 나옴. 두 집합씩 교집합을 구해보자
intersection_ab = set_a & set_b
intersection_bc = set_b & set_c
print(f"set_a와 set_b의 교집합: {intersection_ab}")
print(f"set_b와 set_c의 교집합: {intersection_bc}")

# A-(B∪C): A에는 속하지만 B 또는 C에는 속하지 않는 요소
only_in_a = set_a - (set_b | set_c)
print(f"set_a에만 있는 요소: {only_in_a}")

# 복합 집합 연산
complex_set = (set_a & set_b) | (set_b & set_c)
print(f"(A∩B)∪(B∩C): {complex_set}")

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

# 존재하지 않는 요소 제거 시도
try:
    s.remove(10)
except KeyError as e:
    print(f"KeyError 발생: {e}")

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

# 다양한 집합 메서드 추가 예제
elements = {10, 20, 30, 40, 50}
print(f"\n원래 집합: {elements}")

# 복사본 만들기
elements_copy = elements.copy()
print(f"elements.copy() = {elements_copy}")

# 여러 요소 추가
elements.update([60, 70], {80, 90}, (100, 110))
print(f"여러 요소 추가 후: {elements}")

# 빈 집합 확인 메서드
print(f"elements가 비어있나요? {not elements}")  # 빈 집합은 False 값을 가짐
print(f"비어있는 집합(s_copy)가 비어있나요? {not s_copy}")  # 빈 집합은 False 값을 가짐

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

# 집합 연산 메서드 추가 예제
print("\n집합 연산 메서드 추가 예제:")
languages1 = {"Python", "Java", "C++", "JavaScript"}
languages2 = {"JavaScript", "TypeScript", "Python", "PHP"}
languages3 = {"Ruby", "Swift", "Kotlin"}

# 여러 집합의 합집합
result = languages1.copy()
result.update(languages2, languages3)
print(f"모든 언어: {result}")

# 특정 언어만 제거
result = languages1.copy()
to_remove = {"Java", "C++"}
result.difference_update(to_remove)
print(f"Python과 JavaScript만 남기기: {result}")

# 두 언어 목록의 공통 언어 찾기
common_languages = languages1.copy()
common_languages.intersection_update(languages2)
print(f"공통 언어: {common_languages}")

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

# 집합 간의 포함 관계 판단 추가 예제
# 추가 집합 정의
animal_types = {"포유류", "조류", "파충류", "양서류", "어류"}
mammals = {"개", "고양이", "소", "말", "원숭이"}
pets = {"개", "고양이", "햄스터", "앵무새", "금붕어"}
dogs = {"진돗개", "리트리버", "셰퍼드", "불독"}

# 포함 관계 테스트
print("\n추가 포함 관계 예제:")
print(
    f"모든 개는 포유류인가? {dogs.issubset(mammals)}"
)  # False: 실제 dogs는 개 품종들이지 개체가 아님
print(
    f"모든 포유류는 동물 타입인가? {set(mammals).issubset(animal_types)}"
)  # False: set 끼리의 관계가 아니라 요소의 관계를 볼 수 없음

# 진부분집합 vs 부분집합
a = {1, 2, 3}
b = {1, 2, 3}
c = {1, 2, 3, 4}
print(f"a = {a}, b = {b}, c = {c}")
print(f"a는 b의 부분집합인가? {a.issubset(b)}")  # True
print(f"a는 b의 진부분집합인가? {a < b}")  # False: a와 b는 같은 집합
print(f"a는 c의 부분집합인가? {a.issubset(c)}")  # True
print(f"a는 c의 진부분집합인가? {a < c}")  # True: a는 c의 진부분집합

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

# 추가 집합 컴프리헨션 예제
# 1. 3의 배수와 5의 배수 집합
multiples_of_3 = {x for x in range(1, 31) if x % 3 == 0}
multiples_of_5 = {x for x in range(1, 31) if x % 5 == 0}
print(f"\n1부터 30까지 3의 배수: {multiples_of_3}")
print(f"1부터 30까지 5의 배수: {multiples_of_5}")
print(f"3의 배수이거나 5의 배수: {multiples_of_3 | multiples_of_5}")

# 2. 문장에서 각 단어의 첫 글자 집합
sentence = "The quick brown fox jumps over the lazy dog"
first_letters = {word[0].lower() for word in sentence.split()}
print(f"문장의 각 단어 첫 글자: {first_letters}")

# 3. 두 리스트의 곱집합(cartesian product)의 합
list1 = [1, 2, 3]
list2 = ["a", "b"]
products = {f"{num}{char}" for num in list1 for char in list2}
print(f"곱집합: {products}")

# 4. 소수 집합 (20 이하)
non_primes = {j for i in range(2, 5) for j in range(i * 2, 21, i)}
primes = {i for i in range(2, 21)} - non_primes
print(f"20 이하의 소수: {primes}")

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

# 집합을 활용한 실제 문제 해결
# 1. 투표 결과에서 고유한 후보자 찾기
votes = ["Kim", "Lee", "Park", "Kim", "Lee", "Lee", "Choi", "Kim", "Choi", "Park"]
candidates = set(votes)
print(f"\n투표 결과: {votes}")
print(f"후보자 목록: {candidates}")
print(f"후보자 수: {len(candidates)}")

# 2. 여러 텍스트 파일에서 공통 단어 찾기
file1_words = {
    "Python",
    "is",
    "a",
    "programming",
    "language",
    "that",
    "is",
    "easy",
    "to",
    "learn",
}
file2_words = {
    "Python",
    "is",
    "widely",
    "used",
    "in",
    "data",
    "science",
    "and",
    "machine",
    "learning",
}
file3_words = {
    "Python",
    "has",
    "a",
    "large",
    "standard",
    "library",
    "that",
    "is",
    "easy",
    "to",
    "use",
}

# 모든 파일에 공통으로 등장하는 단어
common_words = file1_words & file2_words & file3_words
print(f"모든 파일에 공통으로 등장하는 단어: {common_words}")

# 적어도 2개 이상의 파일에서 등장하는 단어
at_least_two_files = (
    (file1_words & file2_words)
    | (file2_words & file3_words)
    | (file1_words & file3_words)
)
print(f"적어도 2개 이상의 파일에서 등장하는 단어: {at_least_two_files}")

# 3. 친구 관계 분석
# 각 사람의 친구 집합
alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "Eve"}
charlie_friends = {"Alice", "Bob", "David", "Frank"}

# 공통 친구 찾기
alice_bob_common = alice_friends & bob_friends
print(f"Alice와 Bob의 공통 친구: {alice_bob_common}")

# 한 사람만 아는 친구 찾기
only_alice_friends = alice_friends - (bob_friends | charlie_friends)
print(f"Alice만 아는 친구: {only_alice_friends}")

# 모든 친구 목록
all_friends = alice_friends | bob_friends | charlie_friends
print(f"모든 친구 목록: {all_friends}")

# 4. URL 파라미터 분석
url1_params = {"id", "name", "page", "sort"}
url2_params = {"id", "category", "filter", "sort"}
url3_params = {"id", "name", "category", "page"}

# 모든 URL에 공통으로 있는의 파라미터
common_params = url1_params & url2_params & url3_params
print(f"모든 URL에 공통 파라미터: {common_params}")

# 어떤 URL에도 있는 모든 파라미터
all_params = url1_params | url2_params | url3_params
print(f"모든 URL 파라미터 집합: {all_params}")

# 5. 집합을 활용한 간단한 검색 엔진
documents = [
    {"id": 1, "keywords": {"python", "programming", "tutorial", "beginner"}},
    {"id": 2, "keywords": {"python", "machine", "learning", "advanced"}},
    {"id": 3, "keywords": {"web", "development", "html", "css", "javascript"}},
    {"id": 4, "keywords": {"data", "science", "python", "statistics"}},
    {"id": 5, "keywords": {"mobile", "app", "development", "ios", "android"}},
]

# 검색어로 문서 찾기
search_terms = {"python", "development"}
print("\n검색 결과:")
for doc in documents:
    # 검색어 중 하나라도 포함된 문서 찾기
    if not search_terms.isdisjoint(doc["keywords"]):
        # 일치하는 키워드 수에 따라 관련성 점수 계산
        relevance = len(search_terms & doc["keywords"]) / len(search_terms) * 100
        print(
            f"문서 ID: {doc['id']}, 키워드: {doc['keywords']}, 관련성: {relevance:.1f}%"
        )

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
try:
    frozen_set.add(5)
except AttributeError as e:
    print(f"불변 집합 수정 시도 오류: {e}")

# 불변 집합은 해시 가능하므로 딕셔너리 키나 다른 집합의 요소로 사용 가능
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
dict_with_frozenset_keys = {
    frozenset([1, 2]): "첫 번째 집합",
    frozenset([3, 4]): "두 번째 집합",
}
print(f"집합의 집합: {set_of_sets}")
print(f"불변 집합을 키로 갖는 딕셔너리: {dict_with_frozenset_keys}")
print(f"딕셔너리 값 접근: {dict_with_frozenset_keys[frozenset([1, 2])]}")


# 불변 집합 사용 예제
# 1. 캐싱에 사용하기
def get_factors(n):
    """주어진 수의 약수 집합을 반환합니다."""
    return frozenset(i for i in range(1, n + 1) if n % i == 0)


# 각 숫자의 약수 집합을 저장하는 딕셔너리
factor_cache = {}

# 1부터 10까지 각 숫자의 약수 계산
for i in range(1, 11):
    factors = get_factors(i)
    factor_cache[i] = factors
    print(f"{i}의 약수: {factors}")

# 공통 약수 찾기
print(f"6과 8의 공통 약수: {factor_cache[6] & factor_cache[8]}")

# 2. frozenset을 사용하여 중첩 집합 생성
teams = {
    frozenset(["Alice", "Bob"]): "Team 1",
    frozenset(["Charlie", "David"]): "Team 2",
    frozenset(["Eve", "Frank"]): "Team 3",
}

# 팀원으로 팀 이름 찾기
for team_members, team_name in teams.items():
    if "Alice" in team_members:
        print(f"Alice가 속한 팀: {team_name}")

# 3. 불변 집합을 사용한 그래프 표현
graph = {
    "A": frozenset(["B", "C"]),
    "B": frozenset(["A", "D", "E"]),
    "C": frozenset(["A", "F"]),
    "D": frozenset(["B"]),
    "E": frozenset(["B", "F"]),
    "F": frozenset(["C", "E"]),
}

# 각 노드의 이웃 노드 출력
for node, neighbors in graph.items():
    print(f"노드 {node}의 이웃: {neighbors}")


# 두 노드가 직접 연결되어 있는지 확인
def is_connected(node1, node2):
    return node2 in graph[node1]


print(f"A와 B는 연결되어 있나요? {is_connected('A', 'B')}")
print(f"A와 D는 연결되어 있나요? {is_connected('A', 'D')}")


# 공통 이웃 찾기
def common_neighbors(node1, node2):
    return graph[node1] & graph[node2]


print(f"A와 B의 공통 이웃: {common_neighbors('A', 'B')}")
print(f"B와 E의 공통 이웃: {common_neighbors('B', 'E')}")
