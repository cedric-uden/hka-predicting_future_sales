def compute_lag_feature(df, lags, feature):
    for i in lags: # id_columns = ['date_block_num', 'shop_id', 'item_id']
        shifted = df[cl(id_columns, feature)].copy()
        shifted.columns = cl(id_columns, f"{feature}_lag_{str(i)}")
        shifted['date_block_num'] += i
        df = pd.merge(df, shifted, on=id_columns, how='left')
    return df