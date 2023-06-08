import os
from typing import Final

from suspension_data.constants import DATA_SOURCE_LOCATION
from suspension_data.dto import SuspensionCsvDto
from suspension_data.models import SuspensionRecord


def read_csv_content():
    dto: Final[SuspensionCsvDto] = SuspensionCsvDto(f'{DATA_SOURCE_LOCATION}/university_suspension_data.csv')
    records: Final[tuple[SuspensionRecord]] = dto.to_suspension_records()

    # pretty print the records
    for record in records:
        print(record.serializable_dict)


def start():
    read_csv_content()


if __name__ == '__main__':
    # This is needed to run the script from the root directory
    os.chdir('..')
    start()
