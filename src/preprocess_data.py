def preprocess_data(df):
    # Drop rows with missing values
    df = df.dropna()
    return df
