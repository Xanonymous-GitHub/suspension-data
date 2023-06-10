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

def plot_gender_data(year_list: list[int], male_list: list[int], female_list) -> None:
    plt.plot(year_list, male_list, label="male")
    plt.plot(year_list, female_list, label="female")
    plt.xlabel('Year')
    plt.ylabel('Number of Suspensions')
    plt.title('Suspensions by Year')
    plt.legend()
    plt.show()