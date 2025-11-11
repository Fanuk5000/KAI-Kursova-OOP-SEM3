from DAL.Entities.football_player import FootballPlayer
import re

class FootballMatch:
    PATTERN_DATE = r"^(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}$"
    SCORE_PATTERN = r"^\d{1,2}:\d{1,2}$"
    POSSIBLE_STATUSES: set = {"Won", "Lost", "Draw", "Not played yet"}

    def __init__(self, match_place: str, home_team: str, away_team: str,
                 match_date: str, match_status: str, score: str = "00:00",
                 players: list[FootballPlayer] = None, viewers: int = 0):# type: ignore
        """Initialize a FootballMatch instance.

        Args:
            match_place (str): The place where the match is held.
            home_team (str): The name of the home team.
            away_team (str): The name of the away team.
            match_date (str): The date of the match in DD-MM-YYYY format.
            match_status (str): The current status of the match.
            score (str, optional): The score of the match in X:Y format. Defaults to "00:00".
            players (list[FootballPlayer], optional): The players participating in the match. Defaults to None.
            viewers (int, optional): The number of viewers for the match. Defaults to 0.
        """
        self.match_place = match_place
        self.home_team = home_team
        self.away_team = away_team
        self.match_date = match_date
        self.score = score
        self.match_status = match_status

        self._players: list = players if players is not None else []
        self.viewers = viewers

        day, month, year = match_date.split('-')
        self.__id = f"{home_team[0]}{away_team[0]}{day}{month}{year}"

    @property
    def id(self) -> str:
        return self.__id
    
    @property
    def match_place(self) -> str:
        return self._match_place
    
    @match_place.setter
    def match_place(self, new_match_place: str) -> None:
        if not isinstance(new_match_place, str):
            raise TypeError("Match place must be a string")
        self._match_place = new_match_place
    @property
    def home_team(self) -> str:
        return self._home_team

    @home_team.setter
    def home_team(self, new_home_team: str) -> None:
        if not isinstance(new_home_team, str):
            raise TypeError("Home team name must be a string")
        self._home_team = new_home_team

    @property
    def away_team(self) -> str:
        return self._away_team

    @away_team.setter
    def away_team(self, new_away_team: str) -> None:
        if not isinstance(new_away_team, str):
            raise TypeError("Away team name must be a string")
        self._away_team = new_away_team

    @property
    def match_date(self) -> str:
        return self._match_date
    
    @match_date.setter
    def match_date(self, new_match_date: str) -> None:
        if not re.match(self.PATTERN_DATE, new_match_date):
            raise ValueError(f"Invalid date format of {new_match_date} in FootBallMatch. Expected DD-MM-YYYY")
        self._match_date = new_match_date

    @property
    def score(self) -> str:
        return self._score

    @score.setter
    def score(self, new_score: str) -> None:
        if not re.match(self.SCORE_PATTERN, new_score):
            raise ValueError("Invalid score format. Expected 'X:Y'")
        self._score = new_score

    @property
    def match_status(self) -> str:
        return self._match_status

    @match_status.setter
    def match_status(self, new_match_status: str) -> None:
        if not isinstance(new_match_status, str):
            raise TypeError("Match status must be a string")
        if new_match_status not in self.POSSIBLE_STATUSES:
            raise ValueError(f"Invalid match status: {new_match_status}. Must be one of {self.POSSIBLE_STATUSES}")
        # in future: if match is not played yet, score must be "00:00" and if current date < match_date, status must be "Not played yet"
        self._match_status = new_match_status

    @property
    def players(self) -> list:
        return self._players

    @players.setter
    def players(self, players: list[FootballPlayer]) -> None:
        if not all(isinstance(player, FootballPlayer) for player in players):
            raise TypeError("All players must be instances of FootballPlayer")
        self._players = players

    @property
    def viewers(self) -> int:
        return self._viewers
    
    @viewers.setter
    def viewers(self, new_viewers: int) -> None:
        if not isinstance(new_viewers, int):
            raise TypeError("Viewers must be an integer")
        if new_viewers <= 0:
            raise ValueError("Viewers cannot be negative or zero")
        self._viewers = new_viewers
    
    def add_player(self, player: FootballPlayer) -> None:
        if not isinstance(player, FootballPlayer):
            raise TypeError("Expected a FootballPlayer instance")
        if player in self._players:
            raise ValueError("Player already exists in the match")
        self._players.append(player)

    def remove_player(self, player_id: str) -> None:
        player = [player for player in self._players if player.id == player_id]
        if player:
            for player in player:
                self._players.remove(player)
        else:
            raise ValueError("Player not found in the match")

    def to_dict(self) -> dict:
        """Convert FootballMatch to a dictionary."""
        return {
            "id": self.id,
            "match_place": self.match_place,
            "home_team": self.home_team,
            "away_team": self.away_team,
            "match_date": self.match_date,
            "score": self.score,
            "players": [player.to_dict() for player in self.players],
            "viewers": self.viewers,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'FootballMatch':
        """Create a FootBallMatch from a dictionary."""
        dict_players = [FootballPlayer.from_dict(player) for player in data["players"]]
        return cls(
            match_place=data["match_place"],
            home_team=data["home_team"],
            away_team=data["away_team"],
            match_date=data["match_date"],
            match_status=data["match_status"],
            score=data["score"],
            players=dict_players,
            viewers=data["viewers"],
        )

    def __str__(self) -> str:
        return (f"FootBallMatch(id={self.id}, "
                f"match_place='{self.match_place}', "
                f"home_team='{self.home_team}', away_team='{self.away_team}', "
                f"match_date='{self.match_date}', score='{self.score}', "
                f"players=[{', '.join(str(player) for player in self.players)}], "
                f"viewers={self.viewers})")