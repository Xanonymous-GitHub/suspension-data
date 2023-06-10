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
        if record.gender.value == Gender.BOY.value:
            if record.year not in year_list:
                year_list.append(record.year)
                male_list.append(record.count)
            else:
                male_list[year_list.index(record.year)] += record.count

    year_list: list[int] = []
    female_list: list[int] = []
    for record in records:
        if record.gender.value == Gender.GIRL.value:
            if record.year not in year_list:
                year_list.append(record.year)
                female_list.append(record.count)
            else:
                female_list[year_list.index(record.year)] += record.count

    return year_list, male_list, female_list

def sum_records_divide_school_type(records: Iterable[SuspensionRecord]) -> tuple[list[int], list[int]]:
    year_list: list[int] = []
    public_list: list[int] = []
    
    for record in records:
        if record.school_type.value == SchoolType.PUBLIC.value:
            if record.year not in year_list:
                year_list.append(record.year)
                public_list.append(record.count)
            else:
                public_list[year_list.index(record.year)] += record.count

    year_list: list[int] = []
    private_list: list[int] = []
    for record in records:
        if record.school_type.value == SchoolType.PRIVATE.value:
            if record.year not in year_list:
                year_list.append(record.year)
                private_list.append(record.count)
            else:
                private_list[year_list.index(record.year)] += record.count
    return year_list, public_list, private_list

def sum_records_divide_program(records: Iterable[SuspensionRecord]) -> tuple[list[int], list[int], list[int]]:
    total_divide_list = []
    years_list = []
    counting = 0
    for program in EducationProgram:
        year_list: list[int] = []
        temp_list: list[int] = []
        
        for record in records:
            if record.program.value == program.value:
                if record.year not in year_list:
                    years_list.append(record.year)
                    year_list.append(record.year)
                    temp_list.append(record.count)
                else:
                    temp_list[year_list.index(record.year)] += record.count
        total_divide_list.append(temp_list)
    years_list = list(dict.fromkeys(years_list)) 
    program_type_list = [program.value for program in EducationProgram]
    return years_list, total_divide_list[:-1], program_type_list[:-1]