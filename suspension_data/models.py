from dataclasses import dataclass

from enums import Gender, SchoolType, EducationProgram, SuspensionReason
from utils import JsonSerializable


@dataclass(frozen=True)
class SuspensionRecord(JsonSerializable):
    gender: Gender
    school_type: SchoolType
    program: EducationProgram
    suspension_reason: SuspensionReason
    year: int
    count: int
