import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# 테스트 코드
if __name__ == "__main__":
    # TODO: FrenchDeck 클래스의 인스턴스를 생성하세요
    deck = None

    # TODO: 덱의 길이를 출력하세요

    # TODO: 첫 번째 카드와 마지막 카드를 출력하세요

    # TODO: 랜덤으로 카드 한 장을 뽑아 출력하세요

    # TODO: 슬라이싱으로 처음 3장의 카드를 출력하세요

    # TODO: 반복문을 사용하여 에이스('A') 카드만 출력하세요

    # TODO: 카드 정렬을 위한 함수를 정의하세요
    # 스페이드 > 하트 > 다이아몬드 > 클럽 순으로 정렬
    # 같은 무늬면 숫자 순으로 정렬 (2가 가장 낮고 A가 가장 높음)
    suit_values = {"spades": 3, "hearts": 2, "diamonds": 1, "clubs": 0}

    def card_value(card):
        # TODO: 카드의 순위를 계산하는 코드를 작성하세요
        pass

    # TODO: 정렬된 카드를 출력하세요
