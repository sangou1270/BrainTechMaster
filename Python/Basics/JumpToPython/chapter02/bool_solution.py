#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제 해답
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

# 다양한 조건식
print("\n다양한 조건식:")
# 숫자 비교
num = 15
if num > 10:
    print(f"{num}은(는) 10보다 큽니다.")
if num % 2 == 0:
    print(f"{num}은(는) 짝수입니다.")
else:
    print(f"{num}은(는) 홀수입니다.")

# 문자열 비교
text = "Python"
if text.startswith("P"):
    print(f"{text}은(는) 'P'로 시작합니다.")
if "th" in text:
    print(f"{text}에 'th'가 포함되어 있습니다.")
if len(text) > 5:
    print(f"{text}의 길이는 5보다 깁니다.")

# 컬렉션이 비어있는지 확인
my_list = [1, 2, 3]
if my_list:
    print(f"리스트에 {len(my_list)}개의 요소가 있습니다.")
my_dict = {"name": "John", "age": 30}
if "name" in my_dict:
    print(f"이름: {my_dict['name']}")
if my_dict.get("email") is None:
    print("이메일이 지정되지 않았습니다.")

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


# 추가 단락 평가 예제
# 1. 안전한 속성 접근
class Person:
    def __init__(self, name=None):
        self.name = name


person1 = Person("John")
person2 = None


# person이 None이 아닐 때만 name 속성에 접근
def get_person_name(person):
    return person and person.name


print(f"\n추가 단락 평가 예제:")
print(f"get_person_name(person1): {get_person_name(person1)}")
print(f"get_person_name(person2): {get_person_name(person2)}")


# 2. 조건부 함수 실행
def log_error(error_msg):
    print(f"오류: {error_msg}")
    return True


# 오류가 있을 때만 로그 함수 실행
is_error = True
is_error and log_error("파일을 찾을 수 없습니다.")

is_error = False
is_error and log_error("이 메시지는 출력되지 않습니다.")


# 3. 체인 연산
def process_number(num):
    # num이 양수면 계산 수행, 아니면 0 반환
    return num > 0 and num * 2


print(f"process_number(5): {process_number(5)}")
print(f"process_number(-3): {process_number(-3)}")
print(f"process_number(0): {process_number(0)}")

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


# 부울 연산의 연쇄 활용
# 첫 번째 참 값 또는 마지막 값 찾기
def first_truthy(*args):
    for arg in args:
        if arg:  # arg가 참이면
            return arg
    return args[-1] if args else None  # 모두 거짓이면 마지막 값 또는 None 반환


print("\n부울 연산의 연쇄 활용:")
print(
    f"first_truthy(0, '', False, 'Python', 42): {first_truthy(0, '', False, 'Python', 42)}"
)
print(f"first_truthy(0, '', None, False): {first_truthy(0, '', None, False)}")
print(f"first_truthy(): {first_truthy()}")


# 연쇄 할당과 부울 연산
# name이 있으면 name, 없으면 username, 둘 다 없으면 'Guest' 사용
def get_display_name(user_data):
    return user_data.get("name") or user_data.get("username") or "Guest"


user_data1 = {"name": "John", "username": "john_doe"}
user_data2 = {"username": "jane_doe"}
user_data3 = {}

print(f"get_display_name(user_data1): {get_display_name(user_data1)}")
print(f"get_display_name(user_data2): {get_display_name(user_data2)}")
print(f"get_display_name(user_data3): {get_display_name(user_data3)}")

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

# 추가 any/all 예제
# 1. 단어 목록 확인
words = ["apple", "banana", "cherry", "date"]
print(f"\n추가 any/all 예제:")
print(f"words = {words}")
print(f"모든 단어가 'a'를 포함하나요? {all('a' in word for word in words)}")
print(
    f"적어도 하나의 단어가 'b'로 시작하나요? {any(word.startswith('b') for word in words)}"
)
print(f"모든 단어의 길이가 4글자 이상인가요? {all(len(word) >= 4 for word in words)}")


# 2. 유효성 검사
def is_valid_user(user):
    required_fields = ["username", "email", "password"]
    # 모든 필수 필드가 존재하고 비어있지 않은지 확인
    return all(field in user and user[field] for field in required_fields)


user1 = {"username": "john", "email": "john@example.com", "password": "123456"}
user2 = {"username": "jane", "email": "", "password": "123456"}
user3 = {"username": "bob", "password": "123456"}

print(f"is_valid_user(user1): {is_valid_user(user1)}")
print(f"is_valid_user(user2): {is_valid_user(user2)}")
print(f"is_valid_user(user3): {is_valid_user(user3)}")


# 3. 소수 판별
def is_prime(n):
    """n이 소수인지 판별"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# 1부터 20까지의 숫자 중 소수 찾기
primes = [n for n in range(1, 21) if is_prime(n)]
print(f"1부터 20까지의 소수: {primes}")

# 1부터 50까지 숫자 중 3의 배수이거나 5의 배수인 수의 합
sum_of_multiples = sum(n for n in range(1, 51) if n % 3 == 0 or n % 5 == 0)
print(f"1부터 50까지 숫자 중 3 또는 5의 배수의 합: {sum_of_multiples}")


# 팰린드롬(앞뒤 동일한 문자열) 찾기
def is_palindrome(text):
    # 문자열에서 알파벳과 숫자만 추출하고 소문자로 변환
    cleaned_text = "".join(c.lower() for c in text if c.isalnum())
    return cleaned_text == cleaned_text[::-1]


texts = ["Anna", "Python", "A man, a plan, a canal: Panama", "race car", "Hello World"]
palindromes = [text for text in texts if is_palindrome(text)]
print(f"팰린드롬 문자열: {palindromes}")

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


# 비트 연산자의 활용
# 1. 비트 마스킹
def has_permission(user_permissions, required_permission):
    """
    사용자가 필요한 권한을 가지고 있는지 확인합니다.

    권한은 비트로 표현됩니다:
    READ = 4 (100)
    WRITE = 2 (010)
    EXECUTE = 1 (001)
    """
    return (user_permissions & required_permission) == required_permission


# 권한 정의
READ = 4  # 100
WRITE = 2  # 010
EXECUTE = 1  # 001

# 사용자 권한
user1_permissions = READ | WRITE  # 110 (읽기, 쓰기)
user2_permissions = READ  # 100 (읽기만)
user3_permissions = READ | WRITE | EXECUTE  # 111 (모든 권한)

print("\n비트 마스킹을 사용한 권한 확인:")
print(f"user1이 읽기 권한을 가지고 있나요? {has_permission(user1_permissions, READ)}")
print(
    f"user1이 실행 권한을 가지고 있나요? {has_permission(user1_permissions, EXECUTE)}"
)
print(f"user2가 쓰기 권한을 가지고 있나요? {has_permission(user2_permissions, WRITE)}")
print(
    f"user3가 모든 권한을 가지고 있나요? {has_permission(user3_permissions, READ | WRITE | EXECUTE)}"
)


# 2. 비트 플래그 설정/해제
def set_flag(flags, flag):
    """플래그 설정"""
    return flags | flag


def clear_flag(flags, flag):
    """플래그 해제"""
    return flags & ~flag


def toggle_flag(flags, flag):
    """플래그 토글"""
    return flags ^ flag


def check_flag(flags, flag):
    """플래그 확인"""
    return (flags & flag) == flag


# 비트 플래그 예제
flags = 0
print("\n비트 플래그 관리:")
print(f"초기 플래그: {bin(flags)}")

# 플래그 설정
flags = set_flag(flags, READ)
print(f"READ 플래그 설정 후: {bin(flags)}")

# 추가 플래그 설정
flags = set_flag(flags, WRITE)
print(f"WRITE 플래그 추가 설정 후: {bin(flags)}")

# 플래그 확인
print(f"READ 플래그가 설정되어 있나요? {check_flag(flags, READ)}")
print(f"EXECUTE 플래그가 설정되어 있나요? {check_flag(flags, EXECUTE)}")

# 플래그 토글
flags = toggle_flag(flags, EXECUTE)
print(f"EXECUTE 플래그 토글 후: {bin(flags)}")

# 플래그 해제
flags = clear_flag(flags, READ)
print(f"READ 플래그 해제 후: {bin(flags)}")


# 3. 홀수/짝수 판별
def is_even(n):
    """n이 짝수인지 확인 (비트 연산 활용)"""
    return (n & 1) == 0


def is_odd(n):
    """n이 홀수인지 확인 (비트 연산 활용)"""
    return (n & 1) == 1


print("\n비트 연산을 활용한 홀수/짝수 판별:")
for i in range(1, 6):
    print(f"{i}는 짝수인가? {is_even(i)}, 홀수인가? {is_odd(i)}")

# 4. 두 변수 값 교환 (XOR 활용)
a, b = 10, 20
print(f"\nXOR을 활용한 변수 값 교환:")
print(f"교환 전: a = {a}, b = {b}")

a = a ^ b
b = a ^ b
a = a ^ b

print(f"교환 후: a = {a}, b = {b}")
