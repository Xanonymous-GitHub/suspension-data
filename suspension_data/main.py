from typing import Final

from sklearn.model_selection import train_test_split

from suspension_data.constants import DATA_SOURCE_LOCATION
from suspension_data.dto import SuspensionCsvDto
from suspension_data.enums import EducationProgram, Gender, SchoolType, SuspensionReason
from suspension_data.models import SuspensionRecord
from suspension_data.models.predict import (
    predict_from_model,
    split_data,
    train_model_and_evaluate,
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
):
    train_data: list[list] = []
    for gender in genders:
        for school_type in school_types:
            for program in education_programs:
                for reason in suspension_reasons:
                    for year in years:
                        data = [gender, school_type, program, reason, year]
                        train_data.append(data)
    return train_data


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


if __name__ == "__main__":
    start()
