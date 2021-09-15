def compute_lag_feature(df, lags, features):
    id_columns = ['date_block_num', 'shop_id', 'item_id']
    # N.B. `cl` concatenates elements from a lists with other elements
    for n in lags:
        shifted = df[cl(id_columns, features)].copy()
        shifted.columns = cl(id_columns, f"{features}_lag_{str(n)}")
        shifted['date_block_num'] += n
        df = pd.merge(df, shifted, on=id_columns, how='left')
    return df
