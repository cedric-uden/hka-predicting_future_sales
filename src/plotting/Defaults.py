import matplotlib.pyplot as plt


def set_defaults():
    """
    Set the matplotlib default parameters used for this project.
    This is to be reused in the main notebook as well as the more
    in depth analysis of the data at hand.
    This method helps to maintain a uniform look across the project.
    """

    plt.rcParams['lines.marker'] = 'o'
    plt.rcParams['lines.markersize'] = 4
    plt.rcParams['lines.markerfacecolor'] = 'red'
