# Train model
def train_model(df):
    lr = LinearRegression(featuresCol="features", labelCol="Severity")
    model = lr.fit(df)
    return model
