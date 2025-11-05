from DAL.Entities.football_player import FootballPlayer
import re

class FootBallMatch:
    PATTERN_DATE = r"^(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}$"
    SCORE_PATTERN = r"^\d{1,2}:\d{1,2}$"

    def __init__(self, match_place: str, home_team: str, away_team: str,
                 match_date: str, score: str = "00:00",
                 players: list[FootballPlayer] = None, viewers: int = 0):
        self.match_place = match_place
        self.home_team = home_team
        self.away_team = away_team
        self.match_date = match_date
        self.score = score

        self._players: list = players if players is not None else []
        self.viewers = viewers

        day, month, year = match_date.split('-')
        self._id = f"{home_team[0]}{away_team[0]}{day}{month}{year}"

    @property
    def id(self) -> str:
        return self._id

    @property
    def home_team(self) -> str:
        return self._home_team

    @home_team.setter
    def home_team(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Home team name must be a string")
        self._home_team = value

    @property
    def away_team(self) -> str:
        return self._away_team

    @away_team.setter
    def away_team(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Away team name must be a string")
        self._away_team = value

    @property
    def match_date(self) -> str:
        return self._match_date
    
    @match_date.setter
    def match_date(self, value: str) -> None:
        if not re.match(self.PATTERN_DATE, value):
            raise ValueError(f"Invalid date format of {value} in FootBallMatch. Expected DD-MM-YYYY")
        self._match_date = value
    
    @property
    def score(self) -> str:
        return self._score

    @score.setter
    def score(self, value: str) -> None:
        if not re.match(self.SCORE_PATTERN, value):
            raise ValueError("Invalid score format. Expected 'X:Y'")
        self._score = value

    @property
    def players(self) -> list:
        return self._players

    @players.setter
    def players(self, players: list[FootballPlayer]) -> None:
        if not all(isinstance(player, FootballPlayer) for player in players):
            raise TypeError("All players must be instances of FootballPlayer")
        self._players = players

    def add_player(self, player: FootballPlayer) -> None:
        if not isinstance(player, FootballPlayer):
            raise TypeError("Expected a FootballPlayer instance")
        self._players.append(player)


    def to_dict(self) -> dict:
        """Convert FootBallMatch to a dictionary."""
        return {
            "match_place": self.match_place,
            "home_team": self.home_team,
            "away_team": self.away_team,
            "match_date": self.match_date,
            "score": self.score,
            "players": [player.to_dict() for player in self.players],
            "viewers": self.viewers,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'FootBallMatch':
        """Create a FootBallMatch from a dictionary."""
        players = [FootballPlayer.from_dict(player) for player in data["players"]]
        return cls(
            match_place=data["match_place"],
            home_team=data["home_team"],
            away_team=data["away_team"],
            match_date=data["match_date"],
            score=data["score"],
            players=players,
            viewers=data["viewers"],
        )

    def __str__(self) -> str:
        return (f"FootBallMatch(id={self._id}, "
                f"match_place='{self.match_place}', "
                f"home_team='{self.home_team}', away_team='{self.away_team}', "
                f"match_date='{self.match_date}', score='{self.score}', "
                f"players=[{', '.join(str(player) for player in self.players)}], "
                f"viewers={self.viewers})")