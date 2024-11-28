import pandas as pd

# ecris moi qui script qui garde que les lgignes dont la date est compris entre 2024-01-01 et 2024-01-31 dans le csv carrefour_data.csv other_enseignes.csv,et comparaison_prix_carrefour.csv
def filter_dates(file_path, start_date, end_date):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    filtered_df.to_csv(file_path, index=False)

start_date = '2024-01-01'
end_date = '2024-01-31'

files = [
    '/Users/macbookpro/Documents/COURS/Business Intelligence /Jour2/Exauce/data/carrefour_data.csv',
    '/Users/macbookpro/Documents/COURS/Business Intelligence /Jour2/Exauce/data/other_enseigne_data.csv',
    '/Users/macbookpro/Documents/COURS/Business Intelligence /Jour2/Exauce/data/comparaison_prix_carrefour.csv'
]

for file in files:
    filter_dates(file, start_date, end_date)


