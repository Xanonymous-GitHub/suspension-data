from typing import Optional, Final

from pandas import read_csv, DataFrame

from suspension_data.enums import Gender, EducationProgram, SchoolType, SuspensionReason
from suspension_data.models import SuspensionRecord

CSV = DataFrame


class SuspensionCsvDto:
    __csv_file_path: Final[str]

    # These are the columns that we expect to drop.
    # The "Category5Title" column is dropped because it is empty.
    __expect_drop_columns: Final[tuple[str]] = 'Unknown'

    # These are the positions of the columns that we expect to have.
    # Note that the positions are 0-based, and the drop columns are not included.
    GENDER_POS: Final[int] = 0
    PROGRAM_POS: Final[int] = 1
    SCHOOL_TYPE_POS: Final[int] = 2
    REASON_POS: Final[int] = 3
    YEAR_POS: Final[int] = 4
    COUNT_POS: Final[int] = 5

    def __init__(self, csv_file_path: str) -> None:
        self.__csv_file_path = csv_file_path

    def __read_csv_content(self) -> CSV:
        return read_csv(self.__csv_file_path, encoding='utf-8')

    def __remove_unnecessary_columns(self, csv: CSV) -> CSV:
        return csv.drop(columns=self.__expect_drop_columns)

    def __from_row_to_suspension_record(self, row: tuple) -> Optional[SuspensionRecord]:
        raw_gender: Final[str] = row[self.GENDER_POS]
        if Gender.is_valid(raw_gender):
            gender: Final[Gender] = Gender(raw_gender)
        else:
            # Filter out the 'total' value.
            return None

        raw_program: Final[str] = row[self.PROGRAM_POS]
        if EducationProgram.is_valid(raw_program):
            program: Final[EducationProgram] = EducationProgram(raw_program)
        else:
            # Filter out the 'total' value.
            return None

        raw_school_type: Final[str] = row[self.SCHOOL_TYPE_POS]
        if SchoolType.is_valid(raw_school_type):
            school_type: Final[SchoolType] = SchoolType(raw_school_type)
        else:
            # Filter out the 'total' value.
            return None

        raw_reason: Final[str] = row[self.REASON_POS]
        if SuspensionReason.is_valid(raw_reason):
            reason: SuspensionReason = SuspensionReason(raw_reason)
        else:
            reason: Final[SuspensionReason] = SuspensionReason.OTHER

        # For this column, we should remove the last two characters, which are the "00" part.
        raw_year: Final[str] = row[self.YEAR_POS]
        if isinstance(raw_year, str):
            year: Final[int] = int(raw_year[:-2])
        elif isinstance(raw_year, int):
            year: Final[int] = raw_year // 100
        else:
            year: Final[int] = -1

        count: Final[int] = int(row[self.COUNT_POS])

        return SuspensionRecord(
            gender=gender,
            program=program,
            school_type=school_type,
            suspension_reason=reason,
            year=year, count=count
        )

    def to_suspension_records(self) -> tuple[SuspensionRecord]:
        raw_csv: Final[CSV] = self.__read_csv_content()
        cleared_csv: Final[CSV] = self.__remove_unnecessary_columns(raw_csv)

        records: Final[list[SuspensionRecord]] = list()
        for row in cleared_csv.itertuples(index=False):
            record = self.__from_row_to_suspension_record(row)
            if record is not None:
                records.append(record)

        return tuple(records)
