def transform_data(df):
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    
    if 'invoice_date' in df.columns:
        df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
    
    if 'hs_code' in df.columns:
        df['hs_code'] = df['hs_code'].astype(str).str.zfill(6)
    
    return df
