from uuid import uuid4

class FootballEntity:
    def __init__(self, name:str, id: str = ''):
        """Initialize a FootballEntity instance.

        Args:
            id (str, optional): Unique identifier for the entity. Defaults to ''.
        """
        self.name = name
        self.__id = id if id else str(uuid4())
    
    @property
    def id(self) -> str:
        return self.__id
    
    @property
    def name(self) -> str:
        return self._name


    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self._name = new_name

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'FootballEntity':
        return cls(
            name=data["name"],
            id=data["id"]
        )
