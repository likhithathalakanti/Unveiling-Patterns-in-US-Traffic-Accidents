if __name__ == "__main__":
    file_path = "data/US_Accidents_Dec21_updated.csv"
    df = load_data(file_path)
    df = preprocess_data(df)
    explore_data(df)
    df = prepare_features(df)
    model = train_model(df)
    evaluate_model(model, df)
