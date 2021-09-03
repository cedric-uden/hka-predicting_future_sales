import pandas as pd


def date_to_month(df):
    """
    Pass a dataframe with a column "date" containing daily values.
    Transform said values to a monthly interval.
    """
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    return df
