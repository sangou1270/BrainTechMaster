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

    # TODO: __add__ 메서드를 구현하세요
    # 두 벡터를 더하는 연산자 오버로딩

    # TODO: __mul__ 메서드를 구현하세요
    # 벡터와 숫자의 곱셈 연산자 오버로딩


# 테스트 코드
if __name__ == "__main__":
    # 벡터 인스턴스 생성
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)

    print(f"v1 = {v1}")
    print(f"v2 = {v2}")

    # TODO: v1과 v2를 더한 결과를 출력하세요

    # TODO: v1의 절대값(크기)을 출력하세요

    # TODO: v1을 숫자 3과 곱한 결과를 출력하세요

    # TODO: bool(v1)과 bool(Vector(0, 0))의 결과를 출력하세요

    # 시퀀스 언패킹 테스트
    # TODO: Vector의 x, y 값을 언패킹하여 각각의 변수에 할당하고 출력하세요

    # 제너레이터 표현식 테스트
    # TODO: [1, 2, 3, 4, 5]의 각 요소를 제곱한 결과를 제너레이터 표현식으로 생성하고 출력하세요
