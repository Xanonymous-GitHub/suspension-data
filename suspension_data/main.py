from typing import Final

from suspension_data.constants import DATA_SOURCE_LOCATION
from suspension_data.dto import SuspensionCsvDto
from suspension_data.enums.enums import EducationProgram, Gender, SchoolType, SuspensionReason
from suspension_data.models import SuspensionRecord
from suspension_data.models.predict import split_data, train_model_and_predict


def read_csv_content() -> tuple[SuspensionRecord]:
    dto: Final[SuspensionCsvDto] = SuspensionCsvDto(
        f"{DATA_SOURCE_LOCATION}/university_suspension_data.csv"
    )
    records: Final[tuple[SuspensionRecord]] = dto.to_suspension_records()

    # pretty print the records
    # for record in records:
    # print(record.serializable_dict)

    return records


def start():
    records: Final[tuple[SuspensionRecord]] = read_csv_content()
    # year_list, count_list = sum_records(records)
    # plot_data(year_list, count_list)

    x_train, y_train = split_data(records)
    x_test: list[list] = []
    for year in range(111, 115):
        test_data = [
            Gender.BOY.index,
            SchoolType.PUBLIC.index,
            EducationProgram.BACHELORS.index,
            SuspensionReason.WORK_REQUIREMENTS.index,
            year
        ]
        x_test.append(test_data)
    y_test: list = train_model_and_predict(x_train, x_test, y_train)

    # TODO: check the output data is as expected
    result: list = []
    for x_data, y_data in zip(x_test, y_test):
        result = x_data + [y_data]

    print(result)


if __name__ == "__main__":
    start()
