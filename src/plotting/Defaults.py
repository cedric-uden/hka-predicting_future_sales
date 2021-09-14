import matplotlib.pyplot as plt

hka_red = '#D72305'
iwi_purple = '#64378C'


def set_defaults():
    """
    Set the matplotlib default parameters used for this project.
    This is to be reused in the main notebook as well as the more
    in depth analysis of the data at hand.
    This method helps to maintain a uniform look across the project.
    """

    plt.rcParams['lines.color'] = iwi_purple  # override acf, pacf colors
    plt.rcParams['lines.markersize'] = 4
    plt.rcParams['lines.markerfacecolor'] = hka_red
    plt.rcParams['figure.figsize'] = (30,10)
    plt.rcParams['legend.fontsize'] = 16
