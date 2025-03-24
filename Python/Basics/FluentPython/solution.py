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
    # FrenchDeck 클래스의 인스턴스를 생성
    deck = FrenchDeck()

    # 덱의 길이를 출력
    print(f"카드 덱의 길이: {len(deck)}")

    # 첫 번째 카드와 마지막 카드를 출력
    print(f"첫 번째 카드: {deck[0]}")
    print(f"마지막 카드: {deck[-1]}")

    # 랜덤으로 카드 한 장을 뽑아 출력
    random_card = choice(deck)
    print(f"랜덤 카드: {random_card}")

    # 슬라이싱으로 처음 3장의 카드를 출력
    print("첫 3장의 카드:")
    for card in deck[:3]:
        print(f"  {card}")

    # 반복문을 사용하여 에이스('A') 카드만 출력
    print("모든 에이스 카드:")
    for card in deck:
        if card.rank == "A":
            print(f"  {card}")

    # 카드 정렬을 위한 함수를 정의
    # 스페이드 > 하트 > 다이아몬드 > 클럽 순으로 정렬
    # 같은 무늬면 숫자 순으로 정렬 (2가 가장 낮고 A가 가장 높음)
    suit_values = {"spades": 3, "hearts": 2, "diamonds": 1, "clubs": 0}

    def card_value(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * 10 + suit_values[card.suit]

    # 정렬된 카드를 출력
    print("\n정렬된 처음 5장의 카드:")
    for card in sorted(deck, key=card_value)[:5]:
        print(f"  {card}")

    print("\n정렬된 마지막 5장의 카드:")
    for card in sorted(deck, key=card_value)[-5:]:
        print(f"  {card}")
