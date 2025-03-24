#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제
변수(Variable)
"""

# 1. 변수 선언과 할당
print("1. 변수 선언과 할당")
a = 10
b = 3.14
c = "Hello"
d = True
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")

# 2. 변수의 타입
print("\n2. 변수의 타입")
print(f"a의 타입: {type(a)}")  # <class 'int'>
print(f"b의 타입: {type(b)}")  # <class 'float'>
print(f"c의 타입: {type(c)}")  # <class 'str'>
print(f"d의 타입: {type(d)}")  # <class 'bool'>

# 3. 변수 재할당
print("\n3. 변수 재할당")
a = 20
print(f"재할당 후 a = {a}")

# 다른 타입으로 재할당 가능 (동적 타이핑)
a = "Python"
print(f"문자열로 재할당 후 a = {a}")
print(f"재할당 후 a의 타입: {type(a)}")

# 4. 여러 변수 동시 할당
print("\n4. 여러 변수 동시 할당")
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

# 값 교환하기
print("\n값 교환하기")
print(f"교환 전: x = {x}, y = {y}")
x, y = y, x
print(f"교환 후: x = {x}, y = {y}")

# 5. 변수 참조와 객체
print("\n5. 변수 참조와 객체")
# 변수는 객체를 참조함
a = [1, 2, 3]
b = a  # b는 a와 같은 객체를 참조
print(f"a = {a}")
print(f"b = {b}")

# a를 변경하면 b도 변경됨
a.append(4)
print(f"a.append(4) 후 a = {a}")
print(f"a.append(4) 후 b = {b}")

# 6. 복사와 참조
print("\n6. 복사와 참조")
# 다른 객체로 복사
a = [1, 2, 3]
b = a.copy()  # 새로운 리스트 객체를 생성하여 b에 할당
print(f"a = {a}")
print(f"b = {b}")

# a를 변경해도 b는 변경되지 않음
a.append(4)
print(f"a.append(4) 후 a = {a}")
print(f"a.append(4) 후 b = {b}")

# 7. 변수의 식별자 (ID)
print("\n7. 변수의 식별자 (ID)")
a = 10
b = 10
c = a
print(f"a의 ID: {id(a)}")
print(f"b의 ID: {id(b)}")
print(f"c의 ID: {id(c)}")
print(f"a와 b는 같은 객체인가? {a is b}")
print(f"a와 c는 같은 객체인가? {a is c}")

# 불변 객체와 가변 객체
print("\n불변 객체와 가변 객체")
# 불변 객체 (int, float, str, tuple)
a = 10
print(f"a = {a}, ID: {id(a)}")
a = a + 1
print(f"a = {a}, ID: {id(a)}")  # ID가 변경됨 (새로운 객체가 생성됨)

# 가변 객체 (list, dict, set)
b = [1, 2, 3]
print(f"b = {b}, ID: {id(b)}")
b.append(4)
print(f"b = {b}, ID: {id(b)}")  # ID가 같음 (같은 객체가 수정됨)

# 8. 변수의 범위 (Scope)
print("\n8. 변수의 범위 (Scope)")

# 전역 변수
global_var = "나는 전역 변수입니다"


def function1():
    # 지역 변수
    local_var = "나는 지역 변수입니다"
    print(f"함수 내부에서 전역 변수 접근: {global_var}")
    print(f"함수 내부에서 지역 변수 접근: {local_var}")


function1()
print(f"함수 외부에서 전역 변수 접근: {global_var}")
# print(f"함수 외부에서 지역 변수 접근: {local_var}")  # 오류 발생! 지역 변수는 함수 외부에서 접근 불가

# 지역 변수가 전역 변수와 이름이 같은 경우
print("\n지역 변수가 전역 변수와 이름이 같은 경우")
x = 10


def function2():
    x = 20  # 전역 변수 x와 다른 지역 변수 x
    print(f"함수 내부에서 x = {x}")


function2()
print(f"함수 외부에서 x = {x}")

# global 키워드 사용
print("\nglobal 키워드 사용")
y = 10


def function3():
    global y  # 전역 변수 y를 사용하겠다고 선언
    y = 20  # 전역 변수 y의 값을 변경
    print(f"함수 내부에서 y = {y}")


function3()
print(f"함수 외부에서 y = {y}")  # 함수에서 변경한 값이 유지됨

# 9. 네임스페이스 (Namespace)
print("\n9. 네임스페이스 (Namespace)")
# 빌트인 네임스페이스
print(f"빌트인 함수 예: len([1, 2, 3]) = {len([1, 2, 3])}")

# 모듈 네임스페이스
import math

print(f"math 모듈의 pi = {math.pi}")


# 지역 네임스페이스
def outer_function():
    outer_var = "외부 함수 변수"

    def inner_function():
        inner_var = "내부 함수 변수"
        print(f"내부 함수에서 outer_var: {outer_var}")  # 외부 함수의 변수에 접근 가능
        print(f"내부 함수에서 inner_var: {inner_var}")

    inner_function()
    print(f"외부 함수에서 outer_var: {outer_var}")
    # print(f"외부 함수에서 inner_var: {inner_var}")  # 오류 발생! 내부 함수의 변수에 접근 불가


outer_function()

# 10. 변수 생명 주기 (Lifetime)
print("\n10. 변수 생명 주기 (Lifetime)")


def lifetime_example():
    local_var = "함수 호출 시 생성됨"
    print(local_var)
    # 함수가 종료되면 local_var는 소멸됨


lifetime_example()
# print(local_var)  # 오류 발생! 함수가 종료되어 변수가 소멸됨

# 11. 변수 이름 규칙
print("\n11. 변수 이름 규칙")
# 올바른 변수명
valid_name = 10
my_var = 20
myVar = 30
_private = 40
number1 = 50

# 12. del 키워드로 변수 삭제
print("\n12. del 키워드로 변수 삭제")
a = 10
print(f"삭제 전 a = {a}")
del a
# print(f"삭제 후 a = {a}")  # 오류 발생! 변수가 삭제됨

# 13. 변수와 메모리
print("\n13. 변수와 메모리")
import sys

# 다양한 타입의 객체 크기
int_var = 10
float_var = 3.14
str_var = "Hello"
list_var = [1, 2, 3]
dict_var = {"a": 1, "b": 2}

print(f"int_var의 크기: {sys.getsizeof(int_var)} 바이트")
print(f"float_var의 크기: {sys.getsizeof(float_var)} 바이트")
print(f"str_var의 크기: {sys.getsizeof(str_var)} 바이트")
print(f"list_var의 크기: {sys.getsizeof(list_var)} 바이트")
print(f"dict_var의 크기: {sys.getsizeof(dict_var)} 바이트")

# TODO: 다양한 변수를 생성하고 타입과 연산을 실험해보세요.
# 예: 정수, 실수, 문자열, 리스트 등 여러 타입의 변수를 생성하고 값을 변경해보기

# 변수 타입 변환
# a = 10
# b = "20"
# 두 변수를 더하려면 타입 변환이 필요합니다.
# 결과: a + int(b) = ?

# 변수의 참조와 복사를 실험해보세요.
# original = [1, 2, 3]
# reference = original
# copy = original.copy()
# original.append(4)
# 결과는 어떻게 될까요?
