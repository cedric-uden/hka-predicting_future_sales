import pandas as pd


def get_train():
    """Returns the `sales_trains` CSV File."""
    return pd.read_csv("../../data/technical/sales_train.csv")
