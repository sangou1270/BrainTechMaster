#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파이썬 함수 실습 파일
실행 방법: python 07_functions.py
"""

# ==========================================================
# 기본 함수 정의
# ==========================================================
print("=== 기본 함수 ===")
# 매개변수 없는 함수
def greet():
    """인사 메시지를 출력하는 함수"""
    print("안녕하세요! 파이썬 함수에 오신 것을 환영합니다.")

# 함수 호출
greet()

# ==========================================================
# 매개변수가 있는 함수
# ==========================================================
print("\n=== 매개변수가 있는 함수 ===")
def greet_person(name):
    """
    이름을 받아 인사 메시지를 출력하는 함수
    
    매개변수:
    name -- 인사할 사람의 이름
    """
    print(f"안녕하세요, {name}님!")

greet_person("홍길동")

# 여러 매개변수가 있는 함수
def print_info(name, age, city):
    """이름, 나이, 도시 정보를 출력하는 함수"""
    print(f"이름: {name}, 나이: {age}, 도시: {city}")

print_info("김영희", 25, "서울")

# ==========================================================
# 반환 값이 있는 함수
# ==========================================================
print("\n=== 반환 값이 있는 함수 ===")
def add_numbers(a, b):
    """두 숫자를 더하여 결과를 반환하는 함수"""
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# 여러 값 반환
def get_user_info():
    """사용자 정보를 반환하는 함수"""
    name = "이철수"
    age = 30
    city = "부산"
    return name, age, city  # 실제로는 튜플을 반환

# 반환된 값 받기
user_name, user_age, user_city = get_user_info()
print(f"사용자 정보: {user_name}, {user_age}, {user_city}")

# ==========================================================
# 기본값 매개변수
# ==========================================================
print("\n=== 기본값 매개변수 ===")
def greet_with_message(name, message="안녕하세요"):
    """
    기본 메시지를 사용한 인사 함수
    
    매개변수:
    name -- 인사할 사람의 이름
    message -- 인사말 (기본값: "안녕하세요")
    """
    print(f"{message}, {name}님!")

greet_with_message("박지성")  # 기본 메시지 사용
greet_with_message("손흥민", "반갑습니다")  # 다른 메시지 제공

# ==========================================================
# 키워드 인자
# ==========================================================
print("\n=== 키워드 인자 ===")
def create_profile(name, age, job, city):
    """사용자 프로필을 생성하는 함수"""
    profile = f"이름: {name}, 나이: {age}, 직업: {job}, 도시: {city}"
    return profile

# 키워드 인자 사용
profile1 = create_profile(name="김철수", age=35, city="인천", job="개발자")
profile2 = create_profile(age=28, name="이영희", job="디자이너", city="대전")

print("프로필1:", profile1)
print("프로필2:", profile2)

# ==========================================================
# 가변 위치 인자 (*args)
# ==========================================================
print("\n=== 가변 위치 인자 (*args) ===")
def sum_all(*numbers):
    """
    여러 숫자의 합을 계산하는 함수
    
    매개변수:
    *numbers -- 합산할 숫자들 (가변 인자)
    """
    result = 0
    for num in numbers:
        result += num
    return result

print("합계1:", sum_all(1, 2, 3))
print("합계2:", sum_all(1, 2, 3, 4, 5))
print("합계3:", sum_all(10))
print("합계4:", sum_all())  # 인자 없음 (0 반환)

# ==========================================================
# 가변 키워드 인자 (**kwargs)
# ==========================================================
print("\n=== 가변 키워드 인자 (**kwargs) ===")
def print_person_details(**details):
    """
    사람의 세부 정보를 출력하는 함수
    
    매개변수:
    **details -- 사람의 세부 정보 (가변 키워드 인자)
    """
    print("개인 정보:")
    for key, value in details.items():
        print(f"- {key}: {value}")

print_person_details(이름="김민준", 나이=32, 직업="교사", 취미="독서")
print_person_details(이름="이지현", 전화번호="010-1234-5678", 이메일="lee@example.com")

# ==========================================================
# 위치, 키워드, 가변 인자 혼합
# ==========================================================
print("\n=== 인자 혼합 사용 ===")
def complex_function(name, *args, age=30, **kwargs):
    """다양한 종류의 인자를 받는 복잡한 함수"""
    print(f"이름: {name}")
    print(f"나이: {age}")
    print("추가 인자:")
    for arg in args:
        print(f"- {arg}")
    print("키워드 인자:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

complex_function("홍길동", "학생", "서울 거주", age=25, 취미="게임", 전공="컴퓨터")

# ==========================================================
# 함수 독스트링 (Docstring)
# ==========================================================
print("\n=== 함수 독스트링 ===")
def calculate_area(radius):
    """
    원의 면적을 계산하는 함수
    
    매개변수:
    radius -- 원의 반지름 (양수)
    
    반환값:
    float -- 원의 면적
    
    예시:
    >>> calculate_area(5)
    78.5
    """
    if radius < 0:
        raise ValueError("반지름은 음수일 수 없습니다.")
    return 3.14 * radius ** 2

# 독스트링 출력
print(calculate_area.__doc__)

# 함수 사용
area = calculate_area(5)
print(f"반지름이 5인 원의 면적: {area}")

# ==========================================================
# 함수 내부에서 전역 변수 사용
# ==========================================================
print("\n=== 전역 변수 사용 ===")
counter = 0  # 전역 변수

def increment():
    """전역 변수를 증가시키는 함수"""
    global counter  # 전역 변수 사용 선언
    counter += 1
    print(f"카운터 값: {counter}")

print(f"함수 호출 전 카운터: {counter}")
increment()
increment()
print(f"함수 호출 후 카운터: {counter}")

# ==========================================================
# 함수 내부에 함수 정의 (중첩 함수)
# ==========================================================
print("\n=== 중첩 함수 ===")
def outer_function(x):
    """외부 함수"""
    print(f"외부 함수 호출됨, x = {x}")
    
    def inner_function(y):
        """내부 함수"""
        return x + y
    
    return inner_function  # 내부 함수 반환

add_five = outer_function(5)  # 외부 함수 호출, 내부 함수 반환
result = add_five(10)  # 내부 함수 호출
print(f"결과: {result}")  # 5 + 10 = 15

# ==========================================================
# 람다 함수 (Lambda Functions)
# ==========================================================
print("\n=== 람다 함수 ===")
# 일반 함수
def square(x):
    return x ** 2

# 동일한 기능의 람다 함수
square_lambda = lambda x: x ** 2

print(f"일반 함수: {square(4)}")
print(f"람다 함수: {square_lambda(4)}")

# 람다 함수를 인자로 사용
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"제곱된 숫자: {squared_numbers}")

# ==========================================================
# 연습 1: 팩토리얼 계산 함수
# ==========================================================
# TODO: 팩토리얼을 계산하는 함수를 작성하세요
# 팩토리얼: n! = n * (n-1) * (n-2) * ... * 1

# def factorial(n):
#     """
#     n의 팩토리얼을 계산하는 함수
#     
#     매개변수:
#     n -- 팩토리얼을 계산할 음이 아닌 정수
#     
#     반환값:
#     n의 팩토리얼 (n!)
#     """
#     # 팩토리얼 계산 로직을 구현하세요
#     # (힌트: 재귀 또는 반복문 사용)
#     pass

# 함수 테스트
# for i in range(6):
#     print(f"{i}! = {factorial(i)}")

# ==========================================================
# 연습 2: 섭씨-화씨 변환 함수
# ==========================================================
# TODO: 온도를 섭씨에서 화씨로, 화씨에서 섭씨로 변환하는 두 함수를 작성하세요
# 섭씨 -> 화씨: (C × 9/5) + 32 = F
# 화씨 -> 섭씨: (F - 32) × 5/9 = C

# def celsius_to_fahrenheit(celsius):
#     """
#     섭씨 온도를 화씨 온도로 변환하는 함수
#     
#     매개변수:
#     celsius -- 섭씨 온도
#     
#     반환값:
#     화씨 온도
#     """
#     # 변환 코드를 작성하세요
#     pass

# def fahrenheit_to_celsius(fahrenheit):
#     """
#     화씨 온도를 섭씨 온도로 변환하는 함수
#     
#     매개변수:
#     fahrenheit -- 화씨 온도
#     
#     반환값:
#     섭씨 온도
#     """
#     # 변환 코드를 작성하세요
#     pass

# 함수 테스트
# temp_c = 25
# temp_f = celsius_to_fahrenheit(temp_c)
# print(f"{temp_c}°C는 {temp_f:.1f}°F입니다.")
# print(f"{temp_f:.1f}°F는 {fahrenheit_to_celsius(temp_f):.1f}°C입니다.")

# ==========================================================
# 도전 과제: 계산기 함수
# ==========================================================
# TODO: 사칙연산과 제곱을 수행하는 계산기 함수를 작성하세요
# 함수는 operation 매개변수로 'add', 'subtract', 'multiply', 'divide', 'power' 중 
# 하나를 받아, 해당 연산을 수행해야 합니다.

# def calculator(a, b, operation):
#     """
#     두 숫자에 대해 지정된 연산을 수행하는 계산기 함수
#     
#     매개변수:
#     a -- 첫 번째 숫자
#     b -- 두 번째 숫자
#     operation -- 수행할 연산 ('add', 'subtract', 'multiply', 'divide', 'power')
#     
#     반환값:
#     연산 결과
#     """
#     # 계산기 로직을 구현하세요
#     pass

# 함수 테스트
# operations = ['add', 'subtract', 'multiply', 'divide', 'power']
# a, b = 10, 3

# for op in operations:
#     result = calculator(a, b, op)
#     print(f"{a} {op} {b} = {result}")