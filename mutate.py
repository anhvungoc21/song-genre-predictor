import pandas as pd

# Permanently mutated original dataset.csv to have a preview_url column
df = pd.read_csv('./dataset.csv')
df['preview_url'] = pd.Series(['' for _ in range(len(df))]) 

df.to_csv('./dataset.csv', sep=',', encoding='utf-8')