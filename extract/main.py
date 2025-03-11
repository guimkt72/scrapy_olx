import pandas as pd



df = pd.read_json('data/teste3.json')


print(df)

df['product_name'] = df['product_name'].str.lower()




print(df)