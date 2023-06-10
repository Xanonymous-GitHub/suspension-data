from itertools import product
from typing import Final

from sklearn.model_selection import train_test_split

from calculation import sum_records, sum_records_divide_program
from suspension_data.constants import DATA_SOURCE_LOCATION
from suspension_data.dto import SuspensionCsvDto
from suspension_data.enums import EducationProgram, Gender, SchoolType, SuspensionReason
from suspension_data.models import SuspensionRecord
from suspension_data.models.predict import (
    predict_from_model,
    split_data,
    train_model_and_evaluate,
)
from suspension_data.visualize import plot_data


def read_csv_content() -> tuple[SuspensionRecord]:
    dto: Final[SuspensionCsvDto] = SuspensionCsvDto(
        f"{DATA_SOURCE_LOCATION}/university_suspension_data.csv"
    )
    return dto.to_suspension_records()


def generate_train_data(
        genders: list[Gender],
        school_types: list[SchoolType],
        education_programs: list[EducationProgram],
        suspension_reasons: list[SuspensionReason],
        years: list[int],
) -> tuple:
    return tuple(
        product(genders, school_types, education_programs, suspension_reasons, years)
    )


def start():
    records: Final[tuple[SuspensionRecord]] = read_csv_content()

    features, targets = split_data(records)

    model_data_sources = train_test_split(
        features, targets, test_size=0.1, random_state=42
    )

    model, result = train_model_and_evaluate(*model_data_sources)
    print(model, result)

    prediction_data = generate_train_data(
        [Gender.BOY.index],
        [SchoolType.PUBLIC.index],
        EducationProgram.to_index_list(),
        SuspensionReason.to_index_list(),
        [111],
    )
    for data in prediction_data:
        print(data)
    print(len(prediction_data))

    prediction_result = predict_from_model(model, prediction_data)
    print(prediction_result)

    year_list, count_list = sum_records(records)
    plot_data(year_list, count_list)
    # year_list, count_list = sum_records(records)
    # plot_data(year_list, count_list)

    # year_list, male_list, female_count_list = sum_records_divide_gender(records)
    # plot_gender_data(year_list, male_list, female_count_list)

    # year_list, public_list, private_list = sum_records_divide_school_type(records)
    # plot_school_type_data(year_list, public_list, private_list)

    year_list, total_divide_list, program_type_list = sum_records_divide_program(records)
    print(total_divide_list[4])
    print(total_divide_list[5])
    # plot_program_data(year_list, total_divide_list, program_type_list)


if __name__ == "__main__":
    start()
