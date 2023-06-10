from enum import Enum

__all__ = ["AutoCheckRecognizableStrEnum"]


class AutoCheckRecognizableStrEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        """
        This method is invoked when an invalid enum value is passed.
        It raises a ValueError with a message that lists all the valid enum values.
        """
        raise ValueError(
            f"Invalid {cls.__name__} value: {value}. Valid values are: {[e.value for e in cls]}"
        )

    @classmethod
    def is_valid(cls, value) -> bool:
        """
        This method checks if the provided value is a valid enum value.
        """
        return value in cls._value2member_map_

    @property
    def index(self) -> int:
        """
        This method returns the index of the enum value.
        """
        return tuple(self.__class__).index(self)

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value
