import re

class FootballPlayer:
    PATTERN_DATE = r"^(?:0[1-9]|[12][0-9]|3[01])-(?:0[1-9]|1[0-2])-\d{4}$"
    SALARY_LIMIT = 1000000
    POSSIBLE_STATUS: set = {"Active", "Injured", "Retired", "Dead"}

    def __init__(self, name: str, surname: str, birth_date: str, status: str, health: float, salary: float):
        """Initialize a FootballPlayer instance.

        Args:
            name (str): name of the player
            surname (str): surname of the player
            birth_date (str): birth date of the player
            status (str): status of the player
            health (int): health of the player
            salary (float): salary of the player
        """
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.status = status
        self.health = health
        self.salary = salary
        
        self._id = f"{name[0]}{surname[0]}{birth_date.replace('-', '')}"

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Surname must be a string")
        self._surname = value

    @property
    def birth_date(self) -> str:
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Birth date must be a string")
        if not re.match(self.PATTERN_DATE, value):
            raise ValueError("Birth date must be a valid date in the format DD-MM-YYYY")
        self._birth_date = value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Status must be a string")
        if value not in self.POSSIBLE_STATUS:
            raise ValueError(f"Status must be one of {self.POSSIBLE_STATUS}")
        self._status = value

    @property
    def health(self) -> float:
        return self._health

    @health.setter
    def health(self, value: float) -> None:
        if not isinstance(value, (float, int)):
            self._health = 0
            raise TypeError("Health must be a number")
        if not (0 <= value <= 100):
            self._health = 0
            raise ValueError("Health must be between 0 and 100")

        self._health = float(value)

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary must be a positive number")
        if value > self.SALARY_LIMIT:
            raise ValueError(f"Salary must not exceed {self.SALARY_LIMIT}")
        self._salary = value

    def __str__(self) -> str:
        return (f"FootballPlayer(id={self._id}, name='{self._name}', surname='{self._surname}', "
                f"birth_date={self._birth_date}, status='{self._status}', health={self._health}, "
                f"salary={self._salary})")

    def to_dict(self) -> dict:
        """Convert FootballPlayer to a dictionary."""
        return {
            "id": self._id,
            "name": self._name,
            "surname": self._surname,
            "birth_date": self._birth_date,
            "status": self._status,
            "health": self._health,
            "salary": self._salary,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'FootballPlayer':
        """Create a FootballPlayer from a dictionary."""
        return cls(
            name=data["name"],
            surname=data["surname"],
            birth_date=data["birth_date"],
            status=data["status"],
            health=data["health"],
            salary=data["salary"],
        )
