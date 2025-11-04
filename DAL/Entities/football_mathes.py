from football_player import FootballPlayer
import re

class FootBallMatch:
    PATTERN_DATE = r"^(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}$"
    SCORE_PATTERN = r"^\d{1,2}:\d{1,2}$"
    
    def __init__(self, home_team: str, away_team: str, match_date: str, score: str, players: list[FootballPlayer] = None):
        self._home_team = home_team
        self._away_team = away_team
        self.match_date = match_date
        self.score = score
        self.__players: list[FootballPlayer] = players if players is not None else []
        self.__id = f"{home_team[0]}_{away_team[0]}_{match_date.split('-')}"

    @property
    def id(self) -> str:
        return self.__id

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
        return self.__match_date
    
    @match_date.setter
    def match_date(self, value: str) -> None:
        if not re.match(self.PATTERN_DATE, value):
            raise ValueError("Invalid date format. Expected DD-MM-YYYY")
        self.__match_date = value
    
    @property
    def score(self) -> str:
        return self.__score
    
    @score.setter
    def score(self, value: str) -> None:
        if not re.match(self.SCORE_PATTERN, value):
            raise ValueError("Invalid score format. Expected 'X:Y'")
        self.__score = value

    def add_player(self, player: FootballPlayer) -> None:
        if not isinstance(player, FootballPlayer):
            raise TypeError("Expected a FootballPlayer instance")
        self.__players.append(player)
