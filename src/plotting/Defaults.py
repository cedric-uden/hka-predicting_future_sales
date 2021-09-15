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

    # rcParams documentation: https://matplotlib.org/stable/tutorials/introductory/customizing.html

    plt.rcParams['lines.color'] = iwi_purple  # override acf, pacf colors
    plt.rcParams['lines.markersize'] = 4
    plt.rcParams['lines.markerfacecolor'] = hka_red
    plt.rcParams['figure.figsize'] = (30,10)
    plt.rcParams['legend.fontsize'] = 34
    plt.rcParams['axes.titleweight'] = 'extra bold'
    plt.rcParams['axes.labelweight'] = 'bold'

    plt.rcParams['xtick.direction'] = 'inout'

    # spacing options
    plt.rcParams['font.size'] = 30
    plt.rcParams['axes.titlepad'] = 15
    plt.rcParams['axes.labelpad'] = 20
    plt.rcParams['xtick.major.pad'] = 10
    plt.rcParams['ytick.major.pad'] = 10
    plt.rcParams['legend.borderaxespad'] = 1
