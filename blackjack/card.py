class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def value(self) -> int:
        if self.rank == "A":
            return 11
        elif self.rank in ("K", "Q", "J"):
            return 10
        else:
            return int(self.rank)
