from DAL.Entities.football_match import FootballMatch

class FootballStadium:
    def __init__(self, stadium_name: str, seats_amount: int, price_for_place: float, football_match: FootballMatch):  # type: ignore
        self.stadium_name = stadium_name
        self.seats_amount = seats_amount
        self.price_for_place = price_for_place
        self.football_match = football_match

    @property
    def stadium_name(self) -> str:
        return self._stadium_name

    @stadium_name.setter
    def stadium_name(self, new_stadium_name: str) -> None:
        if not isinstance(new_stadium_name, str):
            raise TypeError("Stadium name must be a string")
        self._stadium_name = new_stadium_name

    @property
    def seats_amount(self) -> int:
        return self._seats_amount

    @seats_amount.setter
    def seats_amount(self, new_seats_amount: int) -> None:
        if not isinstance(new_seats_amount, int):
            raise TypeError("Seats amount must be an integer")
        if new_seats_amount <= 0:
            raise ValueError("Seats amount cannot be negative or zero")
        if new_seats_amount > self.seats_amount:
            raise ValueError("Seats amount cannot be increased")
        self._seats_amount = new_seats_amount

    @property
    def price_for_place(self) -> float:
        return self._price_for_place

    @price_for_place.setter
    def price_for_place(self, new_price_for_place: float) -> None:
        if not type(new_price_for_place) in (int, float):
            raise TypeError("Price for place must be a number")
        if new_price_for_place <= 0:
            raise ValueError("Price for place cannot be negative or zero")
        self._price_for_place = float(new_price_for_place)

    @property
    def football_match(self) -> FootballMatch:
        return self._football_match
    
    @football_match.setter
    def football_match(self, new_football_match: FootballMatch) -> None:
        if not isinstance(new_football_match, FootballMatch):
            raise TypeError("football_match must be a FootballMatch instance")
        self._football_match = new_football_match

    def to_dict(self) -> dict:
        """Convert FootballStadium to a dictionary."""
        return {
            "stadium_name": self.stadium_name,
            "seats_amount": self.seats_amount,
            "price_for_place": self.price_for_place,
            "football_match": self.football_match.to_dict(),
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'FootballStadium':
        """Create a FootballStadium from a dictionary."""
        return cls(
            stadium_name=data["stadium_name"],
            seats_amount=data["seats_amount"],
            price_for_place=data["price_for_place"],
            football_match=FootballMatch.from_dict(data["football_match"]),
        )

    def __str__(self):
        return (f"FootballStadium(name={self.stadium_name}, seats={self.seats_amount}, "
               f"price_for_place={self.price_for_place}), "
               f"Playing {self.football_match.home_team} vs {self.football_match.away_team} on {self.football_match.match_date})")

