import pandas as pd

def extract_data(sources):
    df_list = []
    for source in sources:
        if source.endswith('.csv'):
            df = pd.read_csv(source)
            df_list.append(df)
        # Add other source types here (e.g., database, API)
    return pd.concat(df_list, ignore_index=True)
