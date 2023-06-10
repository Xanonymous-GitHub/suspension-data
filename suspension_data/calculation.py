from collections.abc import Iterable

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

def sum_records_divide_gender(records: Iterable[SuspensionRecord]) -> tuple[list[int], list[int]]:
    year_list: list[int] = []
    male_list: list[int] = []
    
    for record in records:
        if record.gender.value == "男":
            if record.year not in year_list:
                year_list.append(record.year)
                male_list.append(record.count)
            else:
                male_list[year_list.index(record.year)] += record.count

    year_list: list[int] = []
    female_list: list[int] = []
    for record in records:
        if record.gender.value == "女":
            if record.year not in year_list:
                year_list.append(record.year)
                female_list.append(record.count)
            else:
                female_list[year_list.index(record.year)] += record.count

    return year_list, male_list, female_list

# def sum_records_of_gender(records: Iterable[SuspensionRecord]) -> tuple[list[Gender], list[int]]:
#     gender_list: list[Gender] = []
#     count_list: list[int] = []

#     for record in records:
#         if record.gender not in gender_list:
#             gender_list.append(record.gender)
#             count_list.append(record.count)
#         else:
#             count_list[gender_list.index(record.gender)] += record.count

#     return gender_list, count_list

# def sum_records_of_schoolType(records: Iterable[SuspensionRecord]) -> tuple[list[SchoolType], list[int]]:
#     schoolType_list: list[SchoolType] = []
#     count_list: list[int] = []

#     for record in records:
#         if record.school_type not in schoolType_list:
#             schoolType_list.append(record.school_type)
#             count_list.append(record.count)
#         else:
#             count_list[schoolType_list.index(record.school_type)] += record.count

#     return schoolType_list, count_list

# def sum_records_of_educationProgram(records: Iterable[SuspensionRecord]) -> tuple[list[EducationProgram], list[int]]:
#     educationProgram_list: list[EducationProgram] = []
#     count_list: list[int] = []

#     for record in records:
#         if record.program not in educationProgram_list:
#             educationProgram_list.append(record.program)
#             count_list.append(record.count)
#         else:
#             count_list[educationProgram_list.index(record.program)] += record.count

#     return educationProgram_list, count_list


# def sum_records_of_reason(records: Iterable[SuspensionRecord]) -> tuple[list[SuspensionReason], list[int]]:
#     reason_list: list[SuspensionReason] = []
#     count_list: list[int] = []

#     for record in records:
#         if record.suspension_reason not in reason_list:
#             reason_list.append(record.suspension_reason)
#             count_list.append(record.count)
#         else:
#             count_list[reason_list.index(record.suspension_reason)] += record.count

#     return reason_list, count_list