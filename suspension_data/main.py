from typing import Final

from suspension_data.constants import DATA_SOURCE_LOCATION
from suspension_data.dto import SuspensionCsvDto
from suspension_data.enums.enums import EducationProgram, Gender, SchoolType, SuspensionReason
from suspension_data.models import SuspensionRecord
from suspension_data.models.predict import split_data, train_model_and_predict


def read_csv_content() -> tuple[SuspensionRecord]:
    dto: Final[SuspensionCsvDto] = SuspensionCsvDto(f'{DATA_SOURCE_LOCATION}/university_suspension_data.csv')
    return dto.to_suspension_records()


def start():
    records: Final[tuple[SuspensionRecord]] = read_csv_content()

    x_train, y_train = split_data(records)
    x_test: Final[list[list]] = []

    for year in range(111, 115):
        x_test.append([
            Gender.BOY.index,
            SchoolType.PUBLIC.index,
            EducationProgram.BACHELORS.index,
            SuspensionReason.WORK_REQUIREMENTS.index,
            year
        ])

    y_test: Final[list] = train_model_and_predict(x_train, y_train, x_test)

    # TODO: check the output data is as expected
    result: list = []
    for x_data, y_data in zip(x_test, y_test):
        result = x_data + [y_data]

    print(result)


if __name__ == "__main__":
    start()
