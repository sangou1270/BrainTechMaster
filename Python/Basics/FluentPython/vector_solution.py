from math import sqrt, hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# 테스트 코드
if __name__ == "__main__":
    # 벡터 인스턴스 생성
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")

    # v1과 v2를 더한 결과를 출력
    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")

    # v1의 절대값(크기)을 출력
    print(f"|v1| = {abs(v1)}")

    # v1을 숫자 3과 곱한 결과를 출력
    v4 = v1 * 3
    print(f"v1 * 3 = {v4}")

    # bool(v1)과 bool(Vector(0, 0))의 결과를 출력
    print(f"bool(v1) = {bool(v1)}")
    print(f"bool(Vector(0, 0)) = {bool(Vector(0, 0))}")

    # 시퀀스 언패킹 테스트
    # Vector의 x, y 값을 언패킹하여 각각의 변수에 할당하고 출력
    x, y = v1.x, v1.y
    print(f"언패킹 결과: x = {x}, y = {y}")

    # 제너레이터 표현식 테스트
    # [1, 2, 3, 4, 5]의 각 요소를 제곱한 결과를 제너레이터 표현식으로 생성하고 출력
    squares = (x * x for x in [1, 2, 3, 4, 5])
    print(f"제너레이터 표현식 결과: {list(squares)}")

    # 추가 기능 - 제너레이터 표현식과 list 컴프리헨션 비교
    import sys

    squares_gen = (x * x for x in range(1000))
    squares_list = [x * x for x in range(1000)]

    print(f"제너레이터 표현식 크기: {sys.getsizeof(squares_gen)} 바이트")
    print(f"리스트 컴프리헨션 크기: {sys.getsizeof(squares_list)} 바이트")
