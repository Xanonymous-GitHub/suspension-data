from typing import Iterable

from suspension_data.models.models import SuspensionRecord


def sum_records(records: Iterable[SuspensionRecord]) -> tuple[list[int], list[int]]:
    year_list: list[int] = []
    count_list: list[int] = []

    for record in records:
        if record.year not in year_list:
            year_list.append(record.year)
            count_list.append(record.count)
        else:
            count_list[year_list.index(record.year)] += record.count

    return year_list, count_list
