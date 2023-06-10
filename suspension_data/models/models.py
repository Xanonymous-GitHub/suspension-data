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


def convert_record_to_list(record: SuspensionRecord) -> list:
    return [
        record.gender.value,
        record.school_type.value,
        record.program.value,
        record.suspension_reason.value,
        record.year,
        record.count
    ]
