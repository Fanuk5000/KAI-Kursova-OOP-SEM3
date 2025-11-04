import re

class FootballPlayer:
    _id: int = 1
    PATTERN_DATE = r"^(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}$"
    SALARY_LIMIT = 1000000
    POSSIBLE_STATUS: set = {"Active", "Injured", "Retired", "Dead"}
    HEALTH_STATUS = {
        "Excellent": range(85, 101),
        "Good": range(70, 85),
        "Average": range(50, 70),
        "Poor": range(30, 50),
        "Critical": range(0, 30),
    }

    def __init__(self, name: str, surname: str, birth_date: str, status: str, health: int, salary: float):
        self.__id = FootballPlayer._id
        FootballPlayer._id += 1

        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.status = status
        self.health = health
        self.salary = salary

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self.__name = value

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Surname must be a string")
        self.__surname = value

    @property
    def birth_date(self) -> str:
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Birth date must be a string")
        if not re.match(self.PATTERN_DATE, value):
            raise TypeError("Birth date must be a valid date in the format DD-MM-YYYY")
        self.__birth_date = value

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Status must be a string")
        if value not in self.POSSIBLE_STATUS:
            raise ValueError(f"Status must be one of {self.POSSIBLE_STATUS}")
        self.__status = value

    @property
    def health(self) -> str:
        return self.__health

    @health.setter
    def health(self, value: int) -> None:
        if not isinstance(value, int):
            self.__health = "Unknown"
            raise TypeError("Health must be an integer")
        if not (0 <= value <= 100):
            self.__health = "Unknown"
            raise ValueError("Health must be between 0 and 100")

        # find the category name whose range contains the numeric health
        category = next(
            (name for name, rng in self.HEALTH_STATUS.items() if value in rng),
            None,
        )
        # always store a string category; fallback to "Unknown" if no category found
        self.__health = category if category is not None else "Unknown"

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary must be a positive number")
        if value > self.SALARY_LIMIT:
            raise ValueError(f"Salary must not exceed {self.SALARY_LIMIT}")
        self.__salary = value

    def __repr__(self) -> str:
        """String representation of the FootballPlayer object."""
        return (f"FootballPlayer(id={self.__id}, name='{self.__name}', surname='{self.__surname}', "
                f"birth_date={self.__birth_date}, status='{self.__status}', health={self.__health}, "
                f"salary={self.__salary})")

ft_player = FootballPlayer("John", "Doe", "15-04-1990", "Active", 90, 300000.0)