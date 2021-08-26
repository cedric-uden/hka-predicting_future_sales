import pandas as pd


def format_timestrings_inside_pd(pd_to_format):
    """
    Pass a dataframe which contains the `date` field. Convert this `date` field
    into a datetime format and then apply a lambda functions which converts the
    string into the format `%Y-%m`.
    """
    pd_to_format['date'] = pd.to_datetime(pd_to_format['date'], dayfirst=True)
    pd_to_format['date'] = pd_to_format['date'].apply(lambda x: x.strftime('%Y-%m'))
    return pd_to_format
