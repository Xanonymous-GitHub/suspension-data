from matplotlib.font_manager import FontProperties
from suspension_data.enums.enums import SuspensionReason, Gender, EducationProgram, SchoolType
from matplotlib.pyplot import gca
import matplotlib.pyplot as plt
import numpy as np

def plot_data(x_list: list[int], y_list: list[int]) -> None:
    plt.plot(x_list, y_list)
    plt.xlabel("Year")
    plt.ylabel("Number of Suspensions")
    plt.title("Suspensions by Year")
    plt.show()

def plot_gender_data(year_list: list[int], male_list: list[int], female_list: list[int]) -> None:
    plt.plot(year_list, male_list, label="male")
    plt.plot(year_list, female_list, label="female")
    plt.xlabel('Year')
    plt.ylabel('Number of Suspensions')
    plt.title('Suspensions by Year')
    plt.legend()
    plt.show()

def plot_school_type_data(year_list: list[int], public_list: list[int], private_list: list[int]) -> None:
    plt.plot(year_list, public_list, label="public")
    plt.plot(year_list, private_list, label="private")
    plt.xlabel('Year')
    plt.ylabel('Number of Suspensions')
    plt.title('Suspensions by Year')
    plt.legend()
    plt.show()

def plot_program_data(year_list: list[int], programs_list, program_type_list) -> None:
    plt.plot(year_list, programs_list[0], label="test1")
    plt.plot(year_list, programs_list[1], label="test2")
    plt.plot(year_list, programs_list[2], label="test1")
    plt.plot(year_list, programs_list[3], label="test1")
    plt.plot(year_list, programs_list[4], label="test1")
    plt.plot(year_list, programs_list[5], label="test1")
    plt.xlabel('Year')
    plt.ylabel('Number of Suspensions')
    plt.title('Suspensions by Year')
    plt.legend()
    plt.show()