def load_data(df, error_df, paths):
    df.to_csv(paths['cleaned_data'], index=False)
    error_df.to_csv(paths['error_log'], index=False)
    print(f"Saved cleaned data to {paths['cleaned_data']}")
    print(f"Saved error log to {paths['error_log']}")
