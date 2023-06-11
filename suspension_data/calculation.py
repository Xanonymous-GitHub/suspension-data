from collections import defaultdict
from collections.abc import Iterable

from frozendict import frozendict

from suspension_data.enums import EducationProgram, SchoolType, Gender
from suspension_data.models.models import SuspensionRecord


def sum_records(records: Iterable[SuspensionRecord]) -> frozendict[int, int]:
    result: dict[int, int] = defaultdict(int)

    for record in records:
        result[record.year] += record.count

    return frozendict(result)


def sum_records_divide_gender(records: Iterable[SuspensionRecord]) -> frozendict[int, frozendict[Gender, int]]:
    result: dict[int, dict[Gender, int]] = defaultdict(lambda: defaultdict(int))

    for record in records:
        result[record.year][record.gender] += record.count

    return frozendict(result)


def sum_records_divide_school_type(records: Iterable[SuspensionRecord]) -> frozendict[int, frozendict[SchoolType, int]]:
    result: dict[int, dict[SchoolType, int]] = defaultdict(lambda: defaultdict(int))

    for record in records:
        result[record.year][record.school_type] += record.count

    return frozendict(result)


def sum_records_divide_program(records: Iterable[SuspensionRecord]) -> frozendict[int, frozendict[EducationProgram, int]]:
    result: dict[int, dict[EducationProgram, int]] = defaultdict(lambda: defaultdict(int))

    for record in records:
        result[record.year][record.program] += record.count

    return frozendict(result)
