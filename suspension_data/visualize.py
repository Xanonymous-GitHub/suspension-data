import matplotlib.pyplot as plt


def plot_data(x_list: list[int], y_list: list[int]):
    plt.plot(x_list, y_list)
    plt.xlabel('Year')
    plt.ylabel('Number of Suspensions')
    plt.title('Suspensions by Year')
    plt.show()
