import sys
sys.path.append("../")

from itertools import product
from typing import Final

# from sklearn.model_selection import train_test_split

from suspension_data.calculation import (
    sum_records,
    sum_records_divide_education_program,
    sum_records_divide_gender,
    sum_records_divide_school_type,
    sum_records_divide_suspension_reason,
    sum_records_divide_suspension_reason_without_other,
)
from suspension_data.constants import DATA_SOURCE_LOCATION
from suspension_data.dto import SuspensionCsvDto
from suspension_data.enums import EducationProgram, Gender, SchoolType, SuspensionReason
from suspension_data.models import SuspensionRecord
# from suspension_data.predict import (
#     predict_from_model,
#     split_data,
#     train_model_and_evaluate,
# )
from suspension_data.visualize import (
    plot_data,
    plot_education_program_data,
    plot_gender_data,
    plot_school_type_data,
    plot_suspensions_reason_data,
)


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


def visualize(records: tuple[SuspensionRecord]):
    year_separated_record_dict = sum_records(records)
    plot_data(year_separated_record_dict)

    gender_separated_record_dict = sum_records_divide_gender(records)
    plot_gender_data(gender_separated_record_dict)

    school_type_separated_record_dict = sum_records_divide_school_type(records)
    plot_school_type_data(school_type_separated_record_dict)

    education_program_separated_record_dict = sum_records_divide_education_program(
        records
    )
    plot_education_program_data(education_program_separated_record_dict)

    education_suspension_reason_separated_record_dict = sum_records_divide_suspension_reason(
        records
    )
    plot_suspensions_reason_data(education_suspension_reason_separated_record_dict)

    education_suspension_reason_separated_record_without_other_dict = sum_records_divide_suspension_reason_without_other(
        records
    )
    plot_suspensions_reason_data(education_suspension_reason_separated_record_without_other_dict)


# def predict(records: tuple[SuspensionRecord]):
#     features, targets = split_data(records)

#     model_data_sources = train_test_split(
#         features, targets, test_size=0.1, random_state=42
#     )

#     model, result = train_model_and_evaluate(*model_data_sources)
#     print(model, result)

#     prediction_data = generate_train_data(
#         [Gender.BOY.index],
#         [SchoolType.PUBLIC.index],
#         EducationProgram.to_index_list(),
#         SuspensionReason.to_index_list(),
#         [111],
#     )
#     for data in prediction_data:
#         print(data)
#     print(len(prediction_data))

#     prediction_result = predict_from_model(model, prediction_data)
#     print(prediction_result)


def start():
    records: Final[tuple[SuspensionRecord]] = read_csv_content()
    visualize(records)
    # predict(records)


if __name__ == "__main__":
    start()
