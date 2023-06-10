from typing import Final

from sklearn.model_selection import train_test_split

from suspension_data.constants import DATA_SOURCE_LOCATION
from suspension_data.dto import SuspensionCsvDto
from suspension_data.models import SuspensionRecord
from suspension_data.models.predict import split_data, train_model_and_evaluate


def read_csv_content() -> tuple[SuspensionRecord]:
    dto: Final[SuspensionCsvDto] = SuspensionCsvDto(
        f"{DATA_SOURCE_LOCATION}/university_suspension_data.csv"
    )
    return dto.to_suspension_records()


def start():
    records: Final[tuple[SuspensionRecord]] = read_csv_content()

    features, targets = split_data(records)

    model_data_sources = train_test_split(
        features, targets, test_size=0.1, random_state=42
    )

    model, loss = train_model_and_evaluate(*model_data_sources)
    print(loss)


if __name__ == "__main__":
    start()
