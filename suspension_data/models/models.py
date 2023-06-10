import sys
sys.path.append("../")
from dataclasses import dataclass

from suspension_data.enums import EducationProgram, Gender, SchoolType, SuspensionReason
from utils import JsonSerializable, ValidatableDataClass


@dataclass(frozen=True)
class SuspensionRecord(ValidatableDataClass, JsonSerializable):
    gender: Gender
    school_type: SchoolType
    program: EducationProgram
    suspension_reason: SuspensionReason
    year: int
    count: int
