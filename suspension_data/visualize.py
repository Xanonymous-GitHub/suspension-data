import matplotlib.pyplot as plt
from frozendict import frozendict
from matplotlib import rcParams
from matplotlib.font_manager import fontManager

from suspension_data.constants import ASSETS_LOCATION
from suspension_data.enums.enums import EducationProgram, Gender, SchoolType

fontManager.addfont(path=f"{ASSETS_LOCATION}/TaipeiSans.ttf")
rcParams["font.family"] = "Taipei Sans TC Beta"


def plot_data(year_separated_record_dict: frozendict[int, int]) -> None:
    plt.plot(
        [*year_separated_record_dict.keys()], [*year_separated_record_dict.values()]
    )
    plt.xlabel("Year")
    plt.ylabel("Number of Suspensions")
    plt.title("Suspensions by Year")
    plt.show()


def plot_gender_data(
    gender_separated_record_dict: frozendict[int, frozendict[Gender, int]]
) -> None:
    years = [*gender_separated_record_dict.keys()]

    males = [gender_separated_record_dict[year][Gender.BOY] for year in years]
    females = [gender_separated_record_dict[year][Gender.GIRL] for year in years]

    plt.plot(years, males, label="male")
    plt.plot(years, females, label="female")
    plt.xlabel("Year")
    plt.ylabel("Number of Suspensions")
    plt.title("Suspensions by Gender")
    plt.legend()
    plt.show()


def plot_school_type_data(
    school_type_separated_record_dict: frozendict[int, frozendict[SchoolType, int]]
) -> None:
    years = [*school_type_separated_record_dict.keys()]

    opens = [
        school_type_separated_record_dict[year][SchoolType.PUBLIC] for year in years
    ]
    privates = [
        school_type_separated_record_dict[year][SchoolType.PRIVATE] for year in years
    ]

    plt.plot(years, opens, label="public")
    plt.plot(years, privates, label="private")
    plt.xlabel("Year")
    plt.ylabel("Number of Suspensions")
    plt.title("Suspensions by School Type")
    plt.legend()
    plt.show()


def plot_education_program_data(
    program_separated_record_dict: frozendict[int, frozendict[EducationProgram, int]]
) -> None:
    years = [*program_separated_record_dict.keys()]

    for edu_prog in EducationProgram:
        plt.plot(
            years,
            [program_separated_record_dict[year][edu_prog] for year in years],
            label=edu_prog.value,
        )

    plt.xlabel("Year")
    plt.ylabel("Number of Suspensions")
    plt.title("Suspensions by Education Program")
    plt.legend()
    plt.show()
