def get_item_cnt_metric(df):
    """
    Return the `item_cnt_****` metric present in the dataset. Either
    `item_cnt_day` or `item_cnt_month` are expected.
    """
    cols = list(df.columns)
    res = list(filter(lambda x: "item_cnt_" in x, cols))
    return str(res[0]) if len(res) == 1 else None
