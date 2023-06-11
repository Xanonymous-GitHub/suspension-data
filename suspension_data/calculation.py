from collections import defaultdict
from collections.abc import Callable, Iterable
from typing import TypeVar

from frozendict import frozendict

from suspension_data.enums import EducationProgram, Gender, SchoolType, SuspensionReason
from suspension_data.models.models import SuspensionRecord

_T = TypeVar("_T")


def _sum_records_divided_by(
    records: Iterable[SuspensionRecord],
    key_func: Callable[[SuspensionRecord], SuspensionRecord],
) -> frozendict[int, frozendict[_T, int]]:
    result: dict[int, dict[SuspensionRecord, int]] = defaultdict(
        lambda: defaultdict(int)
    )

    for record in records:
        key = key_func(record)
        result[record.year][key] += record.count

    return frozendict(result)


def sum_records(records: Iterable[SuspensionRecord]) -> frozendict[int, int]:
    result: dict[int, int] = defaultdict(int)

    for record in records:
        result[record.year] += record.count

    return frozendict(result)


def sum_records_divide_gender(
    records: Iterable[SuspensionRecord],
) -> frozendict[int, frozendict[Gender, int]]:
    return _sum_records_divided_by(records, lambda record: record.gender)


def sum_records_divide_school_type(
    records: Iterable[SuspensionRecord],
) -> frozendict[int, frozendict[SchoolType, int]]:
    return _sum_records_divided_by(records, lambda record: record.school_type)


def sum_records_divide_education_program(
    records: Iterable[SuspensionRecord],
) -> frozendict[int, frozendict[EducationProgram, int]]:
    return _sum_records_divided_by(records, lambda record: record.program)


def sum_records_divide_suspension_reason(
    records: Iterable[SuspensionRecord],
) -> frozendict[int, frozendict[SuspensionReason, int]]:
    return _sum_records_divided_by(records, lambda record: record.suspension_reason)
