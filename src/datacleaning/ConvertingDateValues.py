iso8601_format = '%Y-%m-%d'


def date_to_month(df):
    """
    Pass a dataframe with a column "date" containing daily values.
    Transform said values to a monthly interval.
    """
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m'))
    return df


def date_to_iso8601(df):
    """
    Pass a dataframe with a column "date" containing daily values.
    Transform said values to an ISO8601 matching format.
    """
    df['date'] = df['date'].apply(lambda x: x.strftime(iso8601_format))
    return df
