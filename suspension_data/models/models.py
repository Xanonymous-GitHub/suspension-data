from dataclasses import dataclass

from utils import JsonSerializable
from suspension_data.enums import Gender, SchoolType, EducationProgram, SuspensionReason


@dataclass(frozen=True)
class SuspensionRecord(JsonSerializable):
    gender: Gender
    school_type: SchoolType
    program: EducationProgram
    suspension_reason: SuspensionReason
    year: int
    count: int
