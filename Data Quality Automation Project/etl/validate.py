import pandas as pd

def validate_data(df, rules):
    errors = []

    if 'hs_code' in df.columns:
        invalid_hs = df[df['hs_code'].isnull() | (df['hs_code'] == '')]
        for i, row in invalid_hs.iterrows():
            errors.append({'row': i, 'column': 'hs_code', 'error': 'Missing HS Code'})

    if 'country_code' in df.columns:
        valid_countries = rules.get('valid_country_codes', [])
        invalid_country = df[~df['country_code'].isin(valid_countries)]
        for i, row in invalid_country.iterrows():
            errors.append({'row': i, 'column': 'country_code', 'error': 'Invalid Country Code'})

    if 'tax_amount' in df.columns and 'invoice_total' in df.columns:
        mismatches = df[df['tax_amount'] > df['invoice_total']]
        for i, row in mismatches.iterrows():
            errors.append({'row': i, 'column': 'tax_amount', 'error': 'Tax > Invoice Total'})

    error_df = pd.DataFrame(errors)
    return df, error_df
