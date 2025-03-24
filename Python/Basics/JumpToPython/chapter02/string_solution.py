#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jump to Python 2장 예제 해답
문자열(String)
"""

# 1. 문자열 생성하기
print("1. 문자열 생성하기")
str1 = "Hello"  # 큰따옴표로 생성
str2 = "World"  # 작은따옴표로 생성
str3 = """여러 줄로
작성된
문자열입니다."""  # 큰따옴표 세 개로 여러 줄 문자열 생성
str4 = """이것도
여러 줄
문자열입니다."""  # 작은따옴표 세 개로 여러 줄 문자열 생성

print(str1)
print(str2)
print(str3)
print(str4)

# 큰따옴표 안에 작은따옴표 포함하기
str5 = "Python's amazing"
print(str5)

# 작은따옴표 안에 큰따옴표 포함하기
str6 = 'He said "Python is easy"'
print(str6)

# 이스케이프 문자 사용하기
str7 = "큰따옴표(\")와 작은따옴표(')"
print(str7)

# 2. 문자열 인덱싱과 슬라이싱
print("\n2. 문자열 인덱싱과 슬라이싱")
string = "Python Programming"
print(f"string = {string}")

# 인덱싱 (위치로 한 글자 접근)
print(f"string[0] = {string[0]}")  # P
print(f"string[7] = {string[7]}")  # P
print(f"string[-1] = {string[-1]}")  # g (마지막 문자)
print(f"string[-2] = {string[-2]}")  # n (뒤에서 두 번째 문자)

# 슬라이싱 (범위로 부분 문자열 추출)
print(f"string[0:6] = {string[0:6]}")  # Python (처음부터 6번째까지, 6번째 미포함)
print(f"string[7:] = {string[7:]}")  # Programming (7번째부터 끝까지)
print(f"string[:6] = {string[:6]}")  # Python (처음부터 6번째까지, 6번째 미포함)
print(f"string[-9:] = {string[-9:]}")  # ogramming (뒤에서 9번째부터 끝까지)

# 스텝을 이용한 슬라이싱
print(f"string[::2] = {string[::2]}")  # Pto rgamn (처음부터 끝까지 2칸 간격으로)
print(f"string[::-1] = {string[::-1]}")  # gnimmargorP nohtyP (문자열 뒤집기)

# 3. 문자열 연산
print("\n3. 문자열 연산")
a = "Python"
b = "Programming"

# 문자열 연결 (Concatenation)
c = a + " " + b
print(f"a + ' ' + b = {c}")  # Python Programming

# 문자열 반복
d = a * 3
print(f"a * 3 = {d}")  # PythonPythonPython

# 문자열 길이
print(f"len(a) = {len(a)}")  # 6
print(f"len(b) = {len(b)}")  # 11
print(f"len(c) = {len(c)}")  # 18 (공백 포함)

# 4. 문자열 메서드
print("\n4. 문자열 메서드")
s = "python programming"

# 대소문자 변환
print(f"s.upper() = {s.upper()}")  # PYTHON PROGRAMMING (모두 대문자로)
print(f"s.capitalize() = {s.capitalize()}")  # Python programming (첫 글자만 대문자로)
print(f"s.title() = {s.title()}")  # Python Programming (각 단어의 첫 글자를 대문자로)

s2 = "PYTHON"
print(f"s2.lower() = {s2.lower()}")  # python (모두 소문자로)

# 문자열 찾기
print(f"s.find('gram') = {s.find('gram')}")  # 8 ('gram'의 시작 위치 반환)
print(f"s.find('xyz') = {s.find('xyz')}")  # -1 (없으면 -1 반환)

print(f"s.index('gram') = {s.index('gram')}")  # 8 ('gram'의 시작 위치 반환)
# print(f"s.index('xyz') = {s.index('xyz')}")  # 없으면 ValueError 발생

print(f"'gram' in s = {'gram' in s}")  # True ('gram'이 s에 있는지 확인)
print(f"'xyz' in s = {'xyz' in s}")  # False ('xyz'가 s에 있는지 확인)

print(f"s.count('p') = {s.count('p')}")  # 2 ('p'의 개수 세기)

# 문자열 교체
print(
    f"s.replace('python', 'java') = {s.replace('python', 'java')}"
)  # java programming

# 문자열 분할
s3 = "apple,banana,orange"
print(
    f"s3.split(',') = {s3.split(',')}"
)  # ['apple', 'banana', 'orange'] (쉼표로 분할하여 리스트 반환)

s4 = "   strip test   "
print(f"'{s4}'")  # '   strip test   '
print(f"'{s4.strip()}'")  # 'strip test' (양쪽 공백 제거)
print(f"'{s4.lstrip()}'")  # 'strip test   ' (왼쪽 공백 제거)
print(f"'{s4.rstrip()}'")  # '   strip test' (오른쪽 공백 제거)

# 문자열 결합
fruits = ["apple", "banana", "orange"]
joined = ", ".join(fruits)
print(f"', '.join({fruits}) = {joined}")  # apple, banana, orange

# 문자열 정렬
s5 = "python"
print(f"'{s5.center(10)}'")  # '  python  ' (10자리에서 가운데 정렬)
print(f"'{s5.ljust(10)}'")  # 'python    ' (10자리에서 왼쪽 정렬)
print(f"'{s5.rjust(10)}'")  # '    python' (10자리에서 오른쪽 정렬)
print(f"'{s5.zfill(10)}'")  # '0000python' (10자리로 만들고 앞을 0으로 채움)

# 문자열 시작/끝 확인
file_name = "example.txt"
print(
    f"{file_name}.startswith('ex') = {file_name.startswith('ex')}"
)  # True ('ex'로 시작하는지 확인)
print(
    f"{file_name}.endswith('.txt') = {file_name.endswith('.txt')}"
)  # True ('.txt'로 끝나는지 확인)

# 문자열 구성 확인
num_str = "12345"
alpha_str = "abcde"
alpha_num = "abc123"
space_str = "   "

print(f"'{num_str}'.isdigit() = {num_str.isdigit()}")  # True (모두 숫자인지 확인)
print(f"'{alpha_str}'.isalpha() = {alpha_str.isalpha()}")  # True (모두 알파벳인지 확인)
print(
    f"'{alpha_num}'.isalnum() = {alpha_num.isalnum()}"
)  # True (알파벳 또는 숫자인지 확인)
print(f"'{space_str}'.isspace() = {space_str.isspace()}")  # True (모두 공백인지 확인)

# 5. 문자열 포맷팅
print("\n5. 문자열 포맷팅")

# % 연산자를 이용한 포맷팅
name = "Alice"
age = 25
print("1) %s는 %d살입니다." % (name, age))  # Alice는 25살입니다.

# format() 메서드를 이용한 포맷팅
print("2) {}는 {}살입니다.".format(name, age))  # Alice는 25살입니다.
print(
    "3) {0}는 {1}살이고, {0}의 취미는 프로그래밍입니다.".format(name, age)
)  # Alice는 25살이고, Alice의 취미는 프로그래밍입니다.
print("4) {name}는 {age}살입니다.".format(name="Bob", age=30))  # Bob는 30살입니다.

# f-string (Python 3.6+)
print(f"5) {name}는 {age}살입니다.")  # Alice는 25살입니다.
price = 12345.6789
print(f"가격: {price:.2f}원")  # 가격: 12345.68원 (소수점 2자리까지 표시)

# 6. 문자열 이스케이프 시퀀스
print("\n6. 문자열 이스케이프 시퀀스")
print("줄바꿈\n예제")
# 줄바꿈
# 예제
print("탭\t예제")  # 탭    예제
print("백슬래시 자체 출력: \\")  # 백슬래시 자체 출력: \
print("작은따옴표 출력: '큰따옴표 출력: \"")  # 작은따옴표 출력: '큰따옴표 출력: "

# raw string (이스케이프 시퀀스를 처리하지 않음)
print(r"이스케이프 시퀀스 무시: \n \t \\")  # 이스케이프 시퀀스 무시: \n \t \\

# 7. 문자열 인코딩과 디코딩
print("\n7. 문자열 인코딩과 디코딩")
text = "안녕하세요"
# UTF-8로 인코딩
utf8_encoded = text.encode("utf-8")
print(
    f"'{text}'를 UTF-8로 인코딩: {utf8_encoded}"
)  # b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'

# 디코딩
decoded = utf8_encoded.decode("utf-8")
print(f"UTF-8 바이트를 디코딩: '{decoded}'")  # 안녕하세요

# 8. 유니코드와 문자열
print("\n8. 유니코드와 문자열")
# 유니코드 코드 포인트로 문자 표현
print("유니코드 이모지: \u263a")  # 유니코드 이모지: ☺
print("유니코드 한글: \ud55c\uae00")  # 유니코드 한글: 한글

# ord(): 문자의 유니코드 코드 포인트 반환
print(f"ord('A') = {ord('A')}")  # 65
print(f"ord('가') = {ord('가')}")  # 44032

# chr(): 코드 포인트에 해당하는 문자 반환
print(f"chr(65) = {chr(65)}")  # A
print(f"chr(44032) = {chr(44032)}")  # 가

# 9. 문자열 불변성(Immutability)
print("\n9. 문자열 불변성(Immutability)")
s = "Hello"
print(f"원래 문자열: {s}, ID: {id(s)}")

# 문자열은 불변(immutable)이므로 원래 객체를 변경할 수 없습니다.
# s[0] = "h"  # 이 코드는 TypeError를 발생시킵니다.

# 대신 새로운 문자열을 생성해야 합니다.
s = "h" + s[1:]
print(f"새로운 문자열: {s}, ID: {id(s)}")  # 새로운 객체가 생성됨

# 10. 문자열 성능과 메모리
print("\n10. 문자열 성능과 메모리")
import sys

a = "a"
b = "a" * 10
c = "a" * 100

print(f"len(a) = {len(a)}, 크기: {sys.getsizeof(a)} 바이트")
print(f"len(b) = {len(b)}, 크기: {sys.getsizeof(b)} 바이트")
print(f"len(c) = {len(c)}, 크기: {sys.getsizeof(c)} 바이트")

# 문자열 연결 성능
import time


def str_plus():
    result = ""
    for i in range(10000):
        result = result + "a"
    return result


def str_join():
    result = []
    for i in range(10000):
        result.append("a")
    return "".join(result)


# '+' 연산자를 사용한 연결 (느림)
start = time.time()
result1 = str_plus()
end = time.time()
print(f"'+' 연산자 시간: {end - start:.6f}초")

# join() 메서드를 사용한 연결 (빠름)
start = time.time()
result2 = str_join()
end = time.time()
print(f"join() 메서드 시간: {end - start:.6f}초")
print(f"결과 동일: {result1 == result2}")  # True

# 11. 응용: 문자열 처리 예제
print("\n11. 응용: 문자열 처리 예제")

# 문자열에서 모든 공백 제거하기
text = "  Python   is   an   amazing   language  "
no_spaces = "".join(text.split())
print(f"원본: '{text}'")
print(f"공백 제거: '{no_spaces}'")  # PythonisanamazinglanguagePythonisanamazinglanguage


# 문자 빈도수 계산하기
def char_frequency(text):
    result = {}
    for char in text.lower():
        if char.isalpha():  # 알파벳만 계산
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result


sample = "Python Programming"
freq = char_frequency(sample)
print(f"'{sample}'의 문자 빈도수:")
for char, count in sorted(freq.items()):
    print(f"'{char}': {count}")


# 회문(palindrome) 확인하기
def is_palindrome(text):
    # 공백과 대소문자 구분 없이 비교
    text = "".join(text.lower().split())
    return text == text[::-1]


palindrome1 = "A man a plan a canal Panama"
palindrome2 = "race car"
not_palindrome = "hello world"

print(f"'{palindrome1}'는 회문인가? {is_palindrome(palindrome1)}")  # True
print(f"'{palindrome2}'는 회문인가? {is_palindrome(palindrome2)}")  # True
print(f"'{not_palindrome}'는 회문인가? {is_palindrome(not_palindrome)}")  # False


# 문자열을 카멜 케이스로 변환하기
def to_camel_case(text):
    # 공백, 언더스코어, 하이픈으로 분리된 단어를 카멜 케이스로 변환
    words = text.replace("-", " ").replace("_", " ").split()
    if not words:
        return ""
    result = words[0].lower()
    for word in words[1:]:
        result += word.capitalize()
    return result


print(
    f"snake_case_example -> {to_camel_case('snake_case_example')}"
)  # snakeCaseExample
print(
    f"kebab-case-example -> {to_camel_case('kebab-case-example')}"
)  # kebabCaseExample
print(
    f"Title Case Example -> {to_camel_case('Title Case Example')}"
)  # titleCaseExample


# 문자열 암호화 (시저 암호)
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord("a") if char.islower() else ord("A")
            # 알파벳 범위 내에서 순환하도록 모듈로 연산 사용
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


original = "Hello, World!"
encrypted = caesar_cipher(original, 3)
decrypted = caesar_cipher(encrypted, -3)

print(f"원본: '{original}'")
print(f"암호화 (시프트 3): '{encrypted}'")  # Khoor, Zruog!
print(f"복호화 (시프트 -3): '{decrypted}'")  # Hello, World!

# 12. 문자열 관련 내장 함수
print("\n12. 문자열 관련 내장 함수")

# ord() 및 chr() - 이미 위에서 보여줌

# len() - 문자열 길이
print(f"len('Python') = {len('Python')}")  # 6

# max() 및 min() - 문자열에서 ASCII 값이 가장 큰/작은 문자
print(f"max('Python') = {max('Python')}")  # 'y' (ASCII 값이 가장 큼)
print(f"min('Python') = {min('Python')}")  # 'P' (ASCII 값이 가장 작음)

# 13. 문자열 포맷팅 추가 예제
print("\n13. 문자열 포맷팅 추가 예제")

# 숫자 포맷팅
num = 12345.6789
print(f"기본: {num}")  # 12345.6789
print(f"소수점 2자리: {num:.2f}")  # 12345.68
print(f"천 단위 구분기호: {num:,.2f}")  # 12,345.68
print(f"오른쪽 정렬, 15자리: {num:>15.2f}")  # '      12345.68'
print(f"왼쪽 정렬, 15자리: {num:<15.2f}")  # '12345.68      '
print(f"가운데 정렬, 15자리: {num:^15.2f}")  # '   12345.68   '
print(f"채우기, 15자리: {num:*>15.2f}")  # '*****12345.68'

# 정수 포맷팅
int_num = 42
print(f"10진수: {int_num}")  # 42
print(f"2진수: {int_num:b}")  # 101010
print(f"8진수: {int_num:o}")  # 52
print(f"16진수 (소문자): {int_num:x}")  # 2a
print(f"16진수 (대문자): {int_num:X}")  # 2A

# 문자열 포맷팅
name = "Python"
print(f"기본: {name}")  # Python
print(f"오른쪽 정렬, 10자리: {name:>10}")  # '    Python'
print(f"왼쪽 정렬, 10자리: {name:<10}")  # 'Python    '
print(f"가운데 정렬, 10자리: {name:^10}")  # '  Python  '

# 날짜 포맷팅
import datetime

now = datetime.datetime.now()
print(f"현재 날짜 및 시간: {now}")
print(f"연월일: {now:%Y-%m-%d}")  # 2023-03-24 (실행 날짜에 따라 다름)
print(f"시분초: {now:%H:%M:%S}")  # 08:50:30 (실행 시간에 따라 다름)
print(f"요일: {now:%A}")  # Friday (실행 날짜에 따라 다름)
print(f"간단한 날짜: {now:%y/%m/%d}")  # 23/03/24 (실행 날짜에 따라 다름)
print(f"12시간제: {now:%I:%M %p}")  # 08:50 AM (실행 시간에 따라 다름)

# % 출력하기
percentage = 75.5
print(f"진행률: {percentage}%")  # 진행률: 75.5%
print(f"진행률: {percentage:.1f}%")  # 진행률: 75.5%
# f-string에서 중괄호를 출력하려면 두 개를 연속으로 사용
print(f"중괄호 출력: {{percentage}}")  # 중괄호 출력: {percentage}

# 14. 문자열과 바이트
print("\n14. 문자열과 바이트")

# 문자열을 바이트로 변환
text = "안녕하세요"
bytes_utf8 = text.encode("utf-8")
bytes_utf16 = text.encode("utf-16")

print(f"원본 문자열: {text}")
print(f"UTF-8 바이트: {bytes_utf8}")
print(f"UTF-16 바이트: {bytes_utf16}")
print(
    f"UTF-8 길이: {len(bytes_utf8)} 바이트"
)  # 15 바이트 (한글은 UTF-8에서 문자당 3바이트)
print(
    f"UTF-16 길이: {len(bytes_utf16)} 바이트"
)  # 12 또는 14 바이트 (BOM 포함, 한글은 UTF-16에서 문자당 2바이트)

# 바이트를 문자열로 변환
decoded_utf8 = bytes_utf8.decode("utf-8")
decoded_utf16 = bytes_utf16.decode("utf-16")

print(f"UTF-8 디코딩: {decoded_utf8}")  # 안녕하세요
print(f"UTF-16 디코딩: {decoded_utf16}")  # 안녕하세요

# 바이트 배열
byte_array = bytearray(b"hello")
print(f"바이트 배열: {byte_array}")  # bytearray(b'hello')
# 바이트 배열은 가변(mutable)임
byte_array[0] = 72  # ASCII 코드 'H'
print(f"수정된 바이트 배열: {byte_array}")  # bytearray(b'Hello')
print(f"문자열로 변환: {byte_array.decode('ascii')}")  # Hello

# 15. 문자열 메모리 내부
print("\n15. 문자열 메모리 내부")

# 문자열 인터닝 (같은 내용의 문자열은 같은 객체를 참조)
a = "python"
b = "python"
c = "py" + "thon"

print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"c = {c}, id(c) = {id(c)}")
print(f"a is b: {a is b}")  # True (같은 객체를 참조)
print(f"a is c: {a is c}")  # True (같은 객체를 참조)

# 긴 문자열이나 런타임에 생성된 문자열은 인터닝되지 않을 수 있음
d = "a" * 20
e = "a" * 20
print(f"d = {d}, id(d) = {id(d)}")
print(f"e = {e}, id(e) = {id(e)}")
print(f"d is e: {d is e}")  # 시스템 및 Python 버전에 따라 결과가 다를 수 있음

# 16. 응용: 정규식을 사용한 문자열 처리
print("\n16. 응용: 정규식을 사용한 문자열 처리")
import re

# 이메일 주소 찾기
text = "연락처: john@example.com, mary@gmail.com, info@company.co.kr"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(email_pattern, text)
print(
    f"이메일 주소들: {emails}"
)  # ['john@example.com', 'mary@gmail.com', 'info@company.co.kr']

# 전화번호 찾기
phone_text = "연락처: 010-1234-5678, 02-987-6543, (031) 456-7890"
phone_pattern = r"\(?\d{2,3}\)?[\s-]?\d{3,4}[\s-]?\d{4}"
phones = re.findall(phone_pattern, phone_text)
print(f"전화번호들: {phones}")  # ['010-1234-5678', '02-987-6543', '(031) 456-7890']

# HTML 태그 제거
html = "<p>안녕하세요. <b>파이썬</b>을 사용한 <i>HTML</i> 파싱입니다.</p>"
no_tags = re.sub(r"<[^>]+>", "", html)
print(f"원본 HTML: {html}")
print(f"태그 제거: {no_tags}")  # 안녕하세요. 파이썬을 사용한 HTML 파싱입니다.

# 문자열 분할 (더 복잡한 패턴으로)
complex_text = "이름: 김철수; 나이: 30; 직업: 개발자"
parts = re.split(r";\s*", complex_text)
print(f"분할 결과: {parts}")  # ['이름: 김철수', '나이: 30', '직업: 개발자']

# 17. 응용: 한글 처리
print("\n17. 응용: 한글 처리")


# 한글 유니코드 범위 확인
def is_hangul(char):
    return 0xAC00 <= ord(char) <= 0xD7A3  # 완성형 한글 범위


# 한글 자음/모음 확인
def is_hangul_jamo(char):
    return 0x1100 <= ord(char) <= 0x11FF  # 한글 자모 범위


# 텍스트에서 한글만 추출
def extract_hangul(text):
    return "".join(char for char in text if is_hangul(char))


test_text = "안녕하세요123 Hello World!"
hangul_only = extract_hangul(test_text)
print(f"원본 텍스트: {test_text}")
print(f"한글만 추출: {hangul_only}")  # 안녕하세요


# 자음과 모음 분리 (초/중/종성 분리)
def decompose_hangul(char):
    if not is_hangul(char):
        return None

    code = ord(char) - 0xAC00
    jong = code % 28
    jung = ((code - jong) // 28) % 21
    cho = ((code - jong) // 28) // 21

    # 한글 초성, 중성, 종성의 유니코드 기준값
    cho_chars = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    jung_chars = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
    jong_chars = "ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

    result = cho_chars[cho]
    result += jung_chars[jung]
    if jong > 0:
        result += jong_chars[jong - 1]

    return result


# 한글 분해 예제
hangul_char = "한"
decomposed = decompose_hangul(hangul_char)
print(f"'{hangul_char}' 분해: {decomposed}")  # ㅎㅏㄴ

# 18. 응용: 문자열을 이용한 파일 처리
print("\n18. 응용: 문자열을 이용한 파일 처리")


# 파일 확장자 추출
def get_extension(filename):
    return filename.split(".")[-1] if "." in filename else ""


files = ["document.txt", "image.jpg", "program.py", "noextension"]
for file in files:
    ext = get_extension(file)
    print(f"파일: {file}, 확장자: '{ext}'")

# 파일 경로 처리
path = "/Users/username/Documents/projects/script.py"
path_parts = path.split("/")
print(f"경로: {path}")
print(f"파일명: {path_parts[-1]}")
print(f"디렉토리: {'/'.join(path_parts[:-1])}")

# Windows 경로를 POSIX 경로로 변환
windows_path = r"C:\Users\username\Documents\file.txt"
posix_path = windows_path.replace("\\", "/")
print(f"Windows 경로: {windows_path}")
print(f"POSIX 경로: {posix_path}")

# 19. 응용: 템플릿 문자열
print("\n19. 응용: 템플릿 문자열")
from string import Template

# 기본 템플릿
template = Template("$name님, $product 구매에 $price원을 지불하셨습니다.")
result = template.substitute(name="김철수", product="노트북", price="1,500,000")
print(result)  # 김철수님, 노트북 구매에 1,500,000원을 지불하셨습니다.

# 딕셔너리를 사용한 템플릿
data = {"name": "이영희", "product": "스마트폰", "price": "800,000"}
result2 = template.substitute(data)
print(result2)  # 이영희님, 스마트폰 구매에 800,000원을 지불하셨습니다.

# safe_substitute는 값이 없어도 오류를 발생시키지 않음
incomplete_data = {"name": "박지민", "product": "태블릿"}
result3 = template.safe_substitute(incomplete_data)
print(result3)  # 박지민님, 태블릿 구매에 $price원을 지불하셨습니다.

# 20. 문자열 인코딩의 실제 활용
print("\n20. 문자열 인코딩의 실제 활용")

# 다양한 인코딩으로 한글 인코딩
korean = "파이썬"
encodings = ["utf-8", "utf-16", "euc-kr", "cp949"]

for enc in encodings:
    encoded = korean.encode(enc)
    print(f"{enc} 인코딩: {encoded}, 길이: {len(encoded)} 바이트")
    # 다시 디코딩
    decoded = encoded.decode(enc)
    print(f"{enc} 디코딩: {decoded}")
    print()

# 인코딩 오류 처리
problematic = "파이썬 💻"  # 이모지 포함
try:
    # euc-kr은 이모지를 지원하지 않음
    encoded_error = problematic.encode("euc-kr")
except UnicodeEncodeError as e:
    print(f"인코딩 오류: {e}")

# 오류 처리 방법
encoded_replace = problematic.encode("euc-kr", errors="replace")
print(f"replace 옵션으로 인코딩: {encoded_replace}")
encoded_ignore = problematic.encode("euc-kr", errors="ignore")
print(f"ignore 옵션으로 인코딩: {encoded_ignore}")

# 디코딩 오류 처리
invalid_bytes = b"\xf0\x9f\x92\xbb"  # UTF-8 이모지
try:
    # euc-kr로 디코딩 시도
    decoded_error = invalid_bytes.decode("euc-kr")
except UnicodeDecodeError as e:
    print(f"디코딩 오류: {e}")

# 오류 처리 방법
decoded_replace = invalid_bytes.decode("euc-kr", errors="replace")
print(f"replace 옵션으로 디코딩: {decoded_replace}")
decoded_ignore = invalid_bytes.decode("euc-kr", errors="ignore")
print(f"ignore 옵션으로 디코딩: {decoded_ignore}")

print("\n문자열 관련 예제를 모두 완료했습니다.")
