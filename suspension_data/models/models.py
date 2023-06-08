from dataclasses import dataclass

from utils import JsonSerializable, ValidatableDataClass
from suspension_data.enums import Gender, SchoolType, EducationProgram, SuspensionReason


@dataclass(frozen=True)
class SuspensionRecord(ValidatableDataClass, JsonSerializable):
    gender: Gender
    school_type: SchoolType
    program: EducationProgram
    suspension_reason: SuspensionReason
    year: int
    count: int
