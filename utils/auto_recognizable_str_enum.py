from enum import Enum

__all__ = ['AutoCheckRecognizableStrEnum']


class AutoCheckRecognizableStrEnum(Enum):
    @classmethod
    def _missing_(cls, key):
        """
        This method is invoked when an invalid enum value is passed.
        It raises a ValueError with a message that lists all the valid enum values.
        """
        raise ValueError(f'Invalid {cls.__name__} value: {key}. Valid values are: {[e.value for e in cls]}')

    @classmethod
    def is_valid(cls, value):
        """
        This method checks if the provided value is a valid enum value.
        """
        return value in cls._value2member_map_

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
