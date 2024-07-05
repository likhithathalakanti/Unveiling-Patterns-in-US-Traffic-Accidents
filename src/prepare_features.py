# Prepare features for modeling
def prepare_features(df):
    feature_cols = ['Start_Lat', 'Start_Lng', 'End_Lat', 'End_Lng', 'Distance']
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
    df = assembler.transform(df)
    return df
