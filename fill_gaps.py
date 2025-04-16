import pandas as pd

df = pd.read_csv('ML-gigs.csv')

df['rating'].fillna('Unranked Gig', inplace=True)
df['reviews'].fillna('No Reviewed', inplace=True)
df['seller_level'].fillna('Unleveled', inplace=True)

df.to_csv('ML-gigs.csv', index=False)
